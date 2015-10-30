import threading

manywords=0                   # VARIABLE: Contar palabras en el archivo
conta=0                       # VARIABLE: Contar Cantidad de palabras por Vector
contb=0                       #  "
contc=0                       #  "
contd=0                       #  "
conte=0                       #  "
matrixa=[]                    # VECTOR: Matrix para almacenar una cantidad especifica de palabras
matrixb=[]                    #  "
matrixc=[]                    #  "
matrixd=[]                    #  "
matrixe=[]                    #  "


def worker(vector):           # FUNCION: Funcion Thread
        red=0
        for w in vector:      # VECTOR: Recorrer Vector
                red+=1        # VARIABLE: Para Contar Palabras
                print w       # DEBUG: Recorrido del vector
        print red             # DEBUG: Total palabras en el vector

with open("dic.log","r") as words:  # ARCHIVO: Abrir Diccionario
        for word in words:          # VECTOR: Recorrer Diccionario
                manywords+=1        # VARIABLE: Sumar palabras que contiene el diccionario
        split=manywords/5           # VARIABLE: Dividir la suma en (5) para 5 Vectores (procesos)

with open("dic.log","r") as wordsb: # ARCHIVO: Abrir de nuevo el diccionario ???
        for wordb in wordsb:        # VECTOR: Recorrer Diccionario
                if conta!=split:    # CONDICION: Si el contador no es igual a la divicion de la suma de todas las palabras
                        conta+=1    # VARAIBLE: Sumar palabras para cada vector (split=manywords/5)
                        matrixa.append(wordb) # VECTOR: Agregar Cada Palabra al Vector
                if contb!=split:
                        contb+=1
                        matrixb.append(wordb)
                if contc!=split:
                        contc+=1
                        matrixc.append(wordb)
                if contd!=split:
                        contd+=1
                        matrixd.append(wordb)
                if conte!=split:
                        conte+=1
                        matrixe.append(wordb)

print manywords, split, conta, contb, contc, contd, conte # DEBUG: Mostrar las Varibles

if True:
    t = threading.Thread(target=worker, args=(matrixa,))  # THREAD: Iniciar proceso con cada Matrix
    t.start()
    t = threading.Thread(target=worker, args=(matrixb,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixc,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixd,))
    t.start()
    t = threading.Thread(target=worker, args=(matrixe,))
    t.start()
