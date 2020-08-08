import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict

#Builds the regex
OSMFILE = "test.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

#Builds the expected list of Road names
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons","Freeway","Circle","Strand","Sterling","Way","Highway",
            "Terrace","South","East","West","North","North East","North West","South East","South West"]

#Builds diction w/ keys that match to the regex
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

#Parses through the k attribute within addr:street
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

#Defined function to parse nodes and ways looking for street names
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types

# Function for counting street addresses
def street_number(file_name):
    count = 0

    for event, elem in ET.iterparse(file_name, events=("start",)):
        if elem.tag == 'node' or elem.tag == 'way':
            for tag in elem.iter('tag'):
                if tag.attrib['k'] == "addr:street":
                    count += 1
    return count


# Function for counting address attributes by type
def address_attribute(filename):
    address_attributes={}
    for event, elem in ET.iterparse(filename):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if re.search(re.compile("addr:.*$"),tag.get("k")):
                    if tag.get("k") in address_attributes:
                        address_attributes[tag.get("k")]+=1
                    else:
                        address_attributes[tag.get("k")]=1
    return address_attributes


# Function for sorting by place
def place_type(element, places):
    if element.tag == "node":
         for tag in element.iter('tag'):
                if tag.attrib['k'] == 'place':
                    if tag.attrib['v'] == 'city':
                        places['city'] += 1
                    elif tag.attrib['v'] == 'town':
                        places['town'] += 1
                    elif tag.attrib['v'] == 'village':
                        places['village'] += 1
                    elif tag.attrib['v'] == 'hamlet':
                        places['hamlet'] += 1
                    else:
                        places['other'] += 1

    return places

# Counting Places by type
def process_map_places(filename):
    places = {"city": 0, "town": 0, "village": 0, "hamlet" : 0, "other": 0}
    for _, element in ET.iterparse(filename):
        places = place_type(element, places)

    return places
