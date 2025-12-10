from Cargar import Cargar
from ProcesoDatos import ProcesoDatos
from Estadisticas1 import Estadisticas1
from Estadisticas2 import Estadisticas2
from graficos import Graficos
from Dashboard import Dashboard

def main():
    
    loader = Cargar("c:\Users\FORMACION.DESKTOP-I8U8GQ7\Downloads\dataset_fotomultas_1000.csv")
    df = loader.load()

    df = ProcesoDatos(df).add_columns()

    
    stats1 = Estadisticas1(df)
    stats2 = Estadisticas2(df)
    graficos = Graficos(df)

    dashboard = Dashboard(stats1, stats2, graficos)
    dashboard.mostrar_menu()

if __name__ == "_main_":
    main()