"""
Este programa contiene las funciones para resolver la Situación Problema 1,
la cual involucra la comparación de caracteres en 5 archivos de texto. 

Autores:
Paulina Almada Martínez - A01710029
Miguel Ángel Barrón Sánchez - A01710304	
Jesús Alejandro Cedillo Zertuche - A01705442

Fecha de Creación:
06/10/2024

"""

"""
Lee y regresa los contenidos de un archivo txt.

Parámetros:
archivo (string): el archivo del que se quiere extraer el contenido.

Valor de Retorno:

Complejidad:
"""
def leerArchivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()

# Obtener contenido de los archivos de transmisión
trans01 = leerArchivo("transmission01.txt")
trans02 = leerArchivo("transmission02.txt")

transmissions = [trans01, trans02]

# Obtener contenido de los archivos mcode
mcode01 = leerArchivo("mcode01.txt")
mcode02 = leerArchivo("mcode02.txt")
mcode03 = leerArchivo("mcode11.txt")
test = leerArchivo("kmptest.txt")

mcodes = [mcode01, mcode02, mcode03, test]

# Función KMP para buscar subcadenas
def kmp(pat, txt):
    # Crear el arreglo de fallos para el patrón
    lps = [0] * len(pat)
    j = 0  # índice para pat[]
    
    # Preprocesar el patrón para llenar lps[]
    lps(pat, len(pat), lps)
    
    i = 0  # índice para txt[]
    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1
            
        if j == len(pat):
            return i - j  # Retorna la posición inicial de la coincidencia
        
        # Si hay un desajuste después de j coincidencias
        elif i < len(txt) and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
    return -1  # No se encontró coincidencia

# Función auxiliar para construir el arreglo LPS
def lps(pat, M, lps):
    length = 0  # longitud del prefijo más largo anterior
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Función para analizar si transmission contiene mcode
def analizar_archivos(mcode, transmission):
    # Usa la función kmp para determinar la posición de coincidencia
    return kmp(mcode, transmission)

# Primero verificar todos los mcodes contra transmission1
print("PARTE 1: Comparaciones entre texto de archivos transmission y mcode")
for i, mcode in enumerate(mcodes):
    pos = analizar_archivos(mcode, trans01)
    if pos != -1:
        print(f"mcode{i+1:02d} en transmission01: True {pos}")
    else:
        print(f"mcode{i+1:02d} en transmission01: False")

# Luego verificar todos los mcodes contra transmission2
for i, mcode in enumerate(mcodes):
    pos = analizar_archivos(mcode, trans02)
    if pos != -1:
        print(f"mcode{i+1:02d} en transmission02: True {pos}")
    else:
        print(f"mcode{i+1:02d} en transmission02: False")
