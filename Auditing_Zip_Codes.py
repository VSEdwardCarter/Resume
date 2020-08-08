import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict

# Functions for auditing post_codes
expected=(98101,98102,98103,98104,98105,98106,98107,98108,98109,98110,98111,98112,
            98113,98114,98115,98116,98117,98118,98119,98121,98122,98124,98125,98126,
            98127,98129,98131,98133,98134,98136,98138,98139,98141,98144,98145,98146,
            98148,98154,98155,98158,98160,98161,98164,98165,98166,98168,98170,98174,
            98175,98177,98178,98181,98185,98188,98190,98191,98194,98195,98198,98199)
expected=map(str, expected)

# Function for counting Post_codes.
def post_codes(Filename):
    count = 0
    data = set()

    for event, elem in ET.iterparse(Filename, events=("start",)):
        if elem.tag == 'node' or elem.tag == 'way':
            for tag in elem.iter('tag'):
                if tag.attrib['k'] == "addr:postcode":
                    count += 1
                    data.add( tag.attrib['v'] )

    return count, data



#Auditing Post_codes

#wrong_postcode Identification
def audit_postcode_range(postcode, wrong_postcode, tag):
    if tag.attrib["v"] in expected:
        if tag.attrib["v"] not in postcode:
            postcode[tag.attrib["v"]]=1
        else:
            postcode[tag.attrib["v"]]+=1
    else:
        if tag.attrib["v"] not in wrong_postcode:
            wrong_postcode[tag.attrib["v"]]=1
        else:
            wrong_postcode[tag.attrib["v"]]+=1

def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def process_map_postcodes(Filename):
    postcode={}
    wrong_postcode={}
    osm_file = open(Filename, "r")
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postcode(tag):
                    audit_postcode_range(postcode, wrong_postcode, tag)
    return postcode, wrong_postcode
