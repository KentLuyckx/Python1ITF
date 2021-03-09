import xml.etree.ElementTree as ET  # Import ElementTree function
root = ET.Element('compilation')  # Naming the XML root

with open('./files/songs.txt') as file:  # Open songs.txt
    lines = file.readlines()  # Read all lines at once

    for line in lines:
        if line != '\n':  # For each new line in songs.txt
            record = line.split(';')  # Split information artist - song

            track = ET.Element('track')  # Create child-tag "track"
            track.text = ''  # Naming tag alone is ok
            root.append(track)  # Append "track" tag

            artist = ET.SubElement(track, 'artist')  # Create "artist" tag
            artist.text = record[0]  # Pull information from songs.txt and place in XML under "artist"

            song = ET.SubElement(track, 'song')  # Create "song" tag
            song.text = record[1].rstrip()  # Pull information from songs.txt and place in XML under "song"

xmlDoc = ET.ElementTree(root)  # Required to form ET into XML
xmlDoc.write('./files/songs.xml', encoding='UTF-8', xml_declaration=True)  # Write the actual XML
