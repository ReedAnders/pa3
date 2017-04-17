"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.wordcount import WordCountBolt
from spouts.words import WordSpout


class WordCount(Topology):
    word_spout = WordSpout.spec()
    count_bolt = WordCountBolt.spec(inputs={word_spout: Grouping.fields('score')},
                                par=2)
    # count_bolt = WordCountBolt.spec(inputs={word_spout: Grouping.fields('score')},
    #                                 par=2)
