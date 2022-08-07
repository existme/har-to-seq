#!/usr/bin/python

import sys

import utils

if len(sys.argv) < 2:
    print('Syntax: ', sys.argv[0], ' filename')
    exit()

data = utils.read_json_file(sys.argv[1])

# Find all participants
participants = {}
p = 0
for entry in data['log']['entries']:
    request = entry['request']
    url = request['url']
    # https://auth.axis.com/user-center
    participant = utils.find_base_url(url)
    # print( "  {} - {}".format(participant,url))
    p += 1
    participants[participant] = "P" + str(p)

# print(participants)

print('@startuml')
print('actor "Me" as ME'.format(participant, participants[participant]))
for participant in participants:
    print('participant "{}" as {}'.format(participant, participants[participant]))

# user -> ua: POST "/v1.0/users/hid" {[hid1,hid2]} \nheader {api-key}
for entry in data['log']['entries']:
    request = entry['request']
    response = entry['response']
    url = request['method'] + ' ' + request['url']
    url = url[:100]
    code = response['status']
    participant = participants[utils.find_base_url(request['url'])]
    print('{} -> {}: "{}"'.format("ME", participant, url))
    print('{} -> {}: "{}"'.format(participant, "ME", code))

print('@enduml')
