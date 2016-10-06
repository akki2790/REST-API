#code to retrive data from a URL and copy it into a file

from urllib import urlopen

width=raw_input("Enter the width of the image you want to copy: ")
height=raw_input("Enter the height of the image you want to copy: ")

url='https://www.rsv4factory.com/' + width + '/' + height
rsv4=urlopen(url).read()

with open('rsv4_copy.jpg', 'w') as rsv4_copy:
    rsv4_copy.write(rsv4)
