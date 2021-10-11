from abc import ABCMeta, abstractmethod


class Request:
    """請求內容"""
    def __init__(self, name, day_off, reason):
        self._name = name
        self._day_off = day_off
        self._reason = reason
        self._leader = None

    def get_name(self):
        return self._name

    def get_day_off(self):
        return self._day_off

    def get_reason(self):
        return self._reason


class Responsible(metaclass=ABCMeta):
    """責任人的抽象類別"""
    def __init__(self, name, title):
        self._name = name
        self._title = title
        self._next_handler = None

    def get_name(self):
        return self._name

    def get_title(self):
        return self._title

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler

    def get_next_handler(self):
        return self._next_handler

    def handle_request(self, request):
        """請求處理"""
        # 當前責任人處理請求
        self._handle_request_impl(request)
        # 如果存在下一個責任人，則傳遞給下一責任人
        if self._next_handler is not None:
            self._next_handler.handle_request(request)

    @abstractmethod
    def _handle_request_impl(self, request):
        """真正處理請求方法"""
        pass


