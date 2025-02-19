# Explicacion
Como funcionan los buffers en la vida real es que se tienen dos uno que es el principal y el otro de apoyo o el acumulado. 
El primero se llena con el tamaño del buffer y el segundo por si no se llego a terminar de procesar una palbra.

## funciones
### Cargar Buffer
Esta funcion sirve para cargar una parte de la entrada al buffer y de ser el final le agrega nuestro indicador de final de linea
````python
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof") 
    return buffer
````
### Procesar Buffer
Esta funcion se encarga de leer el buffer y detectar si existe un buffer acumulado para tenerlo en cuenta.
Se tienen dos punteros uno para el marcar el incio del procesamiento y el otro para realizar el avance, cuando encuentra un espacio vacio
(convencion par aeste ejercicio) se termina de leer y se procesa el lexema, hasta terminar si al final del array no llego a un espacio vacio o se quedo incompleto lo agrega a buffer acumulado.

````python
def procesar_buffer(buffer, buffer_acumulado):
    startIndex = 0
    currentIndex = 0
    lexemas = [] # Hola :3

    if buffer_acumulado:
        buffer = buffer_acumulado + buffer
        buffer_acumulado.clear()
    
    while currentIndex < len(buffer):
        if buffer[currentIndex] == " " or buffer[currentIndex] == "eof":
            lexema = "".join(buffer[startIndex:currentIndex])
            if lexema:
                lexemas.append(lexema)
            startIndex = currentIndex + 1
        
        currentIndex += 1

    if startIndex < len(buffer) and " " not in buffer[startIndex:]:
        buffer_acumulado.extend(buffer[startIndex:])

    return lexemas, buffer_acumulado
````
### Inicio del programa

````python 
entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
buffer_acumulado = []

while inicio < len(entrada):
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    inicio += tamano_buffer

    lexemas, buffer_acumulado = procesar_buffer(buffer, buffer_acumulado)
    
    for lexema in lexemas:
        print(f"Lexema procesado: {lexema}")

if buffer_acumulado:
    print(f"Lexema procesado: {''.join(buffer_acumulado)}")
````
