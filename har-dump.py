#!/usr/bin/python

import sys
import json

if len(sys.argv) < 2:
    print('Syntax: ', sys.argv[0], ' filename')
    exit()

filename = sys.argv[1]

f = open(filename, 'r')
data = json.load(f)
f.close()

print('##### Dunp of file {}'.format(filename))
print('Pages')
for page in data['log']['pages']:
    print('  {}'.format(page['title']))

print('Entries')
for entry in data['log']['entries']:
    request = entry['request']
    response = entry['response']
    print('  {} : {:6s} {}'.format(entry['startedDateTime'], request['method'], request['url']))
    print('    response code {}'.format(response['status']))
    print('    execution time {}'.format(entry['time']))
