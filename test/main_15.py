# -*- coding: utf-8 -*-
# @Author: Chen Zhiquan
# @Date:   2019-04-25 20:22:46
# @Last Modified by:   octavian
# @Last Modified time: 2019-04-25 20:39:16
from algorithm.chap_15 import *
import string
import random


def string_gen(size=20, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def lps_1_main():
    s = string_gen()
    length, sub = lps_1(s)
    print("The lps is {}".format(sub))


if __name__ == "__main__":
    lps_1_main()