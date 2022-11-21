import java.util.Scanner;

public class Atividade1{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int salario, prestacao;

        System.out.println("Insira o salario: ");
        salario = input.nextInt();

        System.out.println("Insira a prestação: ");
        prestacao = input.nextInt();

        if(prestacao>(0.3*salario)){
            System.out.println("O empréstimo não pode ser realizado");    
        }

        else{
            System.out.println("O emprestimo pode ser realizado");
        }
    }
}