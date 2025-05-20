import java.util.Random;

public class Cazador extends Personaje {
    private Random random = new Random();

    public Cazador(String nombre, Arma arma) {
        super(nombre, 100, arma);
    }

    @Override
    public void atacar(Personaje oponente) {
        // Impacto base + impactoExtra + variación aleatoria
        int baseImpacto = 10;
        int variacion = random.nextInt(6); // 0 a 5
        int impacto = baseImpacto + arma.getImpactoExtra() + variacion;
        System.out.println(nombre + " ataca con " + arma.getNombre() + " causando " + impacto + " puntos de impacto.");
        oponente.recibirImpacto(impacto);
    }
}

