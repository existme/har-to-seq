#!/usr/bin/python

import sys

import utils

if len(sys.argv) < 2:
    print('Syntax: ', sys.argv[0], ' filename')
    exit()

data = utils.read_json_file(sys.argv[1])

print('##### Dunp of file {}'.format(sys.argv[1]))
print('Pages')
if 'pages' in data['log']:
    for page in data['log']['pages']:
        print('  {}'.format(page['title']))

print('Entries')
for entry in data['log']['entries']:
    request = entry['request']
    response = entry['response']
    print('  {} : {:6s} {}'.format(entry['startedDateTime'], request['method'], request['url']))
    print('    response code {}'.format(response['status']))
    print('    execution time {}'.format(entry['time']))
