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
    
    m = hashlib.sha1(path + private_key)
    return m.hexdigest()[0:8]
    
def get_path(resource):
    """Produces a full path for the desired resource."""
    
    return "https://import.hps.ubio.org/rest"+ resource + "?email=" + keys.email + "&password=" + keys.password
#    return rest_path + resource + "?api_key=" + keys.public_key + "&api_digest=" + get_digest(resource, keys.private_key)

def get_element_from_resource(resource):
    """Returns an ElementTree root node."""
    
    request_path = get_path(resource)
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
                dict[snode.tag] = [ clean_text(cnode[0].text) for cnode in snode ] 
            else:
                dict[snode.tag] = len(snode)
        else:
            dict[snode.tag] = clean_text(snode.text)
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
    return dict_from_node(root)

def collection(id):
    """Retrieves details for a specific collection, by id."""
    
    root = get_element_from_resource('/collections/'+id+'.xml')
    return dict_from_node(root, True)

def all_collections():
    """Retrieves all of the collections."""
    
    root = get_element_from_resource('/collections.xml')
    collections = []
    for node in root:
        collections.append(dict_from_node(node))

    return collections


pprint(collection('38'))