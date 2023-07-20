# Simulador de Juego de Blackjack con agente inteligente mediante Arboles de Busqueda de Monte Carlo

Este es un simulador para el popular juego de Casino "Blackjack"
con inteligencia articial incluida para sugerirle al jugador que jugada es mejor realizar
basado en el algoritmo en arboles de busqueda de Monte Carlo

Cuenta con un cliente llamado black_jack_simulator.py

    Uso: python blackjack_simulator.py [iteration_number]
    argumentos:   iteration_number: Numero de Iteraciones a correr en cada simulacion

# Descripcion del juego

El blackjack, también llamado veintiuno, es un juego de cartas, propio de los casinos con una o más barajas inglesas de 52 cartas sin los comodines, que consiste en sumar un valor lo más próximo a 21 pero sin pasarse. En un casino cada jugador de la mesa juega únicamente contra el crupier, intentando conseguir una mejor jugada que este. El crupier está sujeto a reglas fijas que le impiden tomar decisiones sobre el juego. Por ejemplo, está obligado a pedir carta siempre que su puntuación sume 16 o menos, y obligado a plantarse si suma 17 o más. Las cartas numéricas suman su valor, las figuras suman 10 y el as vale 11 o 1, a elección del jugador. En el caso del crupier, los ases valen 11 mientras no se pase de 21, y 1 en caso contrario. La mejor jugada es conseguir 21 con solo dos cartas, esto es con un As más carta de valor 10. Esta jugada se conoce como Blackjack o 21 natural. Un blackjack gana sobre un 21 conseguido con más de dos cartas.

Se juega en una mesa semicircular con capacidad normalmente de 4 a 7 jugadores, cada uno de los cuales dispone de un casillero marcado en el tapete para realizar su apuesta antes de recibir las 2 cartas iniciales de cada mano. Esta apuesta debe ser realizada en cada mano, necesariamente antes de que se ponga en juego la primera carta.


# Requerimientos
Se requiere python 3 e instalar los requerimientos en el archivo requirements.txt anexo en este repositorio


# Creditos:

Eros Cedeño 16-10216
Leonel Guerrero 18-10638