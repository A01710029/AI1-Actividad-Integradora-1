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

Complejidad: O(n)
"""
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()

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

"""
Función para encontrar el palíndromo más largo en una cadena de texto
utilizando el algoritmo de Manacher.

Parámetros:
transmission (string): el contenido de un archivo de transmission.

Valor de Retorno:
(start, end) (tuple): una tupla con la posición inicial y final del palíndromo más largo.

Complejidad: O(n)
"""
def manacher(transmission):
    # Se cambia la cadena original para siempre hacerla impar
    T = '|' + '|'.join(transmission) + '|'
    n = len(T)
    L = [0] * n 
    
    # Se inicializan las variables del centro y límite derecho del palíndromo más largo
    C, R = 0, 0  

    # Se inicializan las variables para el palíndromo más largo
    max_len = 0 
    center_index = 0  # Centro del palíndromo más largo
    
    for i in range(n):
        mirror = 2 * C - i  # Índice reflejado respecto al centro actual
        
        # Si el índice actual está dentro del límite derecho 
        if i < R:
            # Se usa la simetria para acelerar el proceso
            L[i] = min(R - i, L[mirror])
        
        # Se verifica si el caracter de la izquierda y derecha son iguales
        # Si lo son, se expande L[i] (radio del palíndromo)
        while i + L[i] + 1 < n and i - L[i] - 1 >= 0 and T[i + L[i] + 1] == T[i - L[i] - 1]:
            L[i] += 1
        
        # Si se encuentra un palíndromo más largo, se actualiza el centro y el límite derecho
        # El centro es igual a i (posición actual) y el límite derecho es igual a i + L[i] (radio del palíndromo)
        if i + L[i] > R:
            C, R = i, i + L[i]
        
        # Si el palíndromo actual es más largo que el máximo encontrado hasta ahora
        # Se actualiza la longitud del palíndromo más largo y su centro
        if L[i] > max_len:
            max_len = L[i]
            center_index = i
    
    # Se saca la posición inicial y final del palíndromo más largo
    start = (center_index - max_len) // 2
    end = start + max_len - 1
    
    return (start + 1, end + 1)

"""
Función para encontrar las subcadenas comunes más largas entre dos cadenas
utilizando Longest Common Substring.

Parámetros:
transmission1 (string): el contenido del primer archivo de transmission.
transmission2 (string): el contenido del segundo archivo de transmission.

Valor de Retorno:
results (list): una lista con las posiciones iniciales y finales de los subcadenas comunes más largas.

Complejidad: O(n * m)
"""
def longestCommonSubstrings(transmission1, transmission2):
    # Se saca la longitud de las cadenas
    len1 = len(transmission1)
    len2 = len(transmission2)
    
    # Se crea la matriz con todos los valores en 0
    matrix = []
    for _ in range(len1 + 1):
        matrix.append([0] * (len2 + 1))

    max_len = 0

    # En caso que haya 2 de la misma longitud se almacena en un arreglo
    results = set()

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # Si los caracteres coinciden se incrementa el valor en la matriz
            if transmission1[i - 1] == transmission2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1

                # Si la longitud es mayor a la máxima encontrada hasta ahora
                # Se actualiza la longitud máxima y se reinicia la lista de resultados
                if matrix[i][j] > max_len:
                    max_len = matrix[i][j]
                    results = {(i - max_len, i)}
                # Si hay más de una subcadena de la misma longitud se añade a la lista
                elif matrix[i][j] == max_len:
                    results.add((i - max_len + 1, i)) 

    return list(results)

# Obtener contenido de los archivos de transmisión
trans01 = leer_archivo("transmission01.txt")
trans02 = leer_archivo("transmission02.txt")

transmissions = [trans01, trans02]

# Obtener contenido de los archivos mcode
mcode01 = leer_archivo("mcode01.txt")
mcode02 = leer_archivo("mcode02.txt")
mcode03 = leer_archivo("mcode03.txt")

mcodes = [mcode01, mcode02, mcode03]

# Primero comparar todos los mcodes contra transmission1
comparar_mcodes(mcodes, trans01, "transmission01")

# Luego comparar todos los mcodes contra transmission2
comparar_mcodes(mcodes, trans02, "transmission02")

start01, end01 = manacher(trans01)
print("\nPalíndromo transmission01: " + str(start01) + " " + str(end01))
print(f"Palíndromo más largo en transmission01: {trans01[start01 - 1:end01]}")

start02, end02 = manacher(trans02)
print("\nPalíndromo transmission02: " + str(start02) + " " + str(end02))
print(f"Palíndromo más largo en transmission02: {trans02[start02 - 1:end02]}")

matches = longestCommonSubstrings(trans01, trans02)
print(f"Los substrings más largos entre las dos transmisiones son:")
for start, end in matches:
    print(f"Inicia en {start} y termina en {end}")