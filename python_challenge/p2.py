from collections import Counter

from python_challenge.challenge import Challenge


class Challenge2(Challenge):

    def run(self, debug=False):
        self.read()
        c = Counter(self.data)
        cc = ''.join(k for k,v in c.items() if v==1)
        self.next_url = '{}.html'.format(cc)