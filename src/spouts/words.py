from itertools import cycle

import requests
from xml.etree import ElementTree

from streamparse import Spout


class WordSpout(Spout):
    # outputs = ['word']
    outputs = ['score','number']

    def initialize(self, stormconf, context):
        url = 'https://storage.googleapis.com/distsys-pa3-data/test2.xml'
        # response = requests.get(url)
        # self.rows = ElementTree.fromstring(response.content)
        # self.words = cycle(['dog', 'cat', 'zebra', 'elephant'])

        response = requests.get(url, stream=True)
        # if the server sent a Gzip or Deflate compressed response, decompress
        # as we read the raw stream:
        response.raw.decode_content = True

        self.rows = ElementTree.iterparse(response.raw)

    def next_tuple(self):
        try:
            number = next(self.rows)[1].get('Score')
            self.emit(['score', number])
        except Exception as e:
            pass
        # word = next(self.words)
        # self.emit([word])
