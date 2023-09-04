fileName = input("Enter file name: ")
folderName = input("What should the bookmark folder name be? ")

myArray = []
firstPart = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL>
    <DT><H3>%s</H3></DT>
    <DL>
""" % (folderName)
lastPart = """
    </DL>
</DL>
"""

if not fileName.endswith(".txt"):
    fileName = fileName + ".txt"

# Read the lines into myArray
with open(fileName, "r", encoding="utf8") as file:
    for line in file.readlines():
        myArray.append(line)

# Write the lines that start with http
with open(fileName.rstrip("txt") + 'bookmark.html', 'w', encoding="utf8") as updatedFile:
    updatedFile.write(firstPart)

    for element in myArray:
        if element.startswith('http'):
            element = element.strip()
            updatedFile.write('        <DT><A HREF="%s">%s</A></DT>\n' % (element, element))

    updatedFile.write(lastPart)
