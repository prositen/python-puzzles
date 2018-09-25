import re

from python_challenge.challenge import Challenge


class Challenge3(Challenge):
    """
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    """

    def run(self, debug=False):
        self.read()

        regex = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
        match = regex.findall(self.data)
        self.next_url = ''.join(match + ['.html'])