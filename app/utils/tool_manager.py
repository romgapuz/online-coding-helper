import os
import imp
import importlib
import app.utils.helper as helper
import sys

class ToolManager(object):
    def __init__(self, tool):
        # get the module
        tool_abspath =  '%s/%s.py' % (
            os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools')),
            helper.dash_case_to_underscore_case(tool)
        )
        _module = imp.load_source(helper.dash_case_to_title_case(tool), tool_abspath)

        # get the class within the module
        _class = getattr(_module, helper.dash_case_to_title_case(tool))

        # save class instance
        self._instance = _class()

    def execute(self, **kwargs):
        try:
            # execute the tool
            return self._instance.execute(**kwargs)
        except:
            return "Error: {}".format(sys.exc_info()[0])

    def get_title(self):
        return self._instance.get_title()

    def get_description(self):
        return self._instance.get_description()

    def get_label(self, index=0):
        return self._instance.get_label(index)

    def get_placeholder(self, index=0):
        return self._instance.get_placeholder(index)