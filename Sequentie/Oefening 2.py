yes_votes = int(input("How many people voted YES: "))
no_votes = int(input("How many people voted NO: "))
blank_votes = int(input("Number of BLANK votes: "))

total_votes = yes_votes + no_votes + blank_votes
print("YES: ", yes_votes * 100 // total_votes + "%")
print("NO: ", no_votes * 100 // total_votes + "%")
print("BLANK: ", blank_votes * 100 // total_votes + "%")
