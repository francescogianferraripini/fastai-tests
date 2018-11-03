from fastai import Learner


class QModelPackager:
    def __init__(self, url:str, learner:Learner = None): 
        self.url = url

x = QModelPackager('Ciao')

print(x.url)