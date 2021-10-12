from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """主題類別"""
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    """真實主題類別"""        
    def request(self, content=''):
        print(f'RealSubject todo something...{content}')


class ProxySubject(Subject):
    """代理人"""
    def __init__(self, name, real_subject):
        super().__init__(name)
        self._real_subject = real_subject
    
    def request(self):
        self.pre_request()
        if self._real_subject is not None:
            self._real_subject.request()
        self.after_request()

    def pre_request(self):
        print('Before Request')
    
    def after_request(self):
        print('After Request')


if __name__ == '__main__':
    realSubject = RealSubject('RealSubject')
    proxySubject = ProxySubject('ProxySubject', realSubject)
    proxySubject.request('This is request...')

