import sqlite3

conn = sqlite3.connect('Taller2.db')
cur = conn.cursor()

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad


class Pelicula:
    def __init__(self,  nombre):
        self.nombre = nombre


class Cine:
    def __init__(self,  nombre):
        self.id = None
        self.idP = 1
        self.nombre = nombre
        self.lista_peliculas = []
        self.entradas = []

    def addPelicula(self, pelicula):

        if self.nombre=='CineStark':

            if pelicula.nombre=='Desaparecido':
                pelicula.funciones =['21:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00', '20:00']
            pelicula.id=self.idP
            self.lista_peliculas.append(pelicula)
            self.idP += 1
        elif self.nombre=='CinePlaneta':

            if pelicula.nombre=='Desaparecido':
                pelicula.funciones = ['20:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00']
            elif pelicula.nombre == 'IT':
                pelicula.funciones = ['19:00', '20:30', '22:00']
            elif pelicula.nombre == 'La Hora Final':
                pelicula.funciones = ['21:00']
            pelicula.id = self.idP
            self.lista_peliculas.append(pelicula)
            self.idP += 1


    def listar_peliculas(self):
        print('********************')
        for pelicula in self.lista_peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************')

        return input('Elija pelicula:')

    def listar_funciones(self, pelicula_id):
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in self.lista_peliculas[int(pelicula_id) - 1].funciones:
            print('Función: {}'.format(funcion))

        rsltdo1 = input('Funcion:')
        rsltdo2 = input('Ingrese cantidad de entradas: ')

        return [rsltdo1,rsltdo2]

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


class GrupoCines:
    def __init__(self):
        self.idCine=1
        self.Cines = []

    def getCine(self, idC):
        return self.Cines[idC]

    def addCine(self,cine):
        cine.id = self.idCine
        self.Cines.append(cine)
        self.idCine+=1

    def listarCines(self):
        print('********************')
        print('Lista de cines')
        for cine in self.Cines:
            print("{}: {}".format(cine.id, cine.nombre))
        print('********************')

    def listarCinesInput(self):
        print('********************')
        print('Lista de cines')
        idCine = 0
        for cine in self.Cines:
            idCine += 1
            print("{}: {}".format(idCine, cine.nombre))
        print('********************')
        return input('Primero elija un cine:')


def Menu():
    print('Ingrese la opción que desea realizar')
    print('(1) Listar cines')
    print('(2) Listar cartelera')
    print('(3) Comprar entrada')
    print('(4) Ver entradas')
    print('(5) LimpiarBD')
    print('(0) Salir')
    return input('Opción: ')


def sql():

    cur.execute('''CREATE TABLE IF NOT EXISTS Cines
           (idCine integer, NombreCine text)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Peliculas_X_Cine
           (idCine integer, NombreCine text, idPelicula integer, NombrePelicula text)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Entradas_X_Func
         (idCine integer, idPelicula integer, Funcion text, Entradas text)''')
    conn.commit()

def limpiarBD():
    cur.execute('''DROP TABLE IF EXISTS Cines''')
    cur.execute('''DROP TABLE IF EXISTS Peliculas_X_Cine''')
    cur.execute('''DROP TABLE IF EXISTS Entradas_X_Func''')

def insertarCine(cine):

    cur.execute("INSERT INTO Cines (idCine, NombreCine) VALUES (?,?)", (cine.id, cine.nombre ))

    conn.commit()

    # Insertar Peliculas

    for pelicula in cine.lista_peliculas:
        cur.execute("INSERT INTO Peliculas_X_Cine (idCine , NombreCine , idPelicula , NombrePelicula )"
                  " VALUES (?,?,?,?)", (cine.id, cine.nombre, pelicula.id , pelicula.nombre))

    conn.commit()

def insertarFuncionEntrada(idCine, idPelicula, horarioFuncion, cantidadEntradas):
    cur.execute("INSERT INTO Entradas_X_Func (idCine, idPelicula , Funcion , Entradas )"
              " VALUES (?, ?,?,?)", (idCine, idPelicula, horarioFuncion, cantidadEntradas))

    conn.commit()

def main():
    terminado = False
    while not terminado:
        
        # CineStark
        cineStark = Cine("CineStark")
        cineStark.addPelicula(Pelicula('Desaparecido'))
        cineStark.addPelicula(Pelicula('Deep El Pulpo'))

        # CinePlaneta
        cinePlaneta = Cine("CinePlaneta")
        cinePlaneta.addPelicula(Pelicula('IT'))
        cinePlaneta.addPelicula(Pelicula('La Hora Final'))
        cinePlaneta.addPelicula( Pelicula('Desaparecido'))
        cinePlaneta.addPelicula(Pelicula('Deep El Pulpo'))

        Cines = GrupoCines()
        Cines.addCine(cineStark)
        Cines.addCine(cinePlaneta)

        cur.execute('SELECT * FROM Cines where NombreCine=?',("CineStark",))
        if cur.fetchone() is None:
            insertarCine(cineStark)

        cur.execute('SELECT * FROM Cines where NombreCine=?', ("CinePlaneta",))
        if cur.fetchone() is None:
            insertarCine(cinePlaneta)


        opcion = Menu()

        if opcion == '1':
            Cines.listarCines()
        elif opcion == '2':
            cine =  Cines.listarCinesInput()
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            cine.listar_peliculas()

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')

            cine = Cines.listarCinesInput()
            if cine == '1':
                cine = Cines.getCine(0)
            elif cine == '2':
                cine = Cines.getCine(1)
            else:
                print("Se ingreso un valor no valido")
                break

            pelicula_elegida = cine.listar_peliculas()

            resultadosFuncion = cine.listar_funciones(pelicula_elegida)
            

            codigo_entrada = cine.guardar_entrada(pelicula_elegida, resultadosFuncion[0], resultadosFuncion[0])
            insertarFuncionEntrada(cine.id ,pelicula_elegida,resultadosFuncion[0], resultadosFuncion[1])
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '4':
            print("******Cine     Pelicula    Funcion   Entradas******")
            cur.execute('SELECT B.NombreCine, B.NombrePelicula, A.Funcion, A.Entradas FROM Entradas_X_Func A LEFT JOIN Peliculas_X_Cine B ON A.idCine=B.idCine AND A.idPelicula=B.idPelicula ')
            for row in cur:
                print(row)
        elif opcion == '5':
            limpiarBD()
            sql()
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)


if __name__ == '__main__':
    sql()
    main()
