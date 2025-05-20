import java.util.Random;

public class Hechicero extends Personaje {
    private Random random = new Random();

    public Hechicero(String nombre, Arma arma) {
        super(nombre, 80, arma);
    }

    @Override
    public void atacar(Personaje oponente) {
        int baseImpacto = 8;
        int variacion = random.nextInt(6);
        int impacto = baseImpacto + arma.getImpactoExtra() + variacion;
        System.out.println(nombre + " lanza un hechizo con " + arma.getNombre() + " causando " + impacto + " puntos de impacto.");
        oponente.recibirImpacto(impacto);
    }
}
