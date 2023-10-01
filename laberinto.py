import os
import readchar


class Laberinto:

    def __init__(self):
        self.nombre_jugador = input("Por favor, introduce tu nombre: ")
        print(f"\n¡Hola, {self.nombre_jugador}! Bienvenido al juego del laberinto.\n")
        self._inicializar_laberinto()
        self.posicion_jugador = self._encontrar_jugador()

    def _inicializar_laberinto(self):
        """Define el laberinto inicial."""
        self.laberinto = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", "#", "#", ".", "#", "#", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", ".", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", "#", "#", "#", "#"],
            ["#", ".", "#", "#", ".", ".", "#", "#", "#"],
            ["#", ".", "#", "#", "#", ".", ".", "#", "#"],
            ["#", ".", "#", "#", "#", ".", ".", "#", "#"],
            ["#", ".", ".", ".", "#", "#", ".", "#", "#"],
            ["#", ".", "#", ".", "#", "#", ".", ".", "#"],
            ["#", ".", "#", ".", ".", "#", "#", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", ".", "E"]

        ]

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

    def fin_del_juego(self, mensaje):
        """Maneja el fin del juego, mostrando un mensaje y pregunta si se desea reiniciar."""
        print(mensaje)
        decision = input(f"{self.nombre_jugador}, ¿quieres jugar de nuevo? (Sí/No) (y/n): ").lower()
        if decision == "s" or decision == "si" or decision == "y":
            self._inicializar_laberinto()
            self.posicion_jugador = self._encontrar_jugador()
            self.jugar()
        else:
            print(f"\n ¡ Gracias por jugar, {self.nombre_jugador} ! Hasta pronto.")
            exit()

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
            self.fin_del_juego("¡Felicidades! Has ganado.")
        elif self.laberinto[nuevo_x][nuevo_y] == "#":
            self.fin_del_juego("\n¡Game Over! Has tocado una pared.")

        # Si es un espacio vacío, mover al jugador
        if self.laberinto[nuevo_x][nuevo_y] == ".":
            self.laberinto[x][y], self.laberinto[nuevo_x][nuevo_y] = ".", "P"
            self.posicion_jugador = (nuevo_x, nuevo_y)
            self.mostrar_laberinto()

    def jugar(self):
        """Ejecuta el bucle principal del juego."""
        self.mostrar_laberinto()
        print("Mueve con las teclas (w a s d) o 'e' para finalizar.")
        while True:
            movimiento = readchar.readkey()

            # Mapea las teclas w, a, s, d a las direcciones
            direcciones = {'w': '↑', 's': '↓', 'a': '←', 'd': '→'}

            if movimiento in direcciones:
                self.mover(direcciones[movimiento])
            elif movimiento == 'e':  # Usamos 'e' para salir
                print("\n¡Gracias por jugar! Hasta pronto.")
                break
            else:
                print("\nTecla no válida. Usa w, a, s, d para mover o 'e' para salir.")
