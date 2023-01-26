package Exercício_1.models;

public class Animal {
    private String nome;
    private float comprimento;
    private int patas;
    private String cor;
    private String ambiente;
    private float velocidade;

    public Animal(String nome, float comprimento, int patas, String cor, String ambiente, float velocidade) {
        this.nome = nome;
        this.comprimento = comprimento;
        this.patas = patas;
        this.cor = cor;
        this.ambiente = ambiente;
        this.velocidade = velocidade;
    
    }
    @Override
    public String toString() {
        return "Animal [nome=" + nome + ", comprimento=" + comprimento + ", patas=" + patas + ", cor=" + cor
                + ", ambiente=" + ambiente + ", velocidade=" + velocidade + "]";
    }

    public String getNome() {
        return nome;
    }
    public float getComprimento() {
        return comprimento;
    }
    public int getpatas() {
        return patas;
    }
    public String getCor() {
        return cor;
    }
    public String getAmbiente() {
        return ambiente;
    }
    public float getVelocidade() {
        return velocidade;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setComprimento(float comprimento) {
        this.comprimento = comprimento;
    }
    public void setpatas(int patas) {
        this.patas = patas;
    }
    public void setCor(String cor) {
        this.cor = cor;
    }
    public void setAmbiente(String ambiente) {
        this.ambiente = ambiente;
    }
    public void setVelocidade(float velocidade) {
        this.velocidade = velocidade;
    }
    
    
}