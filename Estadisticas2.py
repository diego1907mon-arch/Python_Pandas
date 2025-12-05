class Estadisticas2:
    def _init_(self, df):
        self.df = df

    def max_exceso_registrado(self):
        return self.df["Exceso_velocidad"].max()

    def infracciones_por_tipo(self):
        return self.df["Tipo_infracción"].value_counts()

    