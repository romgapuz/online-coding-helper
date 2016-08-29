from app.utils.tool import Tool
import cgi

class HtmlEscape(Tool):
    def execute(self, **kwargs):
        return cgi.escape(kwargs['one'], quote=True).\
           replace(u'\n', u'<br />').\
           replace(u'\t', u'&emsp;').\
           replace(u'  ', u' &nbsp;')