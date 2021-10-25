from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    """命令的抽象類別"""
    @abstractmethod
    def execute(self):
        pass


class CommandImplement(Command):
    """命令具體實現類別"""
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.do_something()


class Receiver:
    """命令的接收者"""
    def do_something(self):
        print('doing something...')


class Invoker:
    """調度者"""
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def action(self):
        if self._command is not None:
            self._command.excute()


