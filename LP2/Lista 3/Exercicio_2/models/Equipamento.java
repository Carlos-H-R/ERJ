package Exercicio_2.models;

public class Equipamento {
    private String nome;
    protected Boolean ligado;

    public Equipamento(String nome){
        this.nome = nome;
        ligado = false;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void liga(){
        ligado = true;
    }

    public void desliga(){
        ligado = false;
    }
}
