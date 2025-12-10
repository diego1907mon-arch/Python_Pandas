import pandas as pd

class Cargar:
    def __init__(self, path):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)
        return df
