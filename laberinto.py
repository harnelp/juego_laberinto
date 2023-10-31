import os
import readchar

class Laberinto:

    def __init__(self, nivel):
        self.nivel = nivel
        self._cargar_laberinto()
        self.posicion_jugador = self._encontrar_jugador()

    def _cargar_laberinto(self):
        """Carga el laberinto desde un archivo de texto."""
        nombre_archivo = f"niveles/map{self.nivel}.txt"
        with open(nombre_archivo, 'r') as archivo:
            self.laberinto = [list(linea.strip()) for linea in archivo.readlines()]

    def _encontrar_jugador(self):
        """Encuentra y devuelve la posición del jugador en el laberinto."""
        for i, fila in enumerate(self.laberinto):
            for j, celda in enumerate(fila):
                if celda == "P":
                    return (i, j)

    def mostrar_laberinto(self):
        """Limpia la pantalla y muestra el estado actual del laberinto."""
        os.system('clear' if os.name == 'posix' else 'cls')
        for fila in self.laberinto:
            print(" ".join(fila))
        print("\n")

    def mover(self, direccion):
        """Intenta mover al jugador en la dirección dada."""
        x, y = self.posicion_jugador

        # Determinar la nueva posición según la dirección
        if direccion == "↑":
            nuevo_x, nuevo_y = x-1, y
        elif direccion == "↓":
            nuevo_x, nuevo_y = x+1, y
        elif direccion == "←":
            nuevo_x, nuevo_y = x, y-1
        elif direccion == "→":
            nuevo_x, nuevo_y = x, y+1
        else:
            return

        # Verificar la meta o pared
        if self.laberinto[nuevo_x][nuevo_y] == "E":
            self.mostrar_laberinto()
            return True  # Indicar que se ha alcanzado el final
        elif self.laberinto[nuevo_x][nuevo_y] == "#":
            self.mostrar_laberinto()
            return False  # Indicar que se ha tocado una pared

        # Si es un espacio vacío, mover al jugador
        if self.laberinto[nuevo_x][nuevo_y] == ".":
            self.laberinto[x][y], self.laberinto[nuevo_x][nuevo_y] = ".", "P"
            self.posicion_jugador = (nuevo_x, nuevo_y)
            self.mostrar_laberinto()

        return None  # Indicar que el juego continúa

    def iniciar_juego(self):
        self.nombre_jugador = input("Por favor, introduce tu nombre: ")
        print(f"\n¡Hola, {self.nombre_jugador}! Bienvenido al juego del laberinto.\n")
        
        nivel_actual = 1
        max_niveles = 5  # Suponiendo que tienes 5 niveles

        while nivel_actual <= max_niveles:
            juego = Laberinto(nivel_actual)
            juego.mostrar_laberinto()
            print("Mueve con las teclas (w a s d) o 'e' para finalizar.")

            while True:
                movimiento = readchar.readkey()

                # Mapea las teclas w, a, s, d a las direcciones
                direcciones = {'w': '↑', 's': '↓', 'a': '←', 'd': '→'}

                if movimiento in direcciones:
                    resultado = juego.mover(direcciones[movimiento])
                    if resultado is not None:
                        break
                elif movimiento == 'e':  # Usamos 'e' para salir
                    print("\n¡Gracias por jugar! Hasta pronto.")
                    return
                else:
                    print("\nTecla no válida. Usa w, a, s, d para mover o 'e' para salir.")

            if resultado:
                print("¡Felicidades! Has completado este nivel.")
                nivel_actual += 1
            else:
                print("\n¡Game Over! Has tocado una pared.")
                decision = input(f"{self.nombre_jugador}, ¿quieres intentar de nuevo este nivel? (y/n): ").lower()
                if decision != "s" and decision != "y":
                    print(f"\n¡Gracias por jugar, {self.nombre_jugador}! Hasta pronto.")
                    return

        print("¡Felicidades! Has completado todos los niveles.")
