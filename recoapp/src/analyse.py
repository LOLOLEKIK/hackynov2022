import os

class analyze:
    @classmethod
    def analyze(self, text):
        lign = os.popen('./analyse.sh ' + str(text) ).read()
        return lign