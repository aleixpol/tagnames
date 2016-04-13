import sys
import subprocess
import math

f = open('tagnames2014-data')
info = f.read().split('\n')
names = {}
for i in range(0, len(info)):
	if info[i] == "":
		continue
	v = info[i].split('|')
	names[i] = { "nombre": v[0], "organizacion": v[2] }
	if v[2]=="" and v[1]!="":
		names[i]["organizacion"] = "nick: "+v[1]
	#print("hola", v, names[i]["organizacion"])

f = open('tagnames2014-blank5.svg')
filecontents = f.read()

def replaceStrings(ff, name, names, idx, count):
	for i in range(0, count+1):
		if idx+i<len(names):
			ff=ff.replace(name+str(i), names[idx+i][name],1)
		else:
			ff=ff.replace(name+str(i), "____________________",1)
	return ff

outputfiles = []
for i in range(0, math.floor(len(names)/5+1)):
	idx=i*5
	ff=filecontents
	
	ff = replaceStrings(ff, "nombre", names, idx, 5)
	ff = replaceStrings(ff, "organizacion", names, idx, 5)
	
	print('--')
	
	outputpath = 'akaes/tags%d.svg' % i
	towrite=open(outputpath, 'w')
	towrite.write(ff)
	towrite.close()
	
	outputfiles.append("akaes/tags%d.pdf" % i)
	subprocess.call(["inkscape", outputpath, "--export-pdf=akaes/tags%d.pdf" % i])


subprocess.call(["gs", "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite", "-sOutputFile=akaes/finished.pdf"] + outputfiles)