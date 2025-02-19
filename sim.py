def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof") 
    return buffer

def procesar_buffer(buffer, buffer_acumulado):
    startIndex = 0
    currentIndex = 0
    lexemas = []

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

