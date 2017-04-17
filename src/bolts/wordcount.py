from __future__ import division
import os
from collections import Counter

from streamparse import Bolt


class WordCountBolt(Bolt):
    outputs = ['score', 'count']
    # outputs = ['word', 'count']

    def initialize(self, conf, ctx):
        self.counter = 0
        self.pid = os.getpid()
        self.total = 0

    def _increment(self, score, number, inc_by):
        # self.counter[word] += inc_by
        self.counter += int(number)
        self.total += inc_by

    def process(self, tup):
        # word = tup.values[0]
        score = tup.values[0]
        number = tup.values[1]
        # self._increment(word, 10 if word == "dog" else 1)
        self._increment(score, number, 1)
        if self.total % 1000 == 0:
            self.logger.info("counted [{:,}] scores [pid={}]".format(self.total,
                                                                    self.pid))
        average = self.counter / self.total

        print("DATA:",average, self.total)
        self.emit([average, self.total])
        # self.emit([word, self.counter[word]])
