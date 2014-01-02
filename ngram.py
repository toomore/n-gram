# -*- coding: utf-8 -*-
''' n-gram '''
from collections import Counter
import re


class Ngram(object):
    ''' n-gram '''
    def __init__(self, data=None):
        self.content = None
        self.counter = None

        if isinstance(data, file):
            self.data = data.read().decode('utf-8')
        else:
            self.data = data

        self.read_files()

    def read_files(self):
        ''' Read sample form files. '''
        self.content = self.data.replace('\n', ' ')
        self.content = re.sub(ur'[\w\/\.\-，、。：；？<:>()（） ]',
                              '', self.content)

    def make_gram(self, nums=6):
        ''' Make n gram '''
        return_data = []
        content_len = len(self.content)

        for i in sorted(range(nums + 1), reverse=1):
            assert (content_len - i) > 0
            for loops in range(content_len - i):
                add_str = self.content[loops : loops + i]
                if add_str:
                    return_data.append(add_str)

        return return_data

    def get_gram(self):
        ''' Get n-gram result. '''
        all_counter = dict(Counter(self.make_gram()))
        all_counter_copy = all_counter.copy()

        for i in all_counter:
            if all_counter_copy.get(i):
                if len(i) == 1 or all_counter_copy[i] == 1:
                    del all_counter_copy[i]
                else:
                    for loops in range(len(i)): # i = abcd, loops = 0~3
                        for sub_loops  in range(1, len(i)+1):
                            # sub_loops = 1,2,3,4
                            if sub_loops > loops and \
                                all_counter_copy.get(i[loops:sub_loops]) and \
                                i[loops:sub_loops] != i and \
                                (all_counter_copy[i[loops:sub_loops]] <= \
                                     all_counter_copy[i]):
                                del all_counter_copy[i[loops:sub_loops]]

        return all_counter_copy


if __name__ == '__main__':
    NGRAM = Ngram(open('./sample.txt'))
    #NGRAM = Ngram(u'我我我我我是我是我是我是我我我是我是')
    #for words in NGRAM.make_gram():
    #    print words
    #NGRAM.counter.most_common(10):
    #print len(NGRAM.make_gram())
    #for counts in Counter(NGRAM.make_gram()).most_common(10):
    #    print counts[0], counts[1]
    for counts in Counter(NGRAM.get_gram()).most_common(10):
        print counts[0], counts[1]
