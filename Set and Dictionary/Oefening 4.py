import xml.etree.ElementTree as ET
txtfile = set()
xmlfile = set()

# <editor-fold desc="Text file">
with open('./files/games.txt', encoding='utf8') as file:
    line = file.readline().rstrip()
    while line:
        record = line.split(',')
        txtfile.add(record[-5].strip("'"))  # Missing column in txt file for 'type' search
        line = file.readline().rstrip()
# </editor-fold>

# <editor-fold desc="XML file">
xmlDoc = ET.parse('./files/games.xml')
root = xmlDoc.getroot()
for game in root.findall('game'):
    xmlfile.add(game[1].text)  # Hardcoded for 'type' field
# </editor-fold>

print('In the txt-file: {}'.format(len(txtfile)))
print('In the XML-file: {}'.format(len(xmlfile)))

print('The types that occur in both files: {}'.format(txtfile & xmlfile))
print('The types that only appear in the txt-file: {}'.format(txtfile - xmlfile))
print('The types that only appear in the xml-file: {}'.format(xmlfile - txtfile))
