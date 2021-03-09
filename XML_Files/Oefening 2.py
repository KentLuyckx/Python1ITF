import xml.etree.ElementTree as ET
xmldoc = ET.parse("./files/cinemas.xml")
root = xmldoc.getroot()

print('Bioscopen in Antwerpen: ')
# <editor-fold desc="Old solution">
# for cinema in root.findall('bioscoopoverzicht'):
#    name = cinema.find('naam').text
#    address = cinema.find('straat').text + ' ' + cinema.find('huisnummer').text
#    city = cinema.find('postcode').text + ' ' + cinema.find('district').text
#    print(name, '\n' + address.upper(), '\n' + city)
#    print()
# </editor-fold>

# <editor-fold desc="New solution">
for cinema in root.findall('bioscoopoverzicht'):
    print(cinema.find('naam').text)
    print(cinema.find('straat').text, cinema.find('huisnummer').text)
    print(cinema.find('postcode').text, cinema.find('district').text + '\n')
# </editor-fold>
