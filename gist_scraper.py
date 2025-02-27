#!/usr/bin/python3
import requests
import json
import hashlib
import time
from malicious_signatures import malicious_indicators

# Github Gists API: https://docs.github.com/en/free-pro-team@latest/rest/reference/gists
# Useful functionality:
# List public gists
# List gist commits
# List gist forks

application_types = [
	'text/plain',
	'x-sh',
	'x-msdos-program'
]

def get_public_gists():
	# return a list of the filenames, filetypes and URLs of the most recent gists
	response = requests.get(
    		'https://api.github.com/gists/public',
    		headers={'Accept': 'application/vnd.github.v3+json'}
	)
	json_response = response.json()
	file_list = [entry['files'] for entry in json_response]
	# replace with list comprehension
	content = []
	for f in file_list:
		for g in f.items():
			content.append({
				'filename':g[1]['filename'], 
				'url': g[1]['raw_url'], 
				'type': g[1]['type']})
	return content

def get_gist_content(gist):
	content = requests.get(gist['url'])
	return content.text

#@TODO
def get_gist_commits():
	pass

#@TODO
def get_gist_forks():
	pass

def filter_application_types(gists):
	# filter list of gists to ones with approved filetypes
	return [gist for gist in gists if gist['type'] in application_types]

def contains_malicious_indicators(malicious_indicators, gist_content):
	# returns signature type depending on whether the gist content
	# contains any of the malicious indicator
	for item in malicious_indicators.items():
		if item[1] in gist_content:
			return item[0]

def write_content_to_file(content, signature):
	# take in the content of a github gist and write it to disk
	# filename format: <md5hash>.<indicator type>
	content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
	filename = content_hash + '.' + signature
	sample_file = open(filename, 'w')
	sample_file.write(content)
	sample_file.close()

def run():
	while True:
		gists = get_public_gists()
		filtered_gists = filter_application_types(gists)
		for gist in filtered_gists:
			content = get_gist_content(gist)
			signature = contains_malicious_indicators(malicious_indicators, content)
			if signature:
				write_content_to_file(content, signature)
		time.sleep(300)

if __name__ == '__main__':
	run()
