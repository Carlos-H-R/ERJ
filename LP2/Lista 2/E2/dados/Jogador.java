package E2.dados;

import java.lang.Math;

public class Jogador {
    private String nome;
    private String nacionalidade;
    private String posicao;
    private float altura;
    private float peso;

    public Jogador(String nome, String nacionalidade, String posicao, float altura, float peso){
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.posicao = posicao;
        this.altura = altura;
        this.peso = peso;
    }

    public String toString(){
        return ("\n"+
                "\nNome: "+nome+
                "\nNacionalidade: "+nacionalidade+
                "\nPosição: "+posicao+
                "\nAltura: "+altura+"m"+
                "\nPeso: "+peso+"Kg");
    }

    public double showIMC(){
        double imc;
        imc = peso/Math.pow(altura, 2);
        return imc;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setPosicao(String posicao){
        this.posicao = posicao;
    }

    public void setNacionalidade(String nacionalidade){
        this.nacionalidade = nacionalidade;
    }

    public void setAltura(float altura){
        this.altura = altura;
    }

    public void setPeso(float peso){
        this.peso = peso;
    }

    public String getNome(){
        return nome;
    }

    public String getNacionalidade(){
        return nacionalidade;
    }

    public String getPosicao(){
        return posicao;
    }

    public float getAltura(){
        return altura;
    }

    public float getPeso(){
        return peso;
    }

}
