#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/5 16:57 
# @Author : Patrick 
# @File : 843. Guess the Word.py 
# @Software: PyCharm


def findSecretWord(wordlist, master):
    import random
    for i in range(10):
        word = random.choice(wordlist)
        ans = master.guess(word)
        wordlist = [w for w in wordlist if sum(i == j for i, j in zip(word, w)) == ans]


findSecretWord("hbaczn",
               ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos",
                "acrtag", "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla",
                "ymqhxk", "qkvipb", "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc",
                "tamszl", "osdifo", "dvxlxm", "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl",
                "tittgf", "evqsqe", "aishiv", "pmwovj", "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz",
                "arabol", "uywurk", "ppywdo", "resfls", "tmoliy", "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy",
                "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg", "egcdab", "cykndr", "lkzobv", "ifwmwp",
                "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg", "sczjmz", "hsdjfp", "mjcgvm",
                "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs", "oxblph", "twejel",
                "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq", "brklfk"]
               )
