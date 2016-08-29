from app.utils.tool import Tool
import subprocess, string, random, os

class ParseX509Certificate(Tool):
    def __init__(self):
        self.title = "Parse X.508 Certificate"
        self.description = """This tool parses an X.509 certificate and output a human-readable
            value."""

    def execute(self, **kwargs):
        # create random file and save certificate
        filename = self.generate_id()
        print(filename)
        f = open(filename, 'w')
        f.write(kwargs['one'])
        f.close()

        # parse certificate
        p = subprocess.Popen(
            ['openssl', 'x509', '-text', '-noout', '-in', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = p.communicate()

        # delete file
        os.remove(filename)

        return out

    def generate_id(self, size=32, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))