from rdflib import Graph, plugin, URIRef, Literal, BNode, Namespace
from rdflib.serializer import Serializer
import glob, time, os, logging,pprint
from rdflib.namespace import XSD, RDF
import sys,re

reload(sys)
sys.setdefaultencoding('UTF-8')


current_file = "ISWC-2015.nt" #Input NT file


outputFile = "titles.txt"

#Execution starts from here:-
f = open(outputFile, "w")  #open input NT file.

g= Graph() #Initialize a Graph
g.parse(current_file, format="nt") #Parse the Input NT file
#SPARQL query to get all triples related to ISWC. They have the same subject prefix.
qres = g.query(
               """SELECT ?b
                   WHERE {
                   ?a <http://dblp.org/rdf/schema-2017-04-18#title> ?b .
                   FILTER (regex( str(?a),  "http://dblp.org/rec/conf/semweb/")).
                   }
                   order by asc(str(?a))
                   """,
               initNs=dict(
                           amco=Namespace("http://dblp.org/rec/journals/"),
                           rdfs=Namespace("http://dblp.org/rdf/schema-2017-04-18#")))

counter = 0
for row in qres.result:
    counter+=1
    print row[0]
    f.write("%s\n" %(row[0].decode('unicode-escape').encode('utf-8')))
#f.write(backlash one character)
f.close()
