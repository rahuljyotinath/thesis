from array import array
import urllib2,re
from bs4 import BeautifulSoup
import urllib
from urllib2 import Request, urlopen, URLError
import time

Auth_dict_file = "author-key map.txt"
author_dict_link = dict()
author_dict_name = dict()

def getName(link):
    response = urllib2.Request(link)
    try:
        value=urllib2.urlopen(response)
    except URLError, e:
        print e.reason
        if e.reason == "Not Found":
            return link
        if e.reason == "Too Many Requests":
            time.sleep(500) #wait for 10 seconds
            getName(link)
        return link
    html = value.read()
    soup = BeautifulSoup(html, "lxml")
    name = ((soup.title.contents[0]).encode('utf-8')).split("dblp: ")[1]
    print name
    return name

########################################################################################


with open(Auth_dict_file,'r') as inf:
    for line in inf:
        currentline = line.split(": ") # Separate the keys and the values
        #currentline[1] = currentline[1].strip("\n") #Key which is 2nd part of each line
        currentline[1] = int(re.search(r'\d+', currentline[1]).group())
        author_dict_link.update({currentline[0]:currentline[1]}) #All the links added to dictionary

for link, key in author_dict_link.iteritems():
    #print link
    if "http" in link:
        print link
        author_dict_name.update({getName(link):key})
    else:
        author_dict_name.update({link:key})
with open(Auth_dict_file, 'w') as f:
    for key, value in sorted(author_dict_name.iteritems(), key=lambda (k,v): (v,k)):
        f.write("%s: %s\n" % (key, value))
        print ("%s: %s\n" % (key, value))
