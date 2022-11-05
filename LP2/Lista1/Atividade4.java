import java.util.Scanner;

public class Atividade4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in)      ;

        int n, aux, even = 0, odd = 0;

        n = input.nextInt();

        for(int i=0; i<n; i++){
            aux = input.nextInt();
            if((aux%2)==0){even++;}
            else{odd++;}
        }

        System.out.printf("%d impares \n%d pares", odd, even);
    }
}