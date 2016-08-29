from pyramid.view import view_config
import yaml, os
from app.utils.tool_manager import ToolManager

class ToolView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='tool', renderer='../templates/tool_single.pt')
    def single(self):
        # get tool from url
        tool_slug = self.request.matchdict['tool']

        # get tool manager
        tool = ToolManager(tool_slug)

        if len(self.request.POST) > 0:
            return {
                'tool': tool_slug,
                'title': tool.get_title(),
                'description': tool.get_description(),
                'placeholder': tool.get_placeholder(),
                'inputText': self.request.POST['inputText'],
                'outputText': tool.execute(one=self.request.POST['inputText']),
                'home_menu': '',
                'about_menu': '',
                'toolbox_menu': 'active'
            }
        else:
            return {
                'tool': tool_slug,
                'title': tool.get_title(),
                'description': tool.get_description(),
                'placeholder': tool.get_placeholder(),
                'inputText': '',
                'outputText': '',
                'home_menu': '',
                'about_menu': '',
                'toolbox_menu': 'active'
            }

    @view_config(route_name='tool_2', renderer='../templates/tool_double.pt')
    def double(self):
        # get tool from url
        tool_slug = self.request.matchdict['tool']

        # get tool manager
        tool = ToolManager(tool_slug)

        if len(self.request.POST) > 0:
            return {
                'tool': tool_slug,
                'title': tool.get_title(),
                'description': tool.get_description(),
                'outputText': tool.execute(
                    one=self.request.POST['input1'],
                    two=self.request.POST['input2']
                ),
                'input1': tool.get_label(0),
                'input2': tool.get_label(1),
                'home_menu': '',
                'about_menu': '',
                'toolbox_menu': 'active'
            }
        else:
            return {
                'tool': tool_slug,
                'title': tool.get_title(),
                'description': tool.get_description(),
                'outputText': '',
                'input1': tool.get_label(0),
                'input2': tool.get_label(1),
                'home_menu': '',
                'about_menu': '',
                'toolbox_menu': 'active'
            }