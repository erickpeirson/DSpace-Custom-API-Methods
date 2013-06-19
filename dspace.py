import keys
import hashlib
import urllib2
import xml.etree.ElementTree as ET
from pprint import pprint
import string
import unicodedata

rest_path = "https://import.hps.ubio.org/rest"

def get_digest(path, private_key):
    """Produces a digest based on resource path and private key."""
    
    m = hashlib.sha1('/rest' + path + private_key)
    return m.hexdigest()[0:8]
    
def get_path(resource, idOnly=False):
    """Produces a full path for the desired resource."""
    return rest_path + resource + "?api_key=" + keys.public_key + "&api_digest=" + get_digest(resource, keys.private_key) + "&idOnly=" + str(idOnly).lower()

def get_element_from_resource(resource, idOnly=False):
    """Returns an ElementTree root node."""
    
    request_path = get_path(resource, idOnly)
    response = urllib2.urlopen(request_path).read()
    return ET.fromstring(response)

def clean_text(s):
    """Gets rid of garbage."""
    
    return unicodedata.normalize('NFKD', unicode(s)).encode('ascii', 'ignore').rstrip().replace('\n','')

def dict_from_node(node, recursive=False):
    """Takes an ET node, and returns children as dict. If recursive=False, any field with children will return as the number of children."""
    
    dict = {}
    for snode in node:
        if len(snode) > 0:
            if recursive:
                value = dict_from_node(snode, True) # Will drill down until len(snode) <= 0.
            else:
                value = len(snode)
        else:
            value = clean_text(snode.text)
            
        if snode.tag in dict.keys():    # If there are multiple subelements with the same tag, then the value of the element should be a list rather than a dict.
            if type(dict[snode.tag]) is list:   # If a list has already been started, just append to it.
                dict[snode.tag].append(value)
            else:
                dict[snode.tag] = [ dict[snode.tag], value ]
        else:
            dict[snode.tag] = value     # Default behavior.
    return dict

def communities():
    """Retrieves all of the communities to which the user has access, and returns them as a list of dictionaries."""
    
    root = get_element_from_resource('/communities.xml')
    
    communities = []
    for node in root:
        communities.append(dict_from_node(node, True))
    return communities

def community(id):
    """Retrieves details for a specific community, by id."""
    
    root = get_element_from_resource('/communities/'+id+'.xml')
    return dict_from_node(root, True)

def collection_ids(community_id):
    """Returns a list of collection IDs for a given community."""
    
    return [ c['id'] for c in community(community_id)['collections']['collectionentityid'] ] 

def collection(id):
    """Retrieves details for a specific collection, by id."""
    
    root = get_element_from_resource('/collections/'+id+'.xml')
    return dict_from_node(root, True)

def items(collection_id):
    return [ i for i in collection(collection_id)['items']['itementity'] ]

def all_collections():
    """Retrieves all of the collections."""
    
    root = get_element_from_resource('/collections.xml')
    collections = []
    for node in root:
        collections.append(dict_from_node(node))

    return collections