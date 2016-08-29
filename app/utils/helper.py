import re

def dash_case_to_title_case(string):
    splitted_string = string.split('-')
    class_ = string.__class__
    return class_.join(class_(''), map(class_.capitalize, splitted_string[0:]))

def dash_case_to_underscore_case(string):
    return string.replace('-', '_')

def title_case_to_sentence(string):
	return ' '.join(filter(None, re.split("([A-Z][^A-Z]*)", string)))