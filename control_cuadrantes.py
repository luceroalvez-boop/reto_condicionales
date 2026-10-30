cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")
intentos_palabras =  [ ]
palabra_ingresada = input("Ingresa una palabra: ")
intentos_palabras.append(palabra_ingresada)
indice_cuadrante = 0
print(f"La palabra '{palabra_ingresada}' fue registrada en el {cuadrantes [ indice_cuadrante]}")
print("\n--- Historial de la sesion ---")
print(f"Palabras intentadas en total: {intentos_palabras}")
