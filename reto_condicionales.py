def evaluar_palabra(palabra):
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print(f"La palabra '{palabra}' es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. '{palabra}' tiene {longitud} letras (minimo 4).")   
    else:
        print(f"sobran letras. '{palabra}' tiene {longitud} letras (maximo 8).") 
        
        
def determinar_cuadrante(x, y): 
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.") 
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")  
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")  
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.") 
    else:
        print("El punto se encuentra sobre un eje o en el origen.") 
if __name__ == "__main__":
        print("--- PRUEBA DE PALABRA ---")  
        palabra_usuario = input("Ingrese una palabra: ")   
        evaluar_palabra(palabra_usuario)
        
        print("\n--- PRUEBA DE CUADRANTE ---")
        x = float(input("Ingrese el valor de x: "))
        y = float(input("Ingrese el valor de y: "))
        determinar_cuadrante(x, y)
                      