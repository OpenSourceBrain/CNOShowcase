'''
API to OSB tests using restkit...
'''

from restkit import Resource
res = Resource('http://www.opensourcebrain.org')

import json

projects = res.get('/projects.json', limit=1000)


jp = json.loads(projects.body_string())


def printCustomField(project, cfName, info):
    for cf in project["custom_fields"]:
        if cf['name'] == cfName and cf.has_key('value'):  
            if cfName == 'CNO Ids':
                info += cf['value']+"  "
            else:
                info += ""
    return info

info = ""

for project in jp["projects"]:

    isProj = False
    hasCNOids = False
    for cf in project["custom_fields"]:
        if cf['name'] == 'Category' and cf.has_key('value') and cf['value']=='Project':
            isProj = True
        if cf['name'] == 'CNO Ids' and cf.has_key('value') and len(cf['value'])>0:
            hasCNOids = True
    
    if isProj:

        url = "http://opensourcebrain.org/projects/%s"%project["identifier"]
        info += "\n%s "%url
        for i in range(100-len(url)):
            info += " "
        
        if hasCNOids:
            info = printCustomField(project, 'CNO Ids', info)
        else:
            info += ""

print info

fn = "CNO_IDs_in_OSB.md"

info_file = open(fn, 'w')
info_file.write(info)
