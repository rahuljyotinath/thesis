import xlsxwriter
from array import array
# -*- coding: utf-8 -*-
Graphpath = "metis.graph"
Clusterpath = "metis.graph.part.4"
Auth_dict_file = "author-key map.txt"
author_dict = dict()

with open(Clusterpath) as f:
    cluster = array('i')
    counter=0
    for line in f:
            eachnumber=[int(s) for s in str.split(line) if s.isdigit()]
            cluster.append(int(eachnumber[0]))
            counter+=1
#print len(cluster)
f.close()

with open(Auth_dict_file,'r') as inf:
    for line in inf:
        currentline = line.split(": ")
        currentline[1] = int(currentline[1].strip("\n"))
        author_dict.update({currentline[0]:currentline[1]})

def getAuthor(index):
    #print author_dict
    value = "hahanot found"
    for name, key in author_dict.iteritems():
        if key == index:
            value = str(name)
            #print name
    print value
    return value
#Initialize Output Excel file
workbook = xlsxwriter.Workbook('graph.xlsx')
worksheet = workbook.add_worksheet()

#Header Row Contents
worksheet.write(0,0, 'Source')
worksheet.write(0,1, 'Target')
worksheet.write(0,2, 'Weight')
worksheet.write(0,3, 'Cluster No.')
worksheet.write(0,4, 'Author Name')


with open(Graphpath) as f: #Open the File containing the Graph nodes and edges.
    rownum=0
    currentrow=1
    empty = 0
    for line in f:
        if not line.startswith("%"): #Omitting Comments
            if (rownum>=1 and line != "\n"): #Omitting the first line of the graph, contains node number and edge number
                eachnumber=[int(s) for s in str.split(line) if s.isdigit()] #Separate all the Numbers from one row and save them in a list.
                x=0 #Column Pointer in this particular row.
                while(x<=((len(eachnumber)/2)-1)): #Each edge has node number and weight, so two values for each edge.
                    y= 2 * x #Node to which the edge goes.
                    z= y+1 #Weight of that particular edge.
                    #print rownum
                    #Save the nodes of the edge and weight.
                    worksheet.write(currentrow,0, rownum)
                    worksheet.write(currentrow,1, eachnumber[y])
                    worksheet.write(currentrow,2, eachnumber[z])
                    worksheet.write(currentrow,3, cluster[rownum-1])
                    Authorname = getAuthor(rownum)
                    #if Authorname == None
                    #print Authorname
                    #print rownum
                    if "http" in Authorname:
                        worksheet.write_url(currentrow,4, Authorname.decode('utf-8'))
                    else:
                        worksheet.write(currentrow,4, Authorname.decode('utf-8'))
                    currentrow+=1
                    x+=1
            if line =="\n":
                worksheet.write(currentrow,0, rownum)
                Authorname = getAuthor(rownum)
                #if Authorname == None
                if "http" in Authorname:
                    worksheet.write_url(currentrow,4, Authorname.decode('utf-8'))
                else:
                    worksheet.write(currentrow,4, Authorname.decode('utf-8'))
                currentrow+=1 #write an empty node line with no edges because its a single node
            rownum+=1
f.close()
workbook.close()
