import requests

from python_challenge.challenge import Challenge


class Challenge4(Challenge):

    def run(self, debug=False):
        """
        urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
        :return:
        """

        visited = set()
        nothing = '12345'
        prev_nothing = ''
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
        for _ in range(400):
            if nothing in visited:
                break
            visited.add(nothing)
            next_url = url.format(nothing)
            result = requests.get(next_url)
            prev_nothing = nothing
            nothing = result.content.decode('ascii').split(' ')[-1]
            if debug:
                print(nothing)
        self.next_url = prev_nothing
