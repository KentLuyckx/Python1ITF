import xml.etree.ElementTree as ET
xmldoc = ET.parse("./files/drugs.xml")
root = xmldoc.getroot()

for leaflet in root.iter('leaflet'):  # Search for child tag "Leaflet" under rood
    forms = leaflet.find('pharmaceutical_forms')  # Search for tag "forms" under tag "leaflet"
    leaflet.remove(forms)  # Remove all children of tag "forms" and the tag itself
    name = leaflet.find('name')  # Search for tag "name" in tag "leaflet"
    name_upper = name.text.upper()  # Save uppercase "name" in new VAR
    name.text = name_upper  # Save new VAR under old VAR

xmldoc.write('./files/drugs_changed.xml')
