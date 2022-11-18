package dados;

// import java.util.Scanner;

public class Contas {
    private int numero;
    private String nome;
    private int tipo;
    private double saldo;
    private double limite;

    public Contas(int numero, String nome, int tipo, double saldo, double limite) {
        this.numero = numero;
        this.nome = nome;
        this.tipo = tipo;
        this.saldo = saldo;
        this.limite = limite;
    }

    public String toString() {
        String aux = "";
        if (this.tipo == 1) {
            aux =  ("\nConta Corrente"+
                    "\nConta: "+numero+
                    "\nCliente: "+nome+
                    "\nSaldo: "+saldo+
                    "\nLimite: "+limite);
        }

        else if (this.tipo == 2) {
            aux =  ("\nConta Poupança"+
                    "\nConta: "+numero+
                    "\nCliente: "+nome+
                    "\nSaldo: "+saldo+
                    "\nLimite: "+limite);
        }

        return aux;

    }

    public void toSacar(double saque) {
        
        if (saque < saldo){
            this.saldo = saldo - saque;
        }
        else{
            System.out.println("\nSaldo insuficiente!");
        }

    }

    public void toDepositar(double deposito) {
        this.saldo = saldo + deposito;
    }

    public void getExtrato() {
        System.out.println("Saldo: "+saldo);
    }
    
    public void toTransf(double valor, Contas destino) {
        if(valor < this.saldo){
            this.saldo = saldo - valor;
            destino.toDepositar(valor);
        }
        
        else{
            System.out.println("\nSaldo Insuficiente!");
        }
    }

    public double getSaldo(){
        return saldo;
    }

}
