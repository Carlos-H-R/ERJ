package E2.main;

import java.util.Scanner;
import java.util.ArrayList;
import E2.dados.Jogador;

public class Time {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            ArrayList<Jogador> time = new ArrayList<Jogador>();

            int key = -1;

            do{
                try {
                    System.out.println( "\n1 - para registrar um jogador"+
                                        "\n0 - para encerrar");
                    key = input.nextInt();

                    } catch (Exception InputMissmatchException) {
                        System.out.println("Opção inválida! \nA entrada deve ser um número inteiro!\n");
                    }
                                        
                    switch (key) {
                        case 1:
                            if (time.size() < 3){
                                try{
                                    System.out.print("\nNome: ");
                                    String nome = input.next();
                                    
                                    System.out.print("Nacionalidade: ");
                                    String nacionalidade = input.next();
                                    
                                    System.out.print("Posição: ");
                                    String posicao = input.next();
                                    
                                    System.out.print("Altura: ");
                                    float altura = input.nextFloat();
                                    
                                    System.out.print("Peso: ");
                                    float peso = input.nextFloat();
                                    
                                    Jogador novo = new Jogador(nome, nacionalidade, posicao, altura, peso);
                                    
                                    time.add(novo);
                                    
                                } catch (Exception InputMissmatchException){
                                    System.out.println("Valor deve ser do tipo float!");
                                    input.nextLine();
                                }
                            }

                            else{
                                System.out.println("\nO time está cheio, não é possível adicionar mais jogadores!");
                            }

                            break;

                        case 0:
                            if (time.get(0) != null){
                                for (int i = 0; i < time.size(); i++){
                                    System.out.println(time.get(i));
                                }
                            }

                            System.out.println("\nEncerrado!");
                            break;
                    
                        default:
                            System.out.println("Opção inválida!");
                            break;
                    }
            }while (key != 0);
        }
    }
}
