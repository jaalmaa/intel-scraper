#!/usr/bin/python3

import time
import datetime
import pastebin_scraper
import signatures

# It needs to work like this:
# Read in timestamp of most recent paste search (stored in log file)
# Search for any new pastes since that timestamp.
# Match any of the new pastes for developed signatures
# If there's a match, store each one in its own file with the following naming convention:
#	<md5_filehash>.<intel_type>
#	e.g. matching an MZ header would store the file like the following:
#		60b725f10c9c85c70d97880dfe8191b3.PE
# eventually this data will instead be sent to the API service to be stored in MongoDB
# but for now this just needs to be a proof of concept to make sure the scraping works.
#
# Might hit IP rate-limits eventually, but could deploy this in the cloud and run it
# through TOR which should refresh the IP in each scraping interval anyway.

while true:
	try:
		with open('pastebin_scraper.log', 'rw') as log:
			# check for most recent paste search
			pass
	except FileNotFoundError:
		# create file and write current datetime
		pass
		
	posts = pastebin_scraper.get_new_posts()
	for post in posts:
		threat = signatures.match(post)
		if threat:
			with open('<MD5sum>.<Filetype>', 'rw') as sample_file:
				# write the contents of the file to the opened file
				sample_file.write(post.contents)
				sample_file.close()
		else:
			pass

	# sleep for 30 minutes
	time.sleep(1800)
