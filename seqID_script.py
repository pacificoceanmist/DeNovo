import sys
import os

file_path = /var2/sj-won/de_novo/data/transdecoder_dir/Trinity.fasta.transdecoder.pep.cdhit
search_str = `\.p1'

def extract_text(file_path,search_str):
	with open(file_path, 'r') as file:
		text = file.read()
		match = re.search(search_string, text)
		if match:
			seqID = return match.group()
		else:
			return "No match found."

print(seqID)