#!/usr/bin/env python 

import re

"""For extracting Time and SEQ no"""
# opening files
with open("node0_tcpdump.txt","r") as inputfile :
	with open("time_SEQ.txt","w") as outputfile :
		# Reading line by line
		lines = inputfile.readlines()
		for line in lines:
			# Checking existence of "seq" in line
			if "seq" in line :
				words = line.split()
				outputfile.write(words[0] + " ")
				# Reading word by word in line
				i=0
				for w in words :		
					if words[i] == "seq":
						if ':' in words[i+1] :
							seq = words[i+1].split(':')
							outputfile.write(seq[0])
				
						elif ',' in words[i+1]:	
							seq=words[i+1].split(',')[0]		
							outputfile.write(seq[0])
						# To change line after writing Seq no.
						outputfile.write("\n")
					i=i+1

"""For extracting Time and ACK no"""
with open("node0_tcpdump.txt","r") as inputfile :
	with open("time_ACK.txt","w") as outputfile2 :
			# Reading line by line
			lines = inputfile.readlines()
			for line in lines:
				# Checking existence of "seq" in line
				if "ack" in line :
					if "seq" not in line:
						words = line.split()
						outputfile2.write(words[0] + " ")
						# Reading word by word in line
						i=0
						for w in words :		
							if words[i] == "ack":
								if ',' in words[i+1] :
									seq = words[i+1].split(',')
									outputfile2.write(seq[0])
								# To change line after writing Seq no.
								outputfile2.write("\n")
							i=i+1		
