import xlsxwriter
from array import array

Graphpath = "metis.graph"
Clusterpath = "metis.graph.part.10"

with open(Clusterpath) as f:
    cluster = array('i')
    counter=0
    for line in f:
            eachnumber=[int(s) for s in str.split(line) if s.isdigit()]
            cluster.append(eachnumber[0])
            print(cluster[counter])
            counter+=1
f.close()


#Initialize Output Excel file
workbook = xlsxwriter.Workbook('graph.xlsx')
worksheet = workbook.add_worksheet()

#Header Row Contents
worksheet.write(0,0, 'Source')
worksheet.write(0,1, 'Target')
worksheet.write(0,2, 'Weight')
worksheet.write(0,3, 'Interaction Type')
worksheet.write(0,4, 'directed')
worksheet.write(0,5, 'Cluster No.')

with open(Graphpath) as f: #Open the File containing the Graph nodes and edges.

    rownum=0
    currentrow=1

    for line in f:
        if not line.startswith("%"): #Omitting Comments
            if (rownum>=1): #Omitting the first line of the graph, contains node number and edge number
                eachnumber=[int(s) for s in str.split(line) if s.isdigit()] #Separate all the Numbers from one row and save them in a list.
                x=0 #Column Pointer in this particular row.
                while(x<=((len(eachnumber)/2)-1)): #Each edge has node number and weight, so two values for each edge.
                    y= 2 * x #Node to which the edge goes.
                    z= y+1 #Weight of that particular edge.

                    #Save the nodes of the edge and weight.
                    worksheet.write(currentrow,0, rownum)
                    worksheet.write(currentrow,1, eachnumber[y])
                    worksheet.write(currentrow,2, eachnumber[z])
                    worksheet.write(currentrow,3, "pp")
                    worksheet.write(currentrow,4, "FALSE")
                    worksheet.write(currentrow,5, cluster[rownum-1])
                    currentrow+=1
                    x+=1
            rownum+=1
            
f.close()
workbook.close()
