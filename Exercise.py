# SECOND HIGHEST MARKS

#n = int(input())
#arr = list(map(int, input().split()))
#arrmax = 0
#def SecondLargestTerm(array):
#    abc = []
#    for i in range(len(array)):
#        if array[i] == max(array):
#            abc.append(i)
#    print(abc)
#    for n in abc:
#        array[n] = 'a'
#        print(array)
#    pqr = []
#    for i in array:
#        if i != 'a':
#            pqr.append(i)
#    return max(pqr)
#print(SecondLargestTerm(arr))


# NESTED LISTS

#arrayName = []
#arrayScore = []
#for y in range(int(input())):
#        name = input()
#        score = float(input())
#        arrayName.append(name)
#        arrayScore.append(score)
#arrmin = 0
#def SecondSmallestNumber(array):
#    abc = []
#    for i in range(len(array)):
#        if array[i] == min(array):
#            abc.append(i)
#    print(abc)
#    for n in abc:
#        array[n] = 'a'
#        print(array)
#    pqr = []
#    for i in array:
#        if i != 'a':
#            pqr.append(i)
#    return min(pqr)
#secSmall = SecondSmallestNumber(arrayScore)
#ranName = []
#for i in range(len(arrayScore)):
#    if arrayScore[i] == secSmall:
#        ranName.append(arrayName[i])
#        print(ranName)
#ranName.sort()
#for xyz in ranName:
#    print(xyz)

# FINDING THE PERCENTAGE

#n = int(input())
#student_marks = {}
#for _ in range(n):
#    name, *line = input().split()
#    scores = list(map(float, line))
#    student_marks[name] = scores
#query_name = input()
#total = 0
#for x, z in student_marks.items():
#    if x == query_name:
#        for i in z:
#            total = total + i
#print("{:.2f}".format(total/3))


print('GitHub works pretty well')
