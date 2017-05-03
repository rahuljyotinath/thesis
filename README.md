# thesis
My Master Thesis (Using METIS for Graph Partitioning)
Python script number 1 filters the DBLP data dump and extracts all the relevant triples and outputs them in a separate NT file. ISWC.NT file uploaded here is the ISWC data extract from the DBLP Data Dump. 

Python Script 2 converts the NT file obtained from Script 1 and processes the information into an Excel spreadsheet with each row corresponding to a particular subject of the NT file, which is a paper in this case.

Python Script 3 is incomplete and it is supposed to take as input the Excel file and produces 1. An Author-Key Mapping. 2. Metis Graph File with edges between co-authors using indexes from the Mapping file created in the first part. 
First Part here is done. Second part is not yet complete. 
