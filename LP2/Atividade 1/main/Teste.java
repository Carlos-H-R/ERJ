package main;

import dados.Contas;

public class Teste {
    public static void main(String[] args) {

        Contas c2;
        Contas c1;
        c1 = new Contas(1870, "Pedro", 1, 1265.63, 3000);
        c2 = new Contas(1970, "Marcelo", 2, 2944.12, 5000);
        System.out.println(c1);
        System.out.println(c2);

        c1.toSacar(235.11);
        System.out.println("\nSaldo 1 apos saque: "+c1.getSaldo());

        c2.toDepositar(120);
        System.out.println("\nSaldo 2 apos deposito: "+c2.getSaldo());

        c2.toTransf(237.15,c1);
        System.out.println("\nApos a transferencia");
        System.out.println("\nSaldo 1: "+c1.getSaldo());
        System.out.println("\nSaldo 2: "+c2.getSaldo());

    }
}
