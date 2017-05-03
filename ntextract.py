# -*- coding: utf-8 -*-
from rdflib import Graph, plugin, URIRef, Literal, BNode, Namespace
from rdflib.serializer import Serializer
import glob, time, os, logging,pprint
from rdflib.namespace import XSD, RDF
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

#Path for the folder containing subfolders of Json Files.
inputpath = os.getcwd() + "/nt-files/"

#Desired Path for the converted nt files.
#outputpath="resulttest.nt"
x = glob.glob("%s*.nt" %inputpath)

counter = 0
f= open('abc.txt', "w")

for current_file in x:
    filename= os.path.basename("%s" %current_file)
    counter+=1

    g= Graph()

    print ("File Number {} processing file : {}" .format(counter,filename))
    f.write("File Number {} processing file : {}" .format(counter,filename))
    f.flush()
    g.parse(current_file, format="nt")

    qres = g.query(
        """SELECT ?a ?b ?c
        WHERE {
            ?a ?b ?c .
            FILTER (regex( str(?a),  "http://dblp.org/rec/conf/esws/")).
            }""",
            initNs=dict(
            amco=Namespace("http://dblp.org/rec/journals/"),
            rdfs=Namespace("http://dblp.org/rdf/schema-2017-04-18#")))

    if (len(qres.result) != 0):
            print ("\nFound the following data in file named {} : \n " .format(filename))
            f.write("\nFound the following data in file named {} : \n " .format(filename))
    else:
        print ("\tFinished Parsing File %s. No Relevant information found. \n" %filename)
        f.write ("\t Finished Parsing File %s. No Relevant information found. \n" %filename)

    for row in qres.result:
        print(row[0].decode('unicode-escape').encode('utf-8'))
        print(row[1].decode('unicode-escape').encode('utf-8'))
        print(row[2].decode('unicode-escape').encode('utf-8'))

        f.write("%s \t" %row[0].decode('unicode-escape').encode('utf-8'))
        f.write("%s \t" %row[1].decode('unicode-escape').encode('utf-8'))
        f.write("%s \n" %row[2].decode('unicode-escape').encode('utf-8'))

f.close()
