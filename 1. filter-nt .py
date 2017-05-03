# -*- coding: utf-8 -*-
from rdflib import Graph, plugin, URIRef, Literal, BNode, Namespace
from rdflib.serializer import Serializer
import glob, time, os, logging,pprint
from rdflib.namespace import XSD, RDF
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

current_file = os.getcwd() + "/nt-files/bp.nt" #Path for the imput file containing triples about ISWC.
outputpath="ISWC.nt" #Output file with triples related to only ISWC Conferences

f= open(outputpath, "w")

g= Graph() #Initialize a Graph
g.parse(current_file, format="nt") #Parse the Input NT file
#SPARQL query to get all triples related to ISWC. They have the same subject prefix.
qres = g.query(
    """SELECT ?a ?b ?c
    WHERE {
        ?a ?b ?c .
        FILTER (regex( str(?a),  "http://dblp.org/rec/conf/semweb/")).
        }
        order by asc(str(?a))
        """,
        initNs=dict(
        amco=Namespace("http://dblp.org/rec/journals/"),
        rdfs=Namespace("http://dblp.org/rdf/schema-2017-04-18#")))

for row in qres.result:
        f.write("<%s> \t" %row[0].decode('unicode-escape').encode('utf-8')) #Write Subject to file
        f.write("<%s> \t" %row[1].decode('unicode-escape').encode('utf-8')) #write predicate
        f.write("<%s>. \n" %row[2].decode('unicode-escape').encode('utf-8')) #write object
f.close()
