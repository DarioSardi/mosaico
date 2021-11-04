import pycali,rdflib
from pyld import jsonld
import json,urllib

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



jsonld.set_document_loader(jsonld.requests_document_loader(timeout=500))
compacted = jsonld.compact(multipleTarget, 'http://www.w3.org/ns/odrl.jsonld')
print(json.dumps(compacted["permission"][1], indent=2))
