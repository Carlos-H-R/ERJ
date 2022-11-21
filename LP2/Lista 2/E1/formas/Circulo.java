package formas;
import java.lang.Math;

public class Circulo {
    public double raio;
    public String cor;

    public Circulo(){
        this.raio = 1;
        this.cor = "vermelho";
    }

    public void setRaio(double raio){
        this.raio = raio;
    }

    public double getRaio(){
        return raio;
    }

    public void setCor(String cor){
        this.cor = cor;
    }

    public String getCor(){
        return cor;
    }

    public double getPerimetro(){
        return (2 * Math.PI * raio);
    }

    public double getArea(){
        return (Math.PI * Math.pow(raio, 2));
    }

    public String toString(){
        return ("Círculo "+cor+
                "\nRaio: "+raio+
                "\nÁrea: "+getArea());
    }
}
