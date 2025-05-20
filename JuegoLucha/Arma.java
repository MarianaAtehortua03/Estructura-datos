public class Arma {
    private String nombre;
    private int impactoExtra;

    public Arma(String nombre, int impactoExtra) {
        this.nombre = nombre;
        this.impactoExtra = impactoExtra;
    }

    public String getNombre() {
        return nombre;
    }

    public int getImpactoExtra() {
        return impactoExtra;
    }
}

