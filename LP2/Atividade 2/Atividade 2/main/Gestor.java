//Implementado com vetor de tamanho estático (50 posições)

package main;

import dados.CadastroPaciente;

public class Gestor {
    public static void main(String[] args) {
        CadastroPaciente menu = new CadastroPaciente();
        
        menu.options();
    }
}
