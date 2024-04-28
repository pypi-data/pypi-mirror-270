# -*- coding: utf-8 -*-

import logging

from typing import Dict, List, Any

from concopilot.framework.plugin import PluginManager
from concopilot.framework.interactor import BasicInteractor
from concopilot.framework.resource import ResourceManager
from concopilot.framework.cerebrum import InteractParameter, Cerebrum
from concopilot.framework.message import Message
from concopilot.framework.message.manager import MessageManager
from concopilot.framework.identity import Identity
from concopilot.util import ClassDict
from concopilot import Settings


settings=Settings()
logger=logging.getLogger(__file__)


class ChatInteractor(BasicInteractor):
    def __init__(
        self,
        config: Dict,
        resource_manager: ResourceManager,
        cerebrum: Cerebrum,
        plugin_manager: PluginManager,
        message_manager: MessageManager
    ):
        super(ChatInteractor, self).__init__(
            config,
            resource_manager,
            cerebrum,
            plugin_manager,
            message_manager
        )
        self.persist_history: bool = self.config.config.persist_history
        self.message_history_key=self.config.config.message_history_key
        self.hello_msg_content: str = self.config.config.hello_msg_content
        self.instructions: List[str] = []
        if self.config.config.instruction_file:
            with open(self.config_file_path(self.config.config.instruction_file), encoding='utf8') as file:
                self.instructions.append(file.read())
        self.exit_tokens: set[str] = set(self.config.config.exit_tokens)
        self.llm_param={}
        self.message_history: List[Message] = None

    def interact_loop(self):
        self.message_history=self.context.storage.get_or_default(self.message_history_key, []) if self.persist_history else []

        if len(self.message_history)>0:
            msg=self.message_history[-1]
            if self.message_history[-1].sender.role=='user':
                self.message_history=self.message_history[:-1]
                msg=self._interact_with_cerebrum(msg)
        else:
            msg=Message(
                sender=Identity(role='cerebrum', name=self.cerebrum.name),
                receiver=Identity(role='user'),
                content_type='text/plain',
                content=self.hello_msg_content,
                time=settings.current_time()
            )
            self.message_history.append(msg)
        self.status=BasicInteractor.Status.RUNNING
        while self.status==BasicInteractor.Status.RUNNING:
            try:
                self.context.user_interface.send_msg_to_user(msg)
                msg=self._check_user_msg()
                if msg is None or msg.content in self.exit_tokens:
                    break
                msg=self._interact_with_cerebrum(msg)
            except Exception as e:
                logger.error('An error happened.', exc_info=e)
                msg=Message(
                    sender=Identity(role='system'),
                    receiver=Identity(role='user'),
                    content_type="<class 'dict'>",
                    content=ClassDict(
                        error=type(e).__name__,
                        detail=str(e)
                    ),
                    time=settings.current_time()
                )

        if self.persist_history:
            self.context.storage.put(self.message_history_key, self.message_history)

        self.status=BasicInteractor.Status.STOPPED

    def _check_user_msg(self):
        while msg:=self.context.user_interface.wait_user_msg():
            if msg is not None:
                if msg.receiver and msg.receiver.role=='interactor':
                    self.context.user_interface.send_msg_to_user(self.on_msg(msg))
                else:
                    break
            else:
                logger.warning('User interface pipeline is broken. Will exit.')
                break
        return msg

    def _interact_with_cerebrum(self, msg):
        self.message_history.append(msg)
        response=self.cerebrum.interact(param=InteractParameter(
            instructions=self.instructions,
            command=None,
            message_history=self.message_history,
            assets=[asset for asset in self.context.assets.values()],
            require_token_len=False,
            require_cost=False
        ), **self.llm_param)
        msg=self.message_manager.parse(response, thrd_id=msg.thrd_id)[0]
        msg.sender=Identity(role='cerebrum', id=self.cerebrum.id, name=self.cerebrum.name)
        if msg.receiver is None:
            msg.receiver=Identity(role='user')
        self.message_history.append(msg)
        return msg

    def set_llm_param(self, update: Dict, remove: List) -> Dict:
        if update:
            self.llm_param.update(update)
        if remove:
            for key in remove:
                if key in self.llm_param:
                    self.llm_param.pop(key)

        return self.llm_param

    def retrieve_history(self, max_count: int = None) -> List[Message]:
        if not max_count:
            max_count=len(self.message_history)
        return self.message_history[-max_count:]

    def clear_history(self) -> bool:
        self.message_history=[]
        return True

    def command(self, command_name: str, param: Any, **kwargs) -> Any:
        if command_name=='set_llm_param':
            return ClassDict(param=self.set_llm_param(param.get('update'), param.get('remove')))
        elif command_name=='retrieve_history':
            return ClassDict(histories=self.retrieve_history(param.get('max_count') if param else None))
        elif command_name=='clear_history':
            return ClassDict(status=self.clear_history())
        else:
            raise ValueError(f'Unknown command: {command_name}. Only "set_llm_param" is acceptable.')
