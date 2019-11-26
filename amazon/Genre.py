#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/6 15:18 
# @Author : Patrick 
# @File : Genre.py
# @Software: PyCharm


def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    ans = {}
    bookToGenres = {}

    for gen in bookGenres.keys():
        for book in bookGenres[gen]:
            bookToGenres[book] = gen
    count = {}
    m = -float('inf')
    for user in userBooksListenedTo.keys():
        count = {}
        m = -float('inf')
        ans[user] = []
        for book in userBooksListenedTo[user]:
            genre = bookToGenres.get(book, None)
            if not genre:
                continue
            c = count.get(genre, 0) + 1
            count[genre] = c
            m = max(m, c)

        for k in count.keys():
            if (count[k] == m):
                ans[user].append(k)

    return ans


print(favoriteVideoGenre({'j': ['latin', 'Tombs', 'Nation']}, {'his': ['latin', 'Nation'], 'Horr': ['Tombs']}))
