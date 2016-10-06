7#code to parse xml(eXtensible Markup Language) file


#<pets>
#   <name>Tony</name>
#   <species>Dog</species>   
#</pets>

from xml.dom import minidom
f=open('file.xml', 'r')
pets=minidom.parseString(f.read())
f.close()

names=pets.getElementsByTagName('name')
for name in names:
    print name.firstChild.nameValue


#O/P: Tony
    
