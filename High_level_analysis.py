import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    if element.tag == "tag":
        if lower.search(element.attrib['k']):
            keys['lower'] += 1
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon'] += 1
        elif problemchars.search(element.attrib['k']):
            keys['problemchars'] = keys['problemchars'] + 1
        else:
            keys['other'] += 1
#            print element.attrib['k']
#            print element.attrib['v']
    return keys

# Function for counting keys by type
def process_map_keys(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

# Function for counting tags
def count_tags(filename):
    count = defaultdict(int)
    for item in ET.iterparse(filename):
        count[item[1].tag] += 1
    return count

# Getting users and count

def get_user(element):
    return element.get('user')


def process_users_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.get('user'):
            users.add(get_user(element))
        element.clear()
    return users


with open("Seattle.osm",'rb') as f:
    users = process_users_map("Seattle.osm")

print len(users)   ##Gets number of users
pprint.pprint(users)  ##Lists all the users
f.close()
