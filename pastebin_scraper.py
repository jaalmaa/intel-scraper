#!/usr/bin/python3

# This file will be responsible for handling the pastebin scraping
# for new posts. It will send a request to the following endpoint:
# hxxps://pastebin[.]com/archive
# and then gather a list of UIDs for each new paste before returning
# a list of each paste UID and its content in the form of a dictionary.

def get_new_posts(timestamp):
	# takes in a parameter timestamp which is a datetime object
	# and gets all new pastes since this timestamp
	pass
