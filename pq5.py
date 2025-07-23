'''Python Program to Reverse Every Kth row in a Matrix
'''
a = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
K = 3

res = []
for i, ele in enumerate(a):

    # checking for K multiple
    if (i + 1) % K == 0:

        # reversing using reversed
        res.append(list(reversed(ele)))
    else:
        res.append(ele)

print("After reversing the Kth row: " + str(res))