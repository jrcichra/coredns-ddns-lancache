#!/usr/bin/python3

# This script generates a partial Corefile from a lancache config

import socket
import logging
import pymysql
import os
import argparse
import glob

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


# Create the parser
my_parser = argparse.ArgumentParser(
    description='Converts a lancache config set to a Corefile')

# Add the arguments
my_parser.add_argument('d',
                       metavar='d',
                       type=str,
                       help='Directory with .txt files we are going to convert')
my_parser.add_argument('ip',
                       metavar='ip',
                       type=str,
                       help='The IP we want to redirect to')

args = my_parser.parse_args()

d = args.d
ip = args.ip

# Glob all the .txt files we find in the specified directory

# Pre output
output = """
pk5001z {
	log
    hosts /root/hosts
}
###END OF PRE
"""

for txt in glob.glob("{}/*.txt".format(d)):
    logging.info("Going to parse: {}".format(txt))
    # Open the file
    with open(txt, 'r') as f:
        # Loop through every newline
        lines = []
        for line in f:
            # Clean up the line
            line = line.strip().replace('*.', '')
            lines.append(line)
        # Loop through the unique set of lines
        for line in set(lines):
            # Skip it if we start with a comment
            if len(line) > 0 and line[0] != '#':
                # Make a block
                output += """
{} {{
    log
    forward . {} 1.1.1.1
}}
""".format(line, ip)

# Post output
output += """
###START OF POST
. {
    forward . 1.1.1.1 1.0.0.1
}
"""


print(output)
