import xml.etree.ElementTree as ET
xmldoc = ET.parse("./files/plants.xml")
root = xmldoc.getroot()

# <editor-fold desc="Solution with iter">
# i = 1
# for plant in root.iter('plant'):
#    print('Plant', i, ':', plant[0].text, '('+plant[1].text.capitalize()+')')
#    i += 1
# </editor-fold>

# <editor-fold desc="1b - change for sunlight">
print()

i = 1
for plant in root.iter('plant'):
    if plant[3].text == 'SUN':
        print('Plant', i, ':', plant[0].text, '('+plant[1].text.capitalize()+')')
        i += 1
# </editor-fold>

# <editor-fold desc="Solution with findall">
print()

counter = 1
for plant in root.findall('plant'):
    common = plant.find('common').text
    botanical = plant.find('botanical').text.capitalize()

    print('Plant {} : {} {}'.format(counter, common, botanical))
    counter += 1
# </editor-fold>
