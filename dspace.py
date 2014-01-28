import hashlib
import urllib2
import xml.etree.ElementTree as ET
from pprint import pprint
import string
import unicodedata


class dspace:
    """
    Talk to DSpace!
    """
    
    def __init__(self, public_key, private_key, rest_path):
        """
        public_key : string
        private_key : string
        rest_path : string
            URL for RESTful API endpoint
        """
        self.public_key = public_key
        self.private_key = private_key
        self.rest_path = rest_path

    def get_digest(self, path, private_key):
        """Produces a digest based on resource path and private key."""
        
        m = hashlib.sha1('/rest' + path + private_key)
        return m.hexdigest()[0:8]
        
    def get_path(self, resource, idOnly=False):
        """Produces a full path for the desired resource."""
        return self.rest_path + resource + "?api_key=" + self.public_key + \
                "&api_digest=" + self.get_digest(resource, self.private_key) + \
                "&idOnly=" + str(idOnly).lower()

    def get_element_from_resource(self, resource, idOnly=False):
        """Returns an ElementTree root node."""
        
        request_path = self.get_path(resource, idOnly)
        response = urllib2.urlopen(request_path).read()
        return ET.fromstring(response)

    def clean_text(self, s):
        """Gets rid of garbage."""
        
        norm = unicodedata.normalize('NFKD', unicode(s))
        return  norm.encode('ascii', 'ignore').rstrip().replace('\n','')

    def dict_from_node(self, node, recursive=False):
        """
        Takes an ET node, and returns children as dict. If recursive=False, any 
        field with children will return as the number of children.
        """
        
        dict = {}
        for snode in node:
            if len(snode) > 0:
                if recursive:
                    # Will drill down until len(snode) <= 0.
                    value = self.dict_from_node(snode, True) 
                else:
                    value = len(snode)
            else:
                value = self.clean_text(snode.text)
                
            if snode.tag in dict.keys():    # If there are multiple subelements 
                                            #  with the same tag, then the value 
                                            #  of the element should be a list 
                                            #  rather than a dict.
                if type(dict[snode.tag]) is list:   # If a list has already been
                                                    #  started, just append to 
                                                    #  it.
                    dict[snode.tag].append(value)
                else:
                    dict[snode.tag] = [ dict[snode.tag], value ]
            else:
                dict[snode.tag] = value     # Default behavior.
        return dict

    def communities(self):
        """
        Retrieves all of the communities to which the user has access, and 
        returns them as a list of dictionaries.
        """
        
        root = self.get_element_from_resource('/communities.xml')
        
        C = []
        for node in root:
            C.append(self.dict_from_node(node, True))
        return C

    def community(self, id):
        """Retrieves details for a specific community, by id."""
        
        root = self.get_element_from_resource('/communities/'+str(id)+'.xml')
        return self.dict_from_node(root, True)

    def collection_ids(self, c_id):
        """Returns a list of collection IDs for a given community."""
        
        return [ c['id'] for c in \
                  self.community(c_id)['collections']['collectionentityid'] ] 

    def collection(self, id):
        """Retrieves details for a specific collection, by id."""
        
        root = self.get_element_from_resource('/collections/'+str(id)+'.xml')
        return self.dict_from_node(root, True)

    def items(self, collection_id):
        return [ i for i in \
                  self.collection(collection_id)['items']['itementity'] ]
    
    def item(self, id):
        root = self.get_element_from_resource('/items/' + str(id) + '.xml')
        return self.dict_from_node(root, True)

    def item_metadata(self, id):
        """
        Returs metadata for an item as a simple dictionary, with dc fields
        as keys.
        """
        
        i = self.item(id)
        return { me['element'] + '.' + me['qualifier']:me['value'] for me \
                  in i['metadata']['metadataentity'] }

    def collections(self):
        """Retrieves all of the collections."""
        
        root = self.get_element_from_resource('/collections.xml')
        collections = []
        for node in root:
            collections.append(self.dict_from_node(node))

        return collections
    
    def bitstream_ids(self, id):
        """
        Returns a list of bitstream ids for an item.
        """
        
        i = self.item(id)
        if type(i['bitstreams']['bitstreamentity']) is dict:    # One bitstream.
            return [ i['bitstreams']['bitstreamentity']['id'] ]
        else:
            return [ be['id'] for be in i['bitstreams']['bitstreamentity'] ]
    
    def bitstream(self, id):
        """
        Returns information about a bitstream.
        """
        
        root = self.get_element_from_resource('/bitstream/' + str(id) + '.xml')
        bitstreamentities = root.findall('.//bitstreamentity')
        for b in bitstreamentities:
            if self.dict_from_node(b)['id'] == str(id):
                return self.dict_from_node(b, True)
    
    def get_bitstream(self, id, save_path=None):
        """
        Downloads a bitstream and handles it.
        """
        
        if save_path is None:
            rpath = self.get_path('/bitstream/' + str(id))
            r = urllib2.urlopen(rpath)
            return r.read()