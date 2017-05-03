from openpyxl import Workbook
from array import array
from openpyxl.utils import coordinate_from_string, column_index_from_string
from openpyxl.utils import get_column_letter
import urllib2,re
from bs4 import BeautifulSoup
import urllib
from urllib2 import Request, urlopen, URLError
import openpyxl

def getvalue(r):
    row=r[2]
    col = 3
    if (row.value!=0):
        return 1
    return

    
def getName(link):
    response = urllib2.Request(link)
    try:
        value=urllib2.urlopen(response)
    except URLError, e:
        print e.reason
        return link
    #response = urllib2.urlopen(link)
    html = value.read()
    soup = BeautifulSoup(html, "lxml")
    return ((soup.title.contents[0]).encode('utf-8')).split("dblp: ")[1]

def edgesmetis(edges):
    #currentedge = []
    #alledges=[]
    edgelength= len(edges)
    loopedge=0
    for val in edges:
        for val2 in edges:
            if (val==val2):
                continue
            if metis_dict[]
            edge_count+=1
            metis_dict[val] = [val2].append
        loopedge+=1


wb = openpyxl.load_workbook(XlsxPath)
sh = wb.get_active_sheet()
f = open("author-key map.txt", 'w+')
g = open(GraphFile, 'w+')
metis_dict={}
counter=0
author_count=0
edge_count=0
author_dict = {}
for r in sh.rows:
    counter+=1
    if (counter==1):
        continue
    #print counter
    num_author= int(r[2].value)
    if (num_author !=0):
        #print "number of authors is %d" %num_author
        edges=[]
        for num in range(1,num_author+1):
            #print "author number %d" %num
            auth_link = r[5+num].value
            if auth_link not in author_dict:
                author_count+=1
                author_dict[auth_link] = author_count
            key=author_dict.get(auth_link, 'No available data')
            edges.append(key)
        print edges
        edgesmetis(edges)

for key, value in sorted(author_dict.iteritems(), key=lambda (k,v): (v,k)):
    f.write( "%s: %s\n" % (key, value))

wb.save("abc.xlsx")
