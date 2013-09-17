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
                info += "\n    CNO Ids:                       %s"%cf['value']
            else:
                info += "\n     "+cfName+":             "+ cf['value']
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
        info += "\n\n--------   Project: "+ project["name"] + "\n"

        if hasCNOids:
            info += "\n    OSB link:                      http://opensourcebrain.org/projects/"+project["identifier"]
            info = printCustomField(project, 'CNO Ids', info)
        else:
            info += "\n    No CNO Ids for model"

print info

fn = "CNO_IDs_in_OSB.txt"

info_file = open(fn, 'w')
info_file.write(info)
