import java.util.Scanner;

public class JuegoLucha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Arma espada = new Arma("Espada", 5);
        Arma baston = new Arma("Bastón mágico", 3);

        System.out.print("Nombre del Cazador: ");
        String nombreCazador = scanner.nextLine();
        Personaje cazador = new Cazador(nombreCazador, espada);

        System.out.print("Nombre del Hechicero: ");
        String nombreHechicero = scanner.nextLine();
        Personaje hechicero = new Hechicero(nombreHechicero, baston);

        Personaje[] jugadores = {cazador, hechicero};
        int turno = 0;

        while (cazador.estaVivo() && hechicero.estaVivo()) {
            Personaje actual = jugadores[turno % 2];
            Personaje oponente = jugadores[(turno + 1) % 2];

            System.out.println("\nTurno de " + actual.getNombre() + " (Vida: " + actual.getPuntosDeVida() + ")");
            System.out.print("Presiona 1 para atacar: ");
            String input = scanner.nextLine();

            if (input.equals("1")) {
                actual.atacar(oponente);
                turno++;
            } else {
                System.out.println("Entrada inválida, por favor presiona 1 para atacar.");
            }
        }

        if (cazador.estaVivo()) {
            System.out.println("\n¡" + cazador.getNombre() + " ha ganado!");
        } else {
            System.out.println("\n¡" + hechicero.getNombre() + " ha ganado!");
        }

        scanner.close();
    }
}


