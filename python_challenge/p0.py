from python_challenge.challenge import Challenge


class Challenge0(Challenge):
    def run(self, debug=False):
        self.next_url = '{}.html'.format(2**38)