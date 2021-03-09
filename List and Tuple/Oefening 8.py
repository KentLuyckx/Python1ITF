scores = []
amount_of_scores = 0
sum_scores = 0
average_score = 0
i = 0

print("Enter the scores for the test. Use -1 if you want to finish")
score = float(input("Score: "))
while score > -1:
    scores.append(score)
    amount_of_scores += 1
    score = float(input("Score: "))
for i in range(0, len(scores)):
    sum_scores = sum_scores + scores[i]
    average_score = sum_scores / amount_of_scores
print("The scores (ordered): ", sorted(scores))
print("The average of these", amount_of_scores, "scores =", average_score)

