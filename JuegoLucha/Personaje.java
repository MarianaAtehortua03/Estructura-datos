public abstract class Personaje {
    protected String nombre;
    protected int puntosDeVida;
    protected Arma arma;

    // Constructor base para cualquier personaje
    public Personaje(String nombre, int puntosDeVida, Arma arma) {
        this.nombre = nombre;
        this.puntosDeVida = puntosDeVida;
        this.arma = arma;
    }

    // Metodos basicos de la clase
    public abstract void atacar(Personaje oponente);

    public void recibirDano(int cantidad) {
        puntosDeVida -= cantidad;
        System.out.println(nombre + " recibe " + cantidad + " puntos de daño. Vida actual: " + puntosDeVida);
    }

    public boolean estaVivo() {
        return puntosDeVida > 0;
    }

    public String getNombre() {
        return nombre;
    }

    public int getPuntosDeVida() {
        return puntosDeVida;
    }
}


