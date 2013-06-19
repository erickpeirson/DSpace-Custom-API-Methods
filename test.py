import keys
import hashlib
import urllib2
import xml.etree.ElementTree as ET
from pprint import pprint
import string
import unicodedata
import dspace

coauthorships = []
for item in items('43'):
    coauthorship = {}
    coauthorship['authors'] = []
    for field in item['metadata']['metadataentity']:
        if (field['element'] == 'creator') and (field['qualifier'] == 'uri'):
            coauthorship['authors'].append(field['value'])
        if (field['element'] == 'identifier') and (field['qualifier'] == 'uri'):
            coauthorship['uri'] = field['value']
        if (field['element'] == 'date') and (field['qualifier'] == 'None'):
            coauthorship['year'] = field['value']
    coauthorships.append(coauthorship)

authors = []
print '<?xml version="1.0"?>'
print '<graph directed="0">'
for coauthorship in coauthorships:
    for author in coauthorship['authors']:
        if author not in authors:
            authors.append(author)
            print '\t<node label="' + author + '" id="' + author + '" />'

for coauthorship in coauthorships:
    for i in range(0, len(coauthorship['authors'])):
        for x in range(i, len(coauthorship['authors'])):
            if coauthorship['authors'][i] != coauthorship['authors'][x]:
                print '\t<edge source="'+ coauthorship['authors'][i] + '" target="' + coauthorship['authors'][x] + '" start="' + coauthorship['year'][0:4] + '">'
                print '\t\t<att name="date" type="integer" value="' + coauthorship['year'][0:4] + '" />'
                print '\t\t<att name="text" type="string" value="' + coauthorship['uri'] + '" />'
                print '\t\t<att name="rel" type="string" value="coauthor" />'
                print '\t</edge>'

print '</graph>'