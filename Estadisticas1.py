class Estadisticas1:
    def __init__(self, df):
        self.df = df

   
    def velocidad_promedio(self):
        """Retorna la velocidad promedio detectada."""
        return self.df["Velocidad_detectada"].mean()

    def exceso_promedio(self):
        """Retorna el exceso de velocidad promedio."""
        return self.df["Exceso_velocidad"].mean()

  
    def infracciones_por_clima(self):
        """Retorna cuántas infracciones ocurrieron según el clima."""
        return self.df.groupby("Clima")["ID_foto"].count()

    def infracciones_por_marca(self, top=5):
        """Retorna las marcas con más infracciones (Top n)."""
        return self.df["Marca_vehículo"].value_counts().head(top)

    def infracciones_por_tipo_via(self):
        """Retorna cantidad de infracciones por tipo de vía."""
        return self.df["Tipo_vía"].value_counts()

    def camaras_fuera_de_servicio(self):
        """Número de cámaras que no estaban funcionando."""
        return self.df[self.df["Cámara_funcionaba"] == "No"].shape[0]

    