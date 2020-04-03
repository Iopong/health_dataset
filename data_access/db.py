import pandas as pd

class DBM:
    def __init__(self, obj):
        self._dataframe = pd.DataFrame(data=obj) 

    def _clean(self):
        #clean data
        pass

    def _combine(self):
        #do something
        pass
    
    def _store(self):
        #store in db
        pass
    
    def run(self):
        #clean, combine, store?
        pass