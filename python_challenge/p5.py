import os
import pickle

from python_challenge.challenge import Challenge


class Challenge5(Challenge):
    def run(self, debug=False):
        with open(os.path.join('data', 'input5.p'), 'rb') as fh:
            self.data = pickle.load(fh)
        if debug:
            for line in self.data:
                print(''.join(k[0]*k[1] for k in line))

        self.next_url = 'channel.html'
