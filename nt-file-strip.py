# -*- coding: utf-8 -*-
from rdflib import Graph, plugin, URIRef, Literal, BNode, Namespace
from rdflib.serializer import Serializer
import glob, time, os, logging,pprint
from rdflib.namespace import XSD, RDF
import sys,io, re
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2, logging

ntfile = "input.nt"
savefile = "output.nt"

g = open(savefile, 'w')
with open(ntfile) as f:
    for line in f:
        eachnumber= re.findall("\<(.*?)\>", line)   #Get the subject, predicate and object stored in eachnumber
        print(("<" + eachnumber[0] + ">" + " " + "<" + eachnumber[1] + ">" + " " + "<" + eachnumber[2] + ">" + " ."))
        g.write("<" + eachnumber[0] + ">" + " " + "<" + eachnumber[1] + ">" + " " + "<" + eachnumber[2] + ">" + " ." + "\n")


