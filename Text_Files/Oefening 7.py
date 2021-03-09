with open("./files/playlist.txt", encoding="utf-8") as file:
    lines = file.readlines()
    lines.sort()
    print("Playlist:")
    for line in lines:
        record = line.split(";")
        print("{} \t {} ({})".format(record[0], record[1].upper(), record[2].rstrip().lower()))
