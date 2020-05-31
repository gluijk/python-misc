# Parse JSON

import json

path = 'C:/_PARSE_JSON/'

source_filename = path + '2020-VDS7B9J3-April.txt'
dest_filename = path + '2020-VDS7B9J3-April_PARSEJSON.txt'


with open(source_filename) as json_file:
    with open(dest_filename, 'w') as dest_file:
        dest_file.write('deviceId;accountId;drmType;timeStamp\n')
        data = json.load(json_file)
        for p in data['devices']:
            dest_file.write(p['deviceId'] + ';' +
                            p['accountId'] + ';' +
                            p['drmType'] + ';' +
                            p['timeStamp'] + '\n')

# #####################################################33

# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# Writing JSON to a File
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# Reading JSON from a File
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
