#!/usr/bin/python3
import requests
import json

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
	# get the contents of a gist from its url
	pass

def get_gist_commits():
	pass

def get_gist_forks():
	pass

if __name__ == '__main__':
	gists = get_public_gists()
	#for gist in gists:
	#	print({gist['url']:gist['type']})
	types = [gist['type'] for gist in gists]
	print(set(types))
