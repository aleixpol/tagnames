import sys
import subprocess

names = sys.stdin.read().split('\n')

f = open('tagnames2012.svg')
filecontents = f.read()

for i in range(0,len(names)/4+1):
	idx=i*4
	ff=filecontents
	
	ff=ff.replace('cucucu1', names[idx],1)
	if idx+1<len(names):
		ff=ff.replace('cucucu2', names[idx+1],1)
	else:
		ff=ff.replace('cucucu2', "____________________",1)
	if idx+2<len(names):
		ff=ff.replace('cucucu3', names[idx+2],1)
	else:
		ff=ff.replace('cucucu3', "____________________",1)
	if idx+3<len(names):
		ff=ff.replace('cucucu4', names[idx+3],1)
	else:
		ff=ff.replace('cucucu4', "____________________",1)
	print '--'
	
	outputpath = 'akaes/tags%d.svg' % i
	towrite=open(outputpath, 'w')
	towrite.write(ff)
	towrite.close()
	
	subprocess.call(["inkscape", outputpath, "--export-pdf=akaes/tags%d.pdf" % i])

