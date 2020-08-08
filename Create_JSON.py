import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict
import Cleaning_Street as cs

mapping = {
            " St ": " Street ",
            " St": " Street ",
            " ST": " Street ",
            " St.": " Street ",
            " Rd.": " Road ",
            " Rd ": " Road ",
            " Rd": " Road ",
            " Ave ": " Avenue ",
            " Ave.": " Avenue ",
            " Av ": " Avenue ",
            " AVE ": " Avenue ",
            " Dr ": " Drive ",
            " Dr.": " Drive",
            " Blvd ": " Boulevard ",
            " Blvd": " Boulevard ",
            " Blvd.": " Boulevard ",
            " Ct ": " Centre ",
            " Ctr": " Centre",
            " Pl ": " Place ",
            " Pl": " Place ",
            " Ln ": " Lane ",
            " LN ": " Lane ",
            " Cir ": " Circle ",
            " Wy": " Way ",
}




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


CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        # created dict
        node['created'] = {}
        for k in CREATED:
            node['created'][k] = element.get(k)

        # position array
        if element.attrib.get('lat') and element.attrib.get('lon'):
            lat = float(element.attrib.get('lat'))
            lon = float(element.attrib.get('lon'))
            node['pos'] = [lat, lon]

        # id, type, & visible keys
        node['id'] = element.attrib['id']
        node['type'] = element.tag
        if element.attrib.get('visible'):
            node['visible'] = element.attrib['visible']

        # process tags
        for tag in element.iter('tag'):
            key = tag.attrib['k']
            value = tag.attrib['v']
            if not problemchars.search(key):
                if key[:5] == 'addr:':
                    if 'address' not in node:
                        node['address'] = {}
                    if ':' not in key[5:]:
                        node['address'][key[5:]] = value

        # process nodes
        for nd in element.iter('nd'):
            if 'node_refs' not in node:
                node['node_refs'] = []
            node['node_refs'].append(nd.attrib['ref'])

        return node
    else:
        return None


def process_map(filename, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(filename)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(filename):
            el = shape_element(element)
            if el:
                el = cs.update_name(el, mapping)
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data
