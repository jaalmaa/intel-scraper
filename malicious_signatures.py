#!/usr/bin/python3

malicious_indicators = {
	'pe_base64': 'TVqQA',
	'pe_base64_2': 'TVpQ',
	'base64_gz': 'H4sI',
	'elf64': 'f0VMR',
	'sh_script': '!/bin/bash',
	'powershell': 'powershell',
	'powershell_webclient': 'Net.WebClient',	
	'powershell_script': 'Invoke-',
	'vba': 'Auto_Open()',
	'vbs': 'wcript.shell'
}

ignore = [
	'chocolatey'
]
