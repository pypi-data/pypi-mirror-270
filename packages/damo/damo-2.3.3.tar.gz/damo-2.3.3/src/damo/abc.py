#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dont_do', action='store_false', dest='the_value')
parser.add_argument('--do', action='store_true', dest='the_value')
args = parser.parse_args()

print(args)
