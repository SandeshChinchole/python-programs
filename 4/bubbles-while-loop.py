
scores = [60, 50, 60, 58, 50, 34, 55, 69, 64, 46, 31, 41, 53, 58, 54, 54, 52, 54, 48, 69, 51, 52, 44, 51, 66, 55, 52, 61, 57, 52, 44, 18, 55, 61, 51, 44]

i = 0
score = ''


length = len(scores)

#print('My way')

#while (i <= length-1):
#    score = scores[i]
#    i = i + 1
#    print('Bubble solution #', i, 'score: ', score)

print("The book's way")

while (i < length):
    print('Bubble solution #' + str(i), 'score: ', scores[i])
    i = i + 1
    
    
#if score > score[i + 1]:
#    highest_score = score
#else:
#    highest_score = score[i + 1]


print('Bubble tests: ', length)
print('Highest bubble score: ',)
print('Solutions with highest score: ',)
