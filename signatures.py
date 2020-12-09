#!/usr/bin/python3

# This file will be responsible for handling the signature matching logic
# as well as the signatures themselves. 

rules = {
	'portable_executable': '<REGEX_MATCH>',
	'bash_script': '<DETECTION_METHOD'
}

def match(content):
	# take in a parameter 'content' and match it against each of
	# the rules to determine if this paste is indeed malicious
	# and, if so, what type of file it is, and return it as a dictionary object.
	pass
