from app.utils.tool import Tool
import subprocess

class Ping(Tool):
    def __init__(self):
        self.description = """Ping is a tool mostly used to troubleshoot connectivity to a
            website or ip address."""

    def execute(self, **kwargs):
        p = subprocess.Popen(
            ['ping', '-c1', kwargs['one']],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        return out