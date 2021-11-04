import pycali,rdflib
ODLRTestData='''
[{
  "@type": "Agreement",
  "uid": "mosaico.database.windows.net/Test:policy:1",
  "permission": [{
      "target": "mosaico.database.windows.net/Test:STUDENTI",
      "assignee": "mosaico.database.windows.net/Test:user:Tester",
      "action": "read"
  }]
  },
  {
  "@type": "Agreement",
  "uid": "mosaico.database.windows.net/Test:policy:2",
  "permission": [
    {
      "target": "mosaico.database.windows.net/Test:DOCENTI:NOME",
      "assignee": "mosaico.database.windows.net/Test:user:Tester",
      "action": "read"
    }
  ]
}]
'''
from pycali.vocabulary import ODRLVocabulary
from rdflib.namespace import RDF,FOAF

odrl = ODRLVocabulary()
# access the list of actions
from rdflib import Graph
from pycali.restrictiveness_lattice_of_status import RestrictivenessLatticeOfStatus
from pycali.examples.restrictiveness_lattice_of_status.DL1 import dl1_rdf

# Load the LS in the examples 
# Turtle format (ttl) contains tuple infos
graph= Graph().parse(data=ODLRTestData,format='json-ld')
for d1,d2,d3 in graph.triples((None, odlr.type, ODRL.uid)):
    print(d3)
# print(graph.serialize(format="turtle"))
    