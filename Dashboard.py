class Dashboard:
    def _init_(self, stats1, stats2, graficos):
        self.stats1 = stats1
        self.stats2 = stats2
        self.graficos = graficos

  
    def mostrar_menu(self):
        while True:
            print(" DASHBOARD DE FOTOMULTAS")
            print("1. Métricas numéricas básicas")
            print("2. Métricas categóricas (clima, marca, tipo de vía)")
            print("3. Cuartiles y percentiles")
            print("4. Gráficos")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_basico()

            elif opcion == "2":
                self.metricas_categoricas()

            elif opcion == "3":
                self.menu_cuartiles()

            elif opcion == "4":
                self.menu_graficos()

            elif opcion == "0":
                print("Saliendo del sistema…")
                break

            else:
                print("Opción inválida.")


    def menu_basico(self):
        print("MÉTRICAS NUMÉRICAS BÁSICAS")

        num_cols = self.stats1.df.select_dtypes(include="number").columns

        for col in num_cols:
            print(f"\n--- {col} ---")
            print(f"Cantidad: {self.stats1.df[col].count()}")
            print(f"Media: {self.stats1.df[col].mean():.2f}")
            print(f"Mínimo: {self.stats1.df[col].min()}")
            print(f"Máximo: {self.stats1.df[col].max()}")
            print(f"Desviación estándar: {self.stats1.df[col].std():.2f}")


    def metricas_categoricas(self):
        print("MÉTRICAS CATEGÓRICAS ")

        print("\n--- Distribución de infracciones por clima ---")
        print(self.stats2.infracciones_por_clima())

        print("\n--- Marcas con más infracciones (Top 5) ---")
        print(self.stats2.infracciones_por_marca(5))

        print("\n--- Infracciones por tipo de vía ---")
        print(self.stats2.df["Tipo_vía"].value_counts())


    def menu_cuartiles(self):
        print("CUARTILES Y PERCENTILES ")

        print("\n--- Cuartiles de exceso ---")
        print(self.stats2.cuartiles_exceso())

        print("\n--- Percentil 90 de exceso ---")
        print(self.stats2.percentil_90_exceso())


    def menu_graficos(self):
        print("MOSTRANDO TODOS LOS GRÁFICOS")

        print("Generando gráfico 1: Infracciones por clima...")
        self.graficos.grafico_barras_clima()

        print("Generando gráfico 2: Infracciones por marca...")
        self.graficos.grafico_pastel_marca()

        print("Generando gráfico 3: Histograma de velocidad detectada...")
        self.graficos.grafico_histograma_velocidad()