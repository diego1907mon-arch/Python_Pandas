import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, df):
        self.df = df

    def grafico_barras_clima(self):
        counts = self.df["Clima"].value_counts()
        counts.plot(kind="bar")
        plt.title("Infracciones por clima")
        plt.xlabel("Clima")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=0)
        plt.show()

    def grafico_pastel_marca(self):
        counts = self.df["Marca_vehículo"].value_counts().head(10)
        counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Top 10: Marcas con más infracciones")
        plt.ylabel("")  
        plt.show()

    def grafico_histograma_velocidad(self):
     print("--- GRÁFICO: DISTRIBUCIÓN DE VELOCIDADES ---")
     self.df["Velocidad_detectada"].plot(kind="hist", bins=15, alpha=0.7)
     plt.title("Distribución de velocidades detectadas")
     plt.xlabel("Velocidad")
     plt.ylabel("Frecuencia")
     plt.show()