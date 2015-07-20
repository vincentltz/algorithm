"""
CS325 - Summer 2015
Project 2
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/17/2015
"""

import sys
import re
import ast


def main():
 
    V = [1, 10, 15, 50]
    A = 21

    
    print "coins: %s, amount: %d\n" % (V, A)

    print "---Greedy Algorithm---"
    coins, count = changegreedy(V, A)
    for coin in coins:
        print "%d coins of %d value" % (coin['count'], coin['value'])
    print "count: %d coins\n" % count

    print "---Brute Force Algorithm---"
    coins, count = changeslow(V, A)
    coins.reverse()
    V.reverse()
    for coin, value in enumerate(coins):
        print "%d coins of %d value" % (value, V[coin])
    print "count: %d coins\n" % count
    V.reverse()

    print "---Dynamic Programming---"
    coins, count = changedp(V, A)
    coins.reverse()
    V.reverse()
    for coin, value in enumerate(coins):
        print "%d coins of %d value" % (value, V[coin])
    print "count: %d coins\n" % count
    V.reverse()
    
    """
    print "The input array is:\n", V,"\nThe amount of change we have to make is:\n",A
    
    
    res = changegreedy(V, A)
    print "\nBy using the Greedy Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]
    
    
    res = changeslow(V, A)
    print "\nBy using the Brute Force Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]
    
    res = changedp(V, A)
    print "\nBy using the Dynamic Programming Method, the result array is:\n", res[0], "\nthe number of coins costed is:\n", res[1]
    """

def changeslow(l, A):

    m = 0
    n = len(l)
    c = [0]*n
    minm = A
    if A > 0:
        for i in range(0,n):
            if A == l[i]:
                m += 1
                c[i] += 1
                return [c,m]

        c = [A] + [0]*(n-1)
        for i in range(1,A/2+1):
            d = [0]*n
            m = 0
            result1 = changeslow(l,i)
            for j in range(0,n):
                d[j] += result1[0][j]
            m += result1[1]
            result2 = changeslow(l,A-i)
            for j in range(0,n):
                d[j] += result2[0][j]
            m += result2[1]
            if minm > m:
                minm = m
                c = d
    return c, minm


def changegreedy(coins, amount):
    coins.sort()
    coins.reverse()
    change = []
    total = 0

    for i in coins:
        count = amount/i
        total += count
        amount = amount%i
        change.append({'count':count, 'value':i})

    coins.reverse()
    return change, total


def changedp(l, A):
    n = len(l)
    c = [0]*n
    cc = [[0]*n]*(A+1)
    T = [0]*(A+1)
    for i in range (1,A+1):
        d = [0]*n
        cc[i] = [0]*n
        for j in range (0,n):
            k = i - l[j]
            if k >= 0:
                d[j] = T[k] + 1
            else:
                d[j] = d[j-1]
        T[i] = d[0]
        index = 0
        for x in range(1,n):
            if d[x] < d[x-1]:
                T[i] = d[x]
                index = x
        k = i - l[index]
        for a in range(0,n):
            if a == index:
                cc[i][a] = cc[k][a] + 1
            else:
                cc[i][a] = cc[k][a]
    return cc[A], T[A]


if __name__ == '__main__':
    main()
