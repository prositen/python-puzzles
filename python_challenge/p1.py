import string

from python_challenge.challenge import Challenge


class Challenge1(Challenge):

    def run(self, debug=False):
        self.read()

        intab = string.ascii_lowercase
        outtab = intab[2:] + intab[:2]

        message = 'map'
        tr = str.maketrans(intab, outtab)
        if debug:
            print(self.data.translate(tr))
        self.next_url = message.translate(tr) + '.html'