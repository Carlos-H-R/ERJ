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
                                   "\n0 - para finalizar o programa");
                key = input.nextInt();

                if (key == 0){
                    System.out.println("\nPrograma Encerrado!");
                }

                else if (key == 1){
                    System.out.print("Codigo: ");
                    long codigo = input.nextLong();

                    System.out.print("Titulo: ");
                    String titulo = input.next();

                    System.out.print("Gênero: ");
                    String genero = input.next();

                    System.out.print("Ano: ");
                    int ano = input.nextInt();

                    System.out.print("Diretor: ");
                    String diretor = input.next();

                    System.out.print("Duração: ");
                    int duracao = input.nextInt();

                    Filme novo = new Filme(codigo,titulo,genero,ano,diretor,duracao);

                    lista.add(novo);

                }

                else if (key == 2){
                    System.out.print("\nTítulo buscado: ");
                    String buscado = input.next();

                    for (int i=0; i < lista.size(); i++){
                        if (lista.get(i).comparaFilme(buscado)){
                            System.out.println(lista.get(i));
                        }
                    }
                }

                else if (key == 3){
                    System.out.print("\nTítulo a ser removido: ");
                    String buscado = input.next();

                    for (int i=0; i < lista.size(); i++){
                        if (lista.get(i).comparaFilme(buscado)){
                            lista.remove(i);
                        }
                    }
                }

                else if (key == 4){
                    for (int i=0; i < lista.size(); i++){
                        System.out.println(lista.get(i));
                    }
                }

            } while (key != 0);
        }
    }
}
