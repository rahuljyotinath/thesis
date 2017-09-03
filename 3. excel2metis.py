from openpyxl import Workbook
from array import array
from openpyxl.utils import coordinate_from_string, column_index_from_string
from openpyxl.utils import get_column_letter
import urllib2,re
from bs4 import BeautifulSoup
import urllib
from urllib2 import Request, urlopen, URLError
import openpyxl

XlsxPath = "metis.xlsx"   #input file containing data to be processed
MetisFile= "metis.graph"    #output file for metis
AuthorkeyFile = "author-key map.txt"    #reference output file for indexing authors

edge_count=0

def getvalue(r):
    row=r[2]
    col = 3
    if (row.value!=0):
        return 1
    return

def edgesmetis(edges):
    global edge_count
    global metis_dict
    for val in edges:
        for val2 in edges:
            if (val==val2):
                continue
            else:
                metis_dict[val-1][val2-1] += 1   #the weight increased of the particular edge
                if metis_dict[val-1][val2-1] ==1: #we increment the edge counter only when the edge is a new edge
                    edge_count+=1
    return

#################******~~~~Processing starts here~~~~*******#######################

wb = openpyxl.load_workbook(XlsxPath)
sh = wb.get_active_sheet()
f = open(AuthorkeyFile, 'w+')
g = open(MetisFile, 'w+')
counter=0   #row pointer of the input file
author_count=0  #total number of authors

author_dict = {}    #list of all the authors
for r in sh.rows:   #loop over each line of input file
    counter+=1      #point to the next line of the input file
    if (counter==1):    #First row is header row, so skip.
        continue
    num_author= int(r[2].value)
    if (num_author !=0):
        for num in range(1,num_author+1):
            auth_link = r[5+num].value.strip("<").strip(">")
            if auth_link not in author_dict:
                author_count+=1
                author_dict[auth_link] = author_count

for key, value in sorted(author_dict.iteritems(), key=lambda (k,v): (v,k)):
    f.write("%s: %s\n" % (key, value))

metis_dict=[[0 for x in range(author_count)] for y in range(author_count)]
counter=0
for r in sh.rows:
    counter+=1
    if (counter==1):
        continue
    num_author= int(r[2].value)
    if (num_author !=0):
        edges=[]
        for num in range(1,num_author+1):
            auth_link = r[5+num].value.strip("<").strip(">")
            key=author_dict.get(auth_link, 'No available data')
            edges.append(key)
        edgesmetis(edges)
edge_count = edge_count/2
#print metis_dict
g.write("%s\t%s\t1" %(author_count, edge_count) )
for row in range(0,author_count):
    edgesfornodes = ""
    g.write("\n")
    for col in range(0, author_count):
        if (metis_dict[row][col] !=0):
            if edgesfornodes == "" :
                edgesfornodes = str(col+1) +" "+ str(metis_dict[row][col])
            else:
                edgesfornodes = edgesfornodes + "\t" +str(col+1) +" "+ str(metis_dict[row][col])
    if (edgesfornodes != ""):
        g.write("%s" %edgesfornodes)
g.write("\n")
wb.close()
