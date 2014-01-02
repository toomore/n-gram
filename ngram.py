# -*- coding: utf-8 -*-
from collections import Counter
import re


class Ngram(object):
    def __init__(self):
        pass

    def read_files(self, path):
        f = open(path, 'r')
        self.content = f.read().replace('\n', ' ').decode('utf-8')
        self.content = re.sub(ur'[\w\/\.\-，、。：；？ ]', '', self.content)

    def make_gram(self, n=6):
        return_data = []
        l = len(self.content)

        for i in sorted(range(n+1), reverse=1):
            assert (l-i) > 0
            for e in range(l-i):
                add_str = self.content[e : e+i]
                return_data.append(add_str) if add_str else None

        return return_data

    def make_counter(self):
        self.counter = Counter(self.make_gram())

    def get_gram(self):
        d = dict(self.counter)
        d_copy = d.copy()

        for i in d:
            if d_copy.get(i):
                if len(i) == 1 or d_copy[i] == 1:
                    del d_copy[i]
                else:
                    for ii in range(len(i)): # i = abcd, ii = 0~3
                        for e in range(1, len(i)+1): # e = 1,2,3,4
                            if e > ii and d_copy.get(i[ii:e]) and i[ii:e] != i \
                                      and (d_copy[i[ii:e]] <= d_copy[i]):
                                del d_copy[i[ii:e]]

        return d_copy


if __name__ == '__main__':
    n = Ngram()
    n.read_files('./sample.txt')
    n.make_counter()
    for i in n.make_gram():
        print i
    #n.counter.most_common(10):
    #print len(n.make_gram())
    #for i in Counter(n.make_gram()).most_common(10):
    #    print i[0],i[1]
    for i in Counter(n.get_gram()).most_common(10):
        print i[0],i[1]
