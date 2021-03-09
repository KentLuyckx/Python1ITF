# Longest
with open('./files/irish_song.txt') as file:
    lines = file.readline()
    longest = ''
    while lines:
        if len(lines) > len(longest):
            longest = lines.rstrip()
        lines = file.readline()
    print("The longest line has", len(longest), "characters")
    print(longest)

# Shortest
with open('./files/irish_song.txt') as file:
    shortest_line = min(file, key=len).rstrip()
print("The shortest line has", len(shortest_line), "characters")
print(shortest_line)
