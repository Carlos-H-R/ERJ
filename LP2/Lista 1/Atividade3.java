import java.util.Scanner;

public class Atividade3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int maior,aux;
        maior = input.nextInt();
        
        for(int i=0; i<5; i++){
            aux = input.nextInt();
            if(aux>maior){
                maior = aux;
            }
        }

        System.out.printf("O maior é: %d",maior);
    }
}
