
import os 

class pelicula:
    def_init_(self,nombre,genero,año,director):
       self.nombre = nombre
       self.genero = genero
       self.año = año
       self.director = director
    

class catalogo_peliculas:
    def _init_(self,nombre):
        self.nombre = nombre
        self.peliculas = []

    def mostrar_menu(self):
        print("\n--- Menu de opciones---")
        print("1.Agregar una pelicula")
        print("2. Mostrar peliculas")
        print("3.Eliminar catalogo de peliculas")
        print("4.Salir")

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    class catalogo_peliculas:
        def __init__(self, nombre):
            self.nombre = nombre
            self.peliculas = []

    def mostrar_menu(self):
        print("\n--- Menú de opciones:---")
        print("1. Agregar una película")
        print("2. Mostrar películas")
        print("3.Eliminar catalogo de peliculas")
        print("4.salir")

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def listar_peliculas(self):
        if not self.peliculas:
            print("No hay películas en el catálogo.")
        else:
            for pelicula in self.peliculas:
                print(f"Título: {pelicula.nombre}, Director: {pelicula.director}, Año: {pelicula.año}, Género: {pelicula.genero}")

    def eliminar_catalogo(self):
        print("Catálogo de películas eliminado.")


    def main():
    nombre_catalogo= input("Ingrese el nombre del catalogo de la pelicula ")
    catalogo = catalogo_peliculas(nombre_catalogo)

    while True:
        catalogo.mostrar_menu()
        opcion = input("Seleccionar una opcion: ")

        if opcion == "1":
          titulo = input("ingresa el titulo de la pelicula:")
          director = input("ingresa el director de la pelicula:")
          año = input("ingresa el año de estreno de la pelicula:")
          genero = input("ingresa el género de la pelicula:")
          pelicula_nueva = pelicula(titulo,director,año,genero)
          catalogo.agregar_pelicula(pelicula_nueva)
        elif opcion == "2":
          catalogo.listar_peliculas()
        elif opcion == "3":
          catalogo.eliminar_catalogo()
        elif opcion == "4":
          print("Saliendo. Gracias por usar el programa")
          break
        else:
          print("Opcion no valida. Por favor, intente de nuevo")


if __name__ == "__main__":
    main()

 