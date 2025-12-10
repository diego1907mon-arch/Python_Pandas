class ProcesoDatos:
    def __init__(self, df):
        self.df = df

    def add_columns(self):
        
        self.df["Exceso_velocidad"] = self.df["Velocidad_detectada"] - self.df["Límite_velocidad"]

       
        self.df["Tipo_infracción"] = self.df["Exceso_velocidad"].apply(
            lambda x: "Grave" if x > 40 else "Moderada" if x > 20 else "Leve"
        )

       
        self.df["Hora_num"] = self.df["Hora"].str.split(":").str[0].astype(int)

   
        return self.df
