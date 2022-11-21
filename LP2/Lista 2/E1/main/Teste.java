package main;

import formas.Circulo;

public class Teste {
    public static void main(String[] args) {
        
        Circulo c1;
        c1 = new Circulo();
        System.out.println(c1);

        c1.setRaio(3);
        System.out.println("\nNovo raio: "+c1.getRaio());

        c1.setCor("amarelo");
        System.out.println("Nova cor: "+c1.getCor());

        System.out.println("\n"+c1);
    }
}
