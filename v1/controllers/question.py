import pandas as pd
from difflib import SequenceMatcher
from v1.model.googleDrive import GgDrive
import webbrowser

class CheckAnswer():
    def __init__(self):
        self.MIN_CORRECT = 0.8
        self.df = GgDrive().get()
    def check(self,question):
        datas = self.df.values.tolist()
        best = -1
        curBest = []
        for data in datas:
            temp = SequenceMatcher(None, data[0], question).ratio()
            if temp> best:
                best = temp
                curBest = data
        if best< self.MIN_CORRECT:
            return None
        else: return {'answer':curBest[1], 'certainty': best}
class GoogleSrearch():
    def __init__(self):
        self.MIN_CORRECT = 0.6
    def check(self,question):
        answer = webbrowser.open('https://www.google.com/search?q='+question, new=2)
        print(answer)

if __name__ == "__main__":
    checkAnswer = CheckAnswer()
    print(checkAnswer.check("What is the capital of Vietnam?"))
       