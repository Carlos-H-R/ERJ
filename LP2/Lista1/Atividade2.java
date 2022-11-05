import java.util.Scanner;

public class Atividade2 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float media = 0;
        int b;
        
        for(int a=0;a<10;a++){
            b = input.nextInt();
            media += b;
        }

        media = media/10;
        System.out.printf("Media: %f",media);
    }
}