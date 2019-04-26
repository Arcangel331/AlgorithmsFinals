'''
Final Exam
CMPT 306
@author: Aidan Crump
'''

def change_making(d, n): 
    d.sort()
    coins = []
    i = (len(d) - 1)

    while i >= 0:
        while n >= d[i]:
           n -= d[i]
           coins.append(d[i])
        i -= 1
    return coins


if __name__ == "__main__":
    #d = [1,2,3]
    #n = 10
    d = [1,5,3]
    n = 14
    print(change_making(d,n))
