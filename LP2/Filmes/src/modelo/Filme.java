package modelo;

public class Filme{
    private long codigo;
    private String titulo;
    private String genero;
    private int ano;
    private String diretor;
    private int duracao;
    
    public Filme() {
    	this.codigo = 0;
        this.titulo = " ";
        this.genero = " ";
        this.ano = 2000;
        this.diretor = " ";
        this.duracao = 0;
    }

    public Filme(long codigo, String titulo, String genero, int ano, String diretor, int duracao){
        this.codigo = codigo;
        this.titulo = titulo;
        this.genero = genero;
        this.ano = ano;
        this.diretor = diretor;
        this.duracao = duracao;
    }

    public Filme(long codigo, String titulo, String genero, int ano, String diretor){
        this.codigo = codigo;
        this.titulo = titulo;
        this.genero = genero;
        this.ano = ano;
        this.diretor = diretor;
    }

    public String toString(){
        return ("\nCódigo: "+codigo+
                "\nTítulo: "+titulo+
                "\nGênero: "+genero+
                "\nAno: "+ano+
                "\nDiretor: "+diretor+
                "\nDuração: "+duracao);
    }

    public Boolean comparaFilme(String nome){
        if (nome.equals(this.titulo)){
            return true;
        }

        else{
            return false;
        }
    }

    public void setCodigo(long codigo){
        this.codigo = codigo;
    }

    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public void setGenero(String genero){
        this.genero = genero;
    }

    public void setAno(int ano){
        this.ano = ano;
    }

    public void setDiretor(String diretor){
        this.diretor = diretor;
    }

    public void setDuracao(int duracao){
        this.duracao = duracao;
    }

    public long getCodigo(){
        return codigo;
    }

    public String getTitulo(){
        return titulo;
    }

    public String getGenero(){
        return genero;
    }

    public int getAno(){
        return ano;
    }

    public String getDiretor(){
        return diretor;
    }

    public int getDuracao(){
        return duracao;
    }
}
