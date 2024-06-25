
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

  def guardar_peliculas(self):
        with open("catalogo.txt","w")as archivo:
          for pelicula in self.peliculas:
              archivo.write(f"{pelicula.nombre},{pelicula.director},{pelicula.año}\n")


    def listar_peliculas(self):
        if not self.peliculas:
            print("No hay películas en el catálogo.")
        else:
            for pelicula in self.peliculas:
                print(f"Título: {pelicula.nombre}, Director: {pelicula.director}, Año: {pelicula.año}")

    def eliminar_catalogo(self):
        print("Catálogo de películas eliminado.")

    



 

 
