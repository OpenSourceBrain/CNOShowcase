'''
API to OSB tests using restkit...
'''

from restkit import Resource
res = Resource('http://www.opensourcebrain.org')

import json

projects = res.get('/projects.json', limit=1000)


jp = json.loads(projects.body_string())


def printCustomField(project, cfName):
    for cf in project["custom_fields"]:
        if cf['name'] == cfName and cf.has_key('value'):  
            if cfName == 'CNO Ids':
                print "    CNO Ids:                       %s"%cf['value']
            else:
                print "     "+cfName+":             "+ cf['value']

for project in jp["projects"]:

    isProj = False
    hasCNOids = False
    for cf in project["custom_fields"]:
        if cf['name'] == 'Category' and cf.has_key('value') and cf['value']=='Project':
            isProj = True
        if cf['name'] == 'CNO Ids' and cf.has_key('value') and len(cf['value'])>0:
            hasCNOids = True
    
    if isProj:
        print "\n--------   Project: "+ project["name"] + "\n"

        if hasCNOids:
            print "    OSB link:                      http://opensourcebrain.org/projects/"+project["identifier"]
            printCustomField(project, 'CNO Ids')
        else:
            print "    No CNO Ids for model"

        
