#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/18 17:53 
# @Author : Patrick 
# @File : kangoroo.py 
# @Software: PyCharm

def contains(a, b):
    c = 0
    if b in a:
        return False
    i, j = 0, 0
    while i < len(b):
        while j < len(a):
            if a[j] == b[i]:
                c += 1
                j += 1
                if c == len(b):
                    return True
                break
            j += 1
        i += 1

    return False


def anton(d):
    d2 = {}
    score = 0
    for k, v in d.items():
        for i in v:

            if contains(k, i):
                score -= 1
                if i not in d2:
                    d2[i] = [k]
                else:
                    d2[i].append(k)
    for k, v in d2.items():
        if len(v) > 1:
            score -= 1

    return score


def sysno(d):
    d2 = {}
    score = 0
    for k, v in d.items():
        for i in v:
            if contains(k, i):
                score += 1
                if i not in d2:
                    d2[i] = [k]
                else:
                    d2[i].append(k)
    for k, v in d2.items():
        if len(v) > 1:
            score += 1

    return score


def findKangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    # Write your code here
    score = 0
    dsyno, danto = {}, {}
    for i in wordsToSynonyms:
        word, l = i.split(':')[0], i.split(':')[1]
        if word in words:
            if ',' in l:
                dsyno[word] = l.split(',')
            else:
                dsyno[word] = [l]
    for i in wordsToAntonyms:
        word, l = i.split(':')[0], i.split(':')[1]
        if word in words:
            if ',' in l:
                danto[word] = l.split(',')
            else:
                danto[word] = [l]
    score += sysno(dsyno)
    score += anton(danto)
    return score


words = ['illuminated', 'animosity', 'deoxyribonucleic', 'container', 'lit', 'amity', 'encourage', 'lighted']
wordsToSynonyms = ['encourage:urge,boost,inspire', 'container:tin,can,bag,bottle', 'lighted:lit',
                   'illuminated:lit']
wordToAntonyms = ['encourage:discourage', 'animosity:amity,like', 'lighted:dark']
print(findKangarooScore(words, wordsToSynonyms, wordToAntonyms))
