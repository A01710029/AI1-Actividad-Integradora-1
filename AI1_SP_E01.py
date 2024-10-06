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
contenido del archivo (string)

Complejidad:
"""
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()

# Obtener contenido de los archivos de transmisión
trans01 = leer_archivo("transmission01.txt")
trans02 = leer_archivo("transmission02.txt")

transmissions = [trans01, trans02]

# Obtener contenido de los archivos mcode
mcode01 = leer_archivo("mcode01.txt")
mcode02 = leer_archivo("mcode02.txt")
mcode03 = leer_archivo("mcode03.txt")

mcodes = [mcode01, mcode02, mcode03]

"""
Compara el contenido de mcode con el de transmission 
para encontrar si se repite una subcadena utilizando el algoritmo KMP.

Parámetros:
patron (string): los caracteres que se buscan.
texto (string): la cadena de texto donde se buscan.

Valor de Retorno:
i (int): índice de la posición inicial del patrón encontrado,
-1 si no se encuentra.

Complejidad: O(n+m)
"""
def kmp(patron, texto):
    # Crear el arreglo de fallos para el patrón
    lps = [0] * len(patron)
    j = 0  # índice para patrón[]
    
    # Preprocesar el patrón para llenar lps[]
    crear_lps(patron, len(patron), lps)
    
    i = 0  # índice para texto[]
    while i < len(texto):
        if patron[j] == texto[i]:
            i += 1
            j += 1
            
        if j == len(patron):
            return i - j  # Retorna la posición inicial de la coincidencia
        
        # Si hay un desajuste después de j coincidencias
        elif i < len(texto) and patron[j] != texto[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1 
    return -1  

"""
Función auxiliar para construir el arreglo LPS 
utilizado por el algoritmo KMP.

Parámetros:
archivo (string): el archivo del que se quiere extraer el contenido.
m (int): longitud de la subcadena que se busca.
lps (array): arreglo donde se guarda la comparación más grande ya realizada.

Valor de Retorno:
lps (array): un arreglo con los índices de los prefijos más largos.

Complejidad: O(n)
"""
def crear_lps(patron, m, lps):
    long = 0  # longitud del prefijo más largo anterior
    i = 1
    while i < m:
        if patron[i] == patron[long]:
            long += 1
            lps[i] = long
            i += 1
        else:
            if long != 0:
                long = lps[long - 1]
            else:
                lps[i] = 0
                i += 1

"""
Función para realizar las comparaciones entre archivos transmission
y mcode y regresar los resultados con el formato esperado.

Parámetros:
mcodes (array): un arreglo con el contenido de cada archivo mcode.
transmission (string): el contenido de un archivo de transmission.
nombre_transmission (string): el nombre del archivo de transmission.

Valor de Retorno:
No aplica, ya que los imprime a consola directamente.

Complejidad: O(k*(n+m))
"""
def comparar_mcodes(mcodes, transmission, nombre_transmission):
    print(f"\nComparaciones entre mcodes y {nombre_transmission}")
    for i, mcode in enumerate(mcodes):
        pos = kmp(mcode, transmission)
        if pos != -1:
            print(f"mcode{i+1:02d} en {nombre_transmission}: True {pos}")
        else:
            print(f"mcode{i+1:02d} en {nombre_transmission}: False")

# Primero comparar todos los mcodes contra transmission1
comparar_mcodes(mcodes, trans01, "transmission01")

# Luego comparar todos los mcodes contra transmission2
comparar_mcodes(mcodes, trans02, "transmission02")

