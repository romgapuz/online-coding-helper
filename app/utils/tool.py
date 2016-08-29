from abc import ABCMeta, abstractmethod
import app.utils.helper as helper

class Tool(object):
    __metaclass__ = ABCMeta

    def __new__(self):
        instance = object.__new__(self)

        self.title = helper.title_case_to_sentence(self.__name__)
        self.description = ""
        self.label = []
        self.placeholder = []

        return instance

    @abstractmethod
    def execute(self, **kwargs):
        pass

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_label(self, index=0):
        try:
            return self.label[index]
        except IndexError:
            return ""

    def get_placeholder(self, index=0):
        try:
            return self.placeholder[index]
        except IndexError:
            return ""