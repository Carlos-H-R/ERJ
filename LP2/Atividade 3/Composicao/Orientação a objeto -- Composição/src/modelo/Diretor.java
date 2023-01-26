package modelo;

public class Diretor {
    private String nome;
    private int experiencia;
    private String origem;

    public Diretor(){

    }

    public Diretor(String nome, int experiencia, String origem){
        this.nome = nome;
        this.experiencia = experiencia;
        this.origem = origem;
    }

    public String toString(){
        return ("\nDiretor: "+nome+
                "\n     Experiencia: "+experiencia+" anos"+
                "\n     Origem do diretor: "+origem);
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setExperiencia(int experiencia){
        this.experiencia = experiencia;
    }

    public void setOrigem(String origem){
        this.origem = origem;
    }

    public String getNome(){
        return nome;
    }

    public int getExperiencia(){
        return experiencia;
    }

    public String getOrigem(){
        return origem;
    }
}
