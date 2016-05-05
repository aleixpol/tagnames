import sys
import subprocess

names = sys.stdin.read().split('\n')

page = 5
blank = [ "____________________", "", "____________________" ]

def replaceName(ff, number, val):
    nombre = ""
    if val[1] == "":
        nombre = val[0]
    else:
        nombre = "%s (%s)" % (val[0], val[1])
    ff=ff.replace('nombre'+number, nombre, 1)
    ff=ff.replace('organizacion'+number, val[2], 1)
    return ff

for i in range(0,len(names)/page+1):
    idx = i * page

    f = open('tagnames2016-martin.svg')
    ff = f.read()
    if idx<len(names):
        ff = replaceName(ff, "1", names[idx].split('|'))
    else:
        ff = replaceName(ff, "1", blank)
    if idx+1<len(names) and names[idx+1] != "":
        ff = replaceName(ff, "2", names[idx+1].split('|'))
    else:
        ff = replaceName(ff, "2", blank)
    if idx+2<len(names) and names[idx+2] != "":
        ff = replaceName(ff, "3", names[idx+2].split('|'))
    else:
        ff = replaceName(ff, "3", blank)
    if idx+3<len(names) and names[idx+3] != "":
        ff = replaceName(ff, "4", names[idx+3].split('|'))
    else:
        ff = replaceName(ff, "4", blank)
    if idx+4<len(names) and names[idx+4] != "":
        ff = replaceName(ff, "5", names[idx+4].split('|'))
    else:
        ff = replaceName(ff, "5", blank)
    print '--'

    outputpath = 'akaes/tags%d.svg' % i
    towrite=open(outputpath, 'w')
    towrite.write(ff)
    towrite.close()

    subprocess.call(["inkscape", outputpath, "--export-pdf=akaes/tags%d.pdf" % i])

