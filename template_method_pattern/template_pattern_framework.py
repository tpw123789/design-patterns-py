from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    """範本類別"""
    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

    def template_method(self):
        """範本方法"""
        self.step_one()
        self.step_two()
        self.step_three()


class TemplateImplA(Template):
    """範本實現類別"""
    def step_one(self):
        print('Step One.')

    def step_two(self):
        print('Step two.')

    def step_three(self):
        print('Step three.')


class TemplateImplB(Template):
    """範本實現類別"""
    def step_one(self):
        print('Step One.')

    def step_two(self):
        print('Step two.')

    def step_three(self):
        print('Step three.')



