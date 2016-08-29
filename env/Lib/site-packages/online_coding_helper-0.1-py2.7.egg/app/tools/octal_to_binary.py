from app.utils.tool import Tool

class OctalToBinary(Tool):
    def execute(self, **kwargs):
    	return bin(int(kwargs['one'], 8)).split('b')[1]