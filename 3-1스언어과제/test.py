from xml.dom.minidom import *
xmlsrc = """<item>
<name>test</name>
</item>
"""
doc = parseString(xmlsrc)

names = doc.getElementsByTagName("name")
