# Resume
Portfolio
# OpenStreetMap Data Case Study
Edward J. Carter

"OpenStreetMap is built by a community of mappers that contribute and maintain data about roads, trails, cafés, railway stations, and much more, all over the world."(openstreetmap.org/about June 2020)

OpenStreetMap is a free mapping services that companies and individuals can use to build out robust geospatially derived applications. This project is my first introduction to the site and its capabilities. The UI provides for simplistic UX for individuals visiting the site. The ability to simply type the location your are looking into and have the map auto-center on the required location was great. However, the exporting of the data or specific data greatly decreased my experience.

For this project, the student is given the option of using either MongoDB or SQL. I selected to use MongoDB. MongoDB is instead of a relational data base a document-based database. Using and manipulating multiple high profile programmatic languages. I used the JSON capability of MongoDB for this project.

## Map Area Choice
Seattle (King County), Washington, United States

https://www.openstreetmap.org/export#map=12/47.6089/-122.3135

Originally for this project my intent was to use my home town of Raleigh, North Carolina (Wake County). However, the challenges presented by this area were to large in order to utilize. The requirement for the project is that the data be at least 50MB when uncompressed.

I alternately used the Seattle as my area for this project study. I wanted to use Seattle because it is in the State of Washington. A state that once I retire I intend to move to. Previously, I was stationed in Tacoma, Washington at Fort Lewis Washington. In fact, I have been stationed at Fort Lewis twice. The second time I was married and my wife fell in love with the area. We went to Seattle multiple time and it is easy to get turned around.

The creation of Capitol Hill Autonomous Zone, CHAZ and its transition to Capitol Hill Organized Protest fueled my curiousity further.

For exporting the OSM on OpenStreetMap I used:

## Initial Auditing of data
I downloaded the original file for Seattle at a size of 725.22 MB. [(os.path.getsize("Seattle.osm")/1.0e6)]

Once converted to a JSON file the size was at 760.21 MB. [(os.path.getsize("Seattle.osm.json")/1.0e6)]

The sample that was created was at the size of 14.63 MB. [(os.path.getsize("test.osm")/1.0e6)]

The intent in auditing the data is to learn the quality of the data and to determine if there are any problems that need to be corrected. Potential problems are missing data, incorrect structure, incorrect format of data, etc. The sources for these problems stem from user entry, poor coding, incorrect schema, legacy data, migration programmer error and corruption due to transmission.

Using OpenStreetMap data I expect to see the most numerous problem source as user entry. The fact that OpenStreetMap data is a free community that is sourced out to average everyday mappers implies that data might be very dirty and need cleaning.

### High level analysis
{'lower': 1083465, 'lower_colon': 1118022, 'other': 22784, 'problemchars': 0}

#### The OSM tags consisted of:
        'bounds': 1,
        'member': 114606,
        'meta': 1,
        'nd': 3431266,
        'node': 3035615,
        'note': 1,
        'osm': 1,
        'relation': 4487,
        'tag': 2224271,
        'way': 383300


#### Users associated with this OSM total 2690 and are:
['!MRGBoss', '-dx-', '0x1B', '123maps', '1luis1', '25or6to4', '3vandaag', '3xodus', '503Greg', '54806b45', '>LAND', '@eldang', 'AE35', 'ALeDonne', 'AMY-jin', 'ASayre8', 'ASwann90', 'Aaron Lidman', u'\u0417\u0435\u043b\u0451\u043d\u044b\u0439 \u041a\u043e\u0448\u0430\u043a', u'\u0418\u0432\u0430\u043d \u041f\u0438\u0440\u043e\u0433\u043e\u0432\u0441\u043a\u0438\u0439', u'\u0421\u0435\u043c\u0451\u043d \u0421\u0435\u043c\u0451\u043d\u043e\u0432', u'\u042e\u043a\u0430\u0442\u0430\u043d', u'\u5289 \u7152', u'\u738b\u7ff0\u6797']

#### Total number of unique keys (tag attrib['k'])is 434 and are:
'APN', 'GEO', 'PID', 'PTN', 'RP_ACCT_ID', 'SHAPE_AREA', 'SHAPE_LEN', 'SID', 'access', 'access:conditional', 'access:lanes', 'access:lanes:backward', 'access:lanes:forward', 'access_aisle', 'addr', 'addr:city', 'addr:country', 'addr:full', 'addr:housename', 'addr:housenumber', 'addr:postcode', 'addr:state', 'addr:street', 'addr:unit', 'amenity', 'contact:email', 'contact:facebook', 'contact:foursquare', 'contact:instagram', 'contact:linkedin', 'contact:phone', 'contact:tty', 'contact:twitter', 'contact:website', 'contact:yelp', 'contact:youtube', 'source', 'source:addr', 'source:addr:id', 'source:geometry', 'source:id', 'source:license', 'source:name', 'source:path', 'source:position', 'source:url', 'source_ref', 'telecom', 'tiger:cfcc', 'tiger:county', 'tiger:name_base', 'tiger:name_base_1', 'tiger:name_base_2', 'tiger:name_direction_prefix', 'tiger:name_direction_prefix_1', 'tiger:name_direction_suffix', 'tiger:name_direction_suffix_1', 'tiger:name_type', 'tiger:name_type_1', 'tiger:reviewed', 'tiger:separated', 'tiger:source', 'tiger:tlid', 'tiger:upload_uuid', 'tiger:zip_right'

## Data Audit (Problems and Corrections)
### Problem 1 (Auditing / Corrcting Zip Codes)
In this section I audited the Zip Codes in order to see what the quality of the data is. I selected a large area when downloading the OSM. To identify the correct zipcodes for Seattle, WA, I searched by city/state on the USPS website: https://tools.usps.com/zip-code-lookup.htm?bycitystate. The Website provied 60 zip codes associated with Seattle, WA. I created a script to identify the zip codes already present and count the total occurrence of a zip code. Then I wrote a script to the list zip codes associated with Seattle, the number of occurrences of that zipcode and place it in its own tuple. The same script identifies zip codes not associated with Seattle, the number of occurrences and places them in another tuple. Below are the results of the described scripts.

#### post_codes("test.osm") provides the count and zip codes present in the OSM
#### Total Count of Zip Code instances : 4514
#### Zip Codes present:
'98004', '98005', '98006', '98007', '98027', '98032', '98033', '98034', '98052', '98052-4176', '98053', '98056', '98059', '98101', '98102', '98103', '98104', '98105', '98106', '98107', '98108', '98109', '98110', '98112', '98115', '98116', '98117', '98118', '98119', '98121', '98122', '98125', '98126', '98133', '98134', '98136', '98144', '98146', '98168', '98177', '98178', '98195', '98199', '98516', '99007'

#### process_map_postcodes("test.osm") provides number of occurences per correct and incorrect zip codes.
#### Correct Zip Codes:Count
{'98101': 28, '98102': 93, '98103': 334, '98104': 44, '98105': 191, '98106': 173, '98107': 168, '98108': 187, '98109': 101, '98110': 4, '98112': 140, '98115': 348, '98116': 168, '98117': 265, '98118': 265, '98119': 119, '98121': 19, '98122': 180, '98125': 103, '98126': 150, '98133': 50, '98134': 31, '98136': 127, '98144': 186, '98146': 34, '98168': 11, '98177': 34, '98178': 9, '98195': 4, '98199': 163})

#### Incorrect Zip Codes: Count
{'98004': 13, '98005': 3, '98006': 4, '98007': 9, '98027': 1, '98032': 1, '98033': 386, '98034': 182, '98052': 62, '98052-4176': 3, '98053': 2, '98056': 88, '98059': 29, '98516': 1, '99007': 1}

Only one of the zip codes is not in the format of XXXXX. However, this zip code does not belong to the city of Seattle. The only correction that can/should be made is to make the initial query a smaller location.

### Problem 2 (Auditing / Correcting Addresses)
The sample document, test.osm, created from the original, Seattle.osm, was used to audit this data and identify any significant deviation from the a standard way of annotating locations and addresses within the sample. I started with a description of the places that can be found within the OSM. The addr:* and the count of each occurrence is presented also. I counted the number of occurrences of street numbers. I printed off the actual street names grouped by the actual street name type.

#### Description of places:
process_map_places("test.osm")

'city': 0
'hamlet': 2
'other': 3
'town': 0
'village': 0

#### Address Attributes:
address_attribute("test.osm")

'addr:city': 4603
'addr:country': 9
'addr:full': 2
'addr:housename': 5
'addr:housenumber': 4664
'addr:postcode': 4609
'addr:state': 148
'addr:street': 4665
'addr:unit': 281
'source:addr:id': 85


#### Total occurrences of street addresses
street_number("test.osm")
4555

#### Street Names by category type
audit("test.osm")

'Broadway'
{'Broadway'}

'Center':
{'Parkplace Center'}

'Circle':
{'Kirkland Circle', 'Northeast 37th Circle', 'Northeast 81st Circle'}

'East':
{'10th Avenue East', '11th Avenue East', '12th Avenue East', '13th Avenue East', '15th Avenue East', '16th Avenue East', '17th Avenue East', '18th Avenue East', '19th Avenue East', }

'Esplanade':
{'Northwest Esplanade'}

'N':
{'Bagley Ave N'}

'NE':
{'161st Avenue NE'}

'NW':
{'Ballard Ave NW'}

'North':
{'1st Avenue North', '2nd Avenue North', '3rd Avenue North', '4th Avenue North', '5th Avenue North', '6th Avenue North', '8th Avenue North', '9th Avenue North', 'Albion Place North' }

'Northeast':
{'100th Avenue Northeast', '100th Lane Northeast', '101st Avenue Northeast', '101st Place Northeast', '101st Way Northeast', '102nd Avenue Northeast', '102nd Lane Northeast', '102nd Place Northeast', '102nd Way Northeast' }

'Northwest':
{'10th Avenue Northwest', '11th Avenue Northwest', '12th Avenue Northwest', '13th Avenue Northwest', '14th Avenue Northwest', '15th Avenue Northwest', '16th Avenue Northwest', '17th Avenue Northwest', '18th Avenue Northwest' }

'Pl':
{'NW Dock Pl'}

'Plaza':
{'Lakeshore Plaza'}

'Point':
{'Carillon Point'}

'SE':
{'119TH AVE SE', '155TH LN SE'}

'ST':
{'109th ST'},

'South':
{'10th Avenue South', '11th Avenue South', '12th Avenue South', '13th Avenue South', '14th Avenue South', '15th Avenue South', '16th Avenue South', '17th Avenue South', '18th Avenue South' 'Wetmore Avenue South', 'Wilson Avenue South', 'Wolcott Avenue South', 'Yakima Avenue South', 'mount saint helens Place South'}

'Southeast':
{'110th Avenue Southeast', '111th Place Southeast', '114th Avenue Southeast', '115th Avenue Southeast', '116th Avenue Southeast', '118th Court Southeast', 'Coal Creek Parkway Southeast', 'Killarney Way Southeast', 'Lake Washington Boulevard Southeast'}

'Southwest':
{'10th Avenue Southwest', '10th Place Southwest', '11th Avenue Southwest', '12th Avenue Southwest', 'Vashon View Southwest', 'Walnut Avenue Southwest', 'West Marginal Way Southwest', 'Woodside Place Southwest', 'Wright Avenue Southwest'}

'St':
{'NE 110th St', 'NE 24th St', 'NE 35th St', 'SE 37th St', 'W Roy St'}

'Terrace':
{'Southwest Beach Drive Terrace'}

'Way':
{'Alaskan Way', 'Central Way', 'Denny Way', 'East Denny Way', 'East Morley Way', 'East Olive Way', 'East Yesler Way', 'Kirkland Way', 'Martin Luther King Jr Way', 'Martin Luther King Junior Way', }

'West':
{'10th Avenue West', '10th Street West', '11th Avenue West', 'Piedmont Place West', 'Thorndyke Avenue West', 'Viewmont Way West', 'West Viewmont Way West', 'Western Avenue West', 'Westview Drive West', 'Williams Avenue West'}

'driveway':
{'West queen anne driveway'}

####  Cleaning Street Names
Calling the below command changes the the actual name for the out put. As you can see, SE 37th St becomes SE 37th Street. This standardizes the data for future manipulation and querying.

{
st_types = audit('test.osm')

#pprint.pprint(dict(st_types))
for st_type, ways in st_types.iteritems():
    for name in ways:
        better_name = update_name(name, mapping)
        print name, "=>", better_name
}
Returns results like:

1. SE 37th St => SE 37th Street
2. NE 24th St => NE 24th Street
3. W Roy St => W Roy Street
4. NE 35th St => NE 35th Street
5. NE 110th St => NE 110th Street

## Preparing Data for MongoDB queries
### Background
Issues with XML and the Advantage of the MongoDB Document Model:

XML is a string - Loses fidelity when converting due to dependence on the data access lay to convert types
XML has poort handling for arrays - No native way to inform if element is scalar or enclosing array
Attributes in XML are on a different axis than nested tags - Not designed to easily carry rich structured data
Features/Capsn of XML in a column vary widely from RDBMS to RDBMS - XML treated as string has no query or update ability
Interaction with XML varies across languages - Software my interpet string data into objects
https://www.mongodb.com/blog/post/why-xml-in-rdbms-is-not-mongodb

Start Thinking in JSON: In MongoDB, data is stored as documents. These documents are stored in MongoDB in JSON (JavaScript Object Notation) format. JSON documents support embedded fields, so related data and lists of data can be stored with the document instead of an external table.

JSON is formatted as name/value pairs. In JSON documents, fieldnames and values are separated by a colon, fieldname and value pairs are separated by commas, and sets of fields are encapsulated in “curly braces” ({}).

https://docs.mongodb.com/guides/server/introduction/

#### Application
Openstreetmap exports its data in an OSM which is similiar to an XML. This data for the reasons stated above does not permit MongoDB to utilize the capabilities of its programming in queryhing the data.

In order to transform the OSM file into JSON I called process_map("Seattle.osm")

The output of this command is the file labeled "seattle.osm.json".

Simple but the code behind this is:

def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

The shape_element(element) command references the below code. The below code establishes the shape and form of a JSON documents. By iterating the the OSM/XML file tags and sub-tags are identified to create arrays that MongoDB is capable of reading and manipulating.
`def shape_element(element): node = {} if element.tag == "node" or element.tag == "way" :

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
    return None`
## Working data with MongoDB
Setting up the connection to MongoDB
Utilizing the module pymongo we import MongoClient in order to access MongoDB's server. The client is the localhost machine's port 27017. The db will be named "Project_2_Udacity". In order to ensure that the conection works the service must be running on the local host.

This is how we create the connection:

from pymongo import MongoClient
import subprocess
import json

db_name = 'Project_2_Udacity'

client = MongoClient('localhost:27017')
db = client[db_name] 

### Importing created JSON into MongoDB
The import script is called with:

print 'Executing: ' + mongoimport_cmd
subprocess.call(mongoimport_cmd.split()

This command calls the script mongoimport_cmd which imports the JSON file intot he a collection in the DB on the localhost server. The following command sets the variable Seattle_region as the actual collection in the DB.

Seattle_region = db[collection]

### Querying the database
To prove the creation of the database the command db.list_collection_names() is ran resulting in:

[u'Seattle']

#### The database objects are presented in this format
[Seattle_region.find_one())]

{u'_id': ObjectId('5f09e5bd753b53b2ba3f921a'),
 u'created': {u'changeset': u'42670803',
  u'timestamp': u'2016-10-05T22:26:36Z',
  u'uid': u'282329',
  u'user': u'compdude',
  u'version': u'12'},
 u'id': u'29445655',
 u'pos': [47.6421717, -122.3211311],
 u'type': u'node'}
The total number of node
[(Seattle_region.find({}).count())]

3418915

#### The total number of node
[(Seattle_region.count_documents({'type':'node'})]

3035615

#### The total number of node
[(Seattle_region.count_documents({'type':'node'})]
383300

#### Number of users
[len(Seattle_region.distinct('created.user'))]
2664

#### List first 50 users
[print sorted(list_users)[:50]]

u'!MRGBoss', u'-dx-', u'0x1B', u'123maps', u'1luis1', u'25or6to4', u'3vandaag', u'3xodus', u'503Greg', u'54806b45', u'>LAND', u'@eldang', u'AE35', u'ALeDonne', u'AMY-jin', u'ASayre8', u'ASwann90', u'Aaron Lidman', u'Aaron Rothschild', u'Aaron the Baron', u'Acizza', u'Adam Martin', u'Adam Schneider', u'AdamGlass', u'Adamant1', u'Adrian Lazar Adler', u'Adv_', u'AdventuringMic', u'Aerrow', u'Ahlzen', u'Ahrtaler', u'Ahwleung', u'Akihiko Lin', u'Alan', u'Alan Bragg', u'Alan Chu', u'Alan Trick', u'Aldyt', u'Aleks-Berlin', u'Aleksandar Matejevic', u'Alex Wipf', u'AlexJ', u'AlexMcCarrel', u'AlexRu', u'AlexanderF', u'AlexanderSidorenko', u'Alexey Lukin', u'AlfonsoJavier', u'AllieKD', u'Alon_Av'

#### Count posts by a specific user
[Seattle_region.count_documents({"created.user": "Adam Schneider"})]
6

#### Show posts by specific user

[for element in Seattle_region.find({"created.user": "Adam Schneider"}).sort("timestamp"):
    print element]

`{u'type': u'way', u'_id': ObjectId('5f09e5e2753b53b2ba6de509'), u'node_refs': [u'31247347', u'3431011337', u'31247332', u'3431011336', u'31247333', u'31247334', u'31247335', u'3431011335', u'31247336', u'31247337', u'31247338', u'31247339', u'3431011334', u'31247340', u'31247341', u'356548624', u'31247342', u'31247343', u'3431011338', u'31247344', u'31247345', u'31247346', u'31247348', u'31247347'], u'id': u'4848381', u'created': {u'changeset': u'56278566', u'version': u'5', u'uid': u'5403394', u'timestamp': u'2018-02-12T01:10:31Z', u'user': u'Adam Schneider'}}

{u'type': u'way', u'_id': ObjectId('5f09e5e2753b53b2ba6e1e38'), u'node_refs': [u'372774551', u'3245642873', u'372774555', u'3245642878', u'3245642881', u'372774556', u'3245642890', u'3245642893', u'3245642904', u'3245642914', u'3245642922', u'372774558', u'3245642924', u'3245642913', u'3245642903', u'3245642898', u'3245642906', u'372774559', u'3245642894', u'3245642889', u'372774560', u'3245642867', u'372774562', u'3245642760', u'3245642753', u'372774564', u'3245642737', u'3245642731', u'372774565', u'3245642727', u'3245642724', u'3245642721', u'3245642716', u'3245642714', u'372774567', u'372774569', u'3245642698', u'372774571', u'372774573', u'372774576', u'3245642674', u'372774577', u'372774578', u'3245642669', u'3245642667', u'372774579', u'3245642666', u'372774580', u'3245642659', u'372774582', u'3245642654', u'3245642652', u'3245642651', u'372774588', u'3245642653', u'372774590', u'3245642658', u'372774592', u'3245642663', u'372774593', u'3245642672', u'372774595', u'3245642676', u'3245642678', u'3245642683', u'3245642684', u'372774597', u'3245642690', u'3245642693', u'3245642694', u'3245642697', u'3245642699', u'3245642704', u'372774599', u'3245642707', u'3245642710', u'3245642713', u'3245642715', u'3245642717', u'3245642726', u'372774601', u'3245642732', u'3245642730', u'3245642733', u'3245642734', u'3245642738', u'3245642740', u'372774604', u'356549164', u'372774551'], u'id': u'33052811', u'created': {u'changeset': u'56278566', u'version': u'5', u'uid': u'5403394', u'timestamp': u'2018-02-12T01:10:33Z', u'user': u'Adam Schneider'}}

{u'type': u'way', u'_id': ObjectId('5f09e5e2753b53b2ba6e447f'), u'node_refs': [u'1026883558', u'1055821649', u'1055821661', u'1055821670', u'1055821653', u'1026883589', u'1055821644', u'1055821650', u'1055821683', u'1055821674', u'1026883615', u'1055821651', u'1055821685', u'1055821680', u'1055821673', u'1055821647', u'1026883607', u'1055821643', u'1055821656', u'1055821686', u'1026883558'], u'id': u'88394034', u'created': {u'changeset': u'56278566', u'version': u'3', u'uid': u'5403394', u'timestamp': u'2018-02-12T01:10:58Z', u'user': u'Adam Schneider'}}

{u'type': u'way', u'_id': ObjectId('5f09e5e2753b53b2ba6e4519'), u'node_refs': [u'1044379899', u'1044379903', u'1044379970', u'1044379944', u'1044379891', u'1044379923', u'1044379914', u'1044379987', u'1044379899'], u'id': u'90097467', u'created': {u'changeset': u'56278566', u'version': u'2', u'uid': u'5403394', u'timestamp': u'2018-02-12T01:10:58Z', u'user': u'Adam Schneider'}}

{u'node_refs': [u'3783654586', u'3783654599', u'4988271169', u'4988271165', u'4988271159', u'3783654571', u'3783654575', u'4988271150', u'4988271154', u'4988271161', u'4988271166', u'4988271170', u'3783654586'], u'created': {u'changeset': u'66543698', u'version': u'5', u'uid': u'5403394', u'timestamp': u'2019-01-22T16:52:36Z', u'user': u'Adam Schneider'},

u'address': {u'city': u'Kirkland', u'street': u'120th Avenue Northeast', u'housenumber': u'8629', u'postcode': u'98033'}, u'_id': ObjectId('5f09e5e6753b53b2ba71f329'), u'type': u'way', u'id': u'374983145'} {u'type': u'way', u'_id': ObjectId('5f09e5e7753b53b2ba724458'), u'node_refs': [u'4525499436', u'4525499437', u'4525499438', u'4525499439', u'4525499436'], u'id': u'456271972', u'created': {u'changeset': u'66543698', u'version': u'5', u'uid': u'5403394', u'timestamp': u'2019-01-22T16:52:40Z', u'user': u'Adam Schneider'}}

#### Top three (3) Users
top_users = Seattle_region.aggregate([
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } }, 
    { "$sort" : {"count" : -1} }, { "$limit" : 3 } 
 ] )
 list(top_users)

[{u'_id': u'Glassman', u'count': 852870},
 {u'_id': u'SeattleImport', u'count': 596130},
 {u'_id': u'Glassman_Import', u'count': 148432}]

#### Number of one time users
onetime_users = Seattle_region.aggregate( [
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } },
    { "$group" : {"_id" : "$count", "num_users": { "$sum" : 1} } },
    { "$sort" : {"_id" : 1} }, { "$limit" : 1} 
] )
list(onetime_users)

[{u'_id': 1, u'num_users': 453}]

#### Top 10 one time users
list_onetime_users = Seattle_region.aggregate([
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } }, 
    { "$sort" : {"count" : 1} }, { "$limit" : 10 } 
] )
print list(list_onetime_users)

[{u'count': 1, u'_id': u'jasonnite'},
{u'count': 1, u'_id': u'Sparks'},
{u'count': 1, u'_id': u'firm-liketheword'},
{u'count': 1, u'_id': u'Test360'},
{u'count': 1, u'_id': u'ChristyToes'},
{u'count': 1, u'_id': u'Neal Finne'},
{u'count': 1, u'_id': u'luxi_sunshine'},
{u'count': 1, u'_id': u'sburris'},
{u'count': 1, u'_id': u'Dave0'},
{u'count': 1, u'_id': u'cropmapper'}]

#### Top 3 most common places
places = Seattle_region.aggregate( [ 
    { "$match" : { "address.place" : { "$exists" : 1} } }, 
    { "$group" : { "_id" : "$address.place", "count" : { "$sum" : 1} } },  
    { "$sort" : { "count" : -1}}, {"$limit":3}
] )
list(places)

[{u'_id': u'The Wave', u'count': 4},
 {u'_id': u'Avenue One', u'count': 1},
 {u'_id': u'Seattle Heights', u'count': 1}]

#### Top 3 most common Zip Codes
top_zipcodes = Seattle_region.aggregate( [ 
    { "$match" : { "address.postcode" : { "$exists" : 1} } }, 
    { "$group" : { "_id" : "$address.postcode", "count" : { "$sum" : 1} } },  
    { "$sort" : { "count" : -1}}, {"$limit": 3}
] )
list(top_zipcodes)

[{u'_id': u'98033', u'count': 19291},
 {u'_id': u'98115', u'count': 18036},
 {u'_id': u'98103', u'count': 16905}]

## Conclusion:
After working on this project I have become more acquainted with MongoDB and associated packages on Python. Extracting the data from OpenStreetMap and forming it so that it can be read by a database like MongoDB was extremely challenging. The programmatic manipulation and translation of the data was not difficult once you have a grasp of it. Through my work on this project I developed the ability to parse, process and aggregate data.

I utilized the city of Seattle for my project. Seattle has a large technologically savvy population. I did not see as many problems with data as my peers have reported. I attribute this to the fact of the tech savvy people. Originally, I attempted to create requests within my Jupyter Notebook in order to pull the data programmatically but soon realized this option was not available to me. I ultimately utilized the Overpass API and downloaded the OSM which is actually in XML format.

I believe that OpenStreetMap is an awesome website. The use of the data could definitely be used in mapping application. The constant and consistent update of the data makes this an invaluable tool. However, the app developer has to ensure that the data is cleaned and within the correct format to a level of acceptable risk. A method to front load the insertion of clean and correct data, the app designer can utilize forms that accept only inputs that match a pre-defined format. The draw back for this is the requirement for consistent updates to the application and the potential for large gaps of data because it fails to match requirements. Creating a script that pulls data from OSM and cleans prior to upload to the application is another way. The developer would have to set a specific time for refreshing the data in order to assure availability of the application and minimize down time.

Resources: https://github.com/gauravansal/Wrangle-OpenStreetMap-Data https://github.com/FrankRuns/Udacity/tree/master/OpenStreetMap-Analysis https://github.com/gauravansal/Wrangle-OpenStreetMap-Data https://github.com/jeswingeorge/Wrangle-Openstreetmap-data https://github.com/anilsai/Wrangle-OpenStreetMap-Data-SQL-database-Udacity-project http://ipython.org/ipython-doc/stable/notebook/notebook.html#importing-py-files https://github.com/bestkao/data-wrangling-with-openstreetmap-and-mongodb https://tools.usps.com/zip-code-lookup.htm?bycitystate
