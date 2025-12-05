class Estadisticas2:
    def _init_(self, df):
        self.df = df

    def max_exceso_registrado(self):
        return self.df["Exceso_velocidad"].max()

    def infracciones_por_tipo(self):
        return self.df["Tipo_infracción"].value_counts()

    def infracciones_por_marca(self, top=5):
        return self.df["Marca_vehículo"].value_counts().head(top)

    def camaras_con_mas_infracciones(self, top=5):
        return self.df.groupby("ID_cámara")["ID_foto"].count().sort_values(ascending=False).head(top)

    def promedio_por_tipo_via(self):
        return self.df.groupby("Tipo_vía")["Velocidad_detectada"].mean()

    def porcentaje_infracciones_graves(self):
        total = len(self.df)
        graves = self.df[self.df["Tipo_infracción"] == "Grave"].shape[0]
        return (graves / total) * 100