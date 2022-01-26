import pycali,rdflib
from pyld import jsonld
import json,urllib,os

singleData={
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "@type": "Set",
    "uid": "http://example.com/policy:1010",
    "permission": [{
        "target": "http://example.com/asset:9898.movie",
        "action": "use"
    }]
}

multipleTarget={
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "@type": "Policy",
    "uid": "http://example.com/policy:8888",
    "profile": "http://example.com/odrl:profile:20",
    "permission": [{
        "target": "http://example.com/music/1999.mp3",
        "assignee": "http://example.com/people/billie",
        "assigner": "http://example.com/org/sony-music",
        "action": "play"
    },
    {
        "target": "http://example.com/music/1999.mp3",
        "assignee": "http://example.com/people/joe",
        "assigner": "http://example.com/org/sony-music",
        "action": "stream"
    },
	{
        "target": "http://example.com/music/PurpleRain.mp3",
        "assignee": "http://example.com/people/danny",
        "assigner": "http://example.com/org/sony-music",
        "action": "play"
    },
	{
        "target": "http://example.com/music/PurpleRain.mp3",
        "assignee": "http://example.com/people/alex",
        "assigner": "http://example.com/org/sony-music",
        "action": "stream"
    }]
}



# jsonld.set_document_loader(jsonld.requests_document_loader(timeout=500))
# compacted = jsonld.compact(multipleTarget, 'http://www.w3.org/ns/odrl.jsonld')
# print(json.dumps(compacted["permission"][1], indent=2))

permissionList = []
odlrFolder = os.getcwd() + "/odlr/"
'''
-aggiungere magari un filtro sulla action permessa
-albero inizialmente senza permessi
'''
def permissionSearcher(name, dbTree):
    for filename in os.listdir(odlrFolder):
        if filename.endswith(".odlr"):
            with open(odlrFolder+filename) as file:
                raw=file.read()
                data=json.loads(raw)
                compact = jsonld.compact(data,'http://www.w3.org/ns/odrl.jsonld')
                for perm in compact["permission"]:
                    if(perm["assignee"]==name):
                        print(perm["target"]," : ",perm["action"])
                        #add to tree the target 
          
            
permissionSearcher("http://example.com/people/billie",None)


