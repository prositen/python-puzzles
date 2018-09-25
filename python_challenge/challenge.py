import os


class Challenge(object):

    BASE_URL = 'http://www.pythonchallenge.com/pc/def/'

    def __init__(self, level):
        self.level = level
        self.next_url = ''
        self.data = ''

    def run(self, debug=False):
        pass

    def solve(self, debug=False):
        self.run(debug)
        return '{}{}'.format(self.BASE_URL, self.next_url)

    def read(self, filename='input{}.txt'):
        with open(os.path.join('data', filename.format(self.level))) as fh:
            self.data = fh.read()

    @staticmethod
    def challenge(level):
        # Standard import
        import importlib
        module_name = 'python_challenge.p{}'.format(level)
        class_name = 'Challenge{}'.format(level)
        MyClass = getattr(importlib.import_module(module_name), class_name)
        # Instantiate the class (pass arguments to the constructor, if needed)
        return MyClass(level)
