package main;

import java.util.Scanner;
import java.util.ArrayList;
import modelo.Filme;

public class Gestor{
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            ArrayList<Filme> lista = new ArrayList<Filme>(1);

            int key = -1;

            do{
                System.out.println("\n1 - para cadastrar um filme"+
                                   "\n2 - para buscar um filme"+
                                   "\n3 - para remover um filme"+
                                   "\n4 - para exibir todos os filmes"+
                                   "\n5 - para exibir lista resumida dos filmes"+
                                   "\n0 - para finalizar o programa\n");
                key = Integer.parseInt(input.nextLine());


                if (key == 0){
                    System.out.println("\nPrograma Encerrado!");
                }

                else if (key == 1){
                    try{
                        System.out.print("\nTitulo: ");
                        String titulo = input.nextLine();

                        System.out.print("Duração em minutos: ");
                        int duracao = Integer.parseInt(input.nextLine());

                        System.out.print("Diretor: ");
                        String diretor = input.nextLine();

                        System.out.print("Experiencia do diretor: ");
                        int experiencia = Integer.parseInt(input.nextLine());

                        System.out.print("Local de origem: ");
                        String origem = input.nextLine();
                        
                        System.out.print("Descrição: ");
                        String descricao = input.nextLine();

                        Filme novo = new Filme(titulo, descricao, duracao, diretor, experiencia, origem);

                        lista.add(novo);
                    }catch (NumberFormatException e){
                        System.out.println("Formato de entrada inválido!");
                    }                
}

                else if (key == 2){
                    System.out.print("\nTítulo buscado: ");
                    String buscado = input.nextLine();

                    for (int i=0; i < lista.size(); i++){
                        if (lista.get(i).checkFilme(buscado)){
                            System.out.println(lista.get(i));
                        }
                    }
                }

                else if (key == 3){
                    System.out.print("\nTítulo a ser removido: ");
                    String buscado = input.next();

                    for (int i=0; i < lista.size(); i++){
                        if (lista.get(i).checkFilme(buscado)){
                            lista.remove(i);
                        }
                    }
                }

                else if (key == 4){
                    if (lista.size() == 0)
                        System.out.println("\nLista Vazia!\n");
                    
                    else{
                        for (int i=0; i < lista.size(); i++){
                            System.out.println(lista.get(i));
                        }
                    }
                }

                else if (key == 5){
                    if (lista.size() == 0)
                        System.out.println("\nLista Vazia!\n");
                    
                    else{
                        for (int i=0; i < lista.size(); i++){
                            lista.get(i).exibirDuracaoEmHoras();
                        }
                    }
                }

            } while (key != 0);
        }
    }
}
