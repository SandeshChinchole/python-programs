
scores = [60, 50, 60, 58, 50, 34, 55, 69, 64, 46, 31, 41, 53, 58, 54, 54, 52, 54, 48, 69, 51, 52, 44, 51, 66, 55, 52, 61, 57, 52, 44, 18, 55, 61, 51, 44]

high_score = 0

length = len(scores)

for i in range(length):
    print('Bubble solution #' + str(i), 'score: ', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]

#for i in range(length):                                #my method
#    if high_score == scores[i]:
#        print('solutions with highest scores: ', i)


print('Bubble tests: ', length)
print('Highest bubble score: ',high_score)
print('Solutions with highest score: ',)
