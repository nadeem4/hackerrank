n = int(input())

hackerrank_arr = list("hackerrank")

for i in range(0,n):
    index = 0
    for char in list(input()):
        if hackerrank_arr[index] == char:
            index += 1
        if index == len(hackerrank_arr):
            break
    if index == len(hackerrank_arr):
        print("YES")
    else:
        print("NO")
         