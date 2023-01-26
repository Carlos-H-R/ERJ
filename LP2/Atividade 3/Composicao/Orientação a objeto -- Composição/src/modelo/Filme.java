package modelo;

public class Filme {
    private String titulo;
    private String descricao;
    private Diretor diretor;
    private int duracaoMin;

    public Filme() {}

    public Filme(String titulo, String descricao, int duracaoMin, String nome, int experiencia, String origem){
        this.titulo = titulo;
        this.descricao = descricao;
        this.duracaoMin = duracaoMin;
        this.diretor = new Diretor(nome, experiencia, origem);
    }

    public String toString() {
        return ("\nTítulo: "+titulo+
                "\nDuração: "+duracaoMin+"min"+diretor+
                "\nDescrição do filme: "+descricao);
    }

    public void exibirDuracaoEmHoras() {
        int H = (duracaoMin / 60);
        int m = (duracaoMin % 60);
        
        System.out.println("\nO filme '"+titulo+"' possui "+H+" horas e "+m+" minutos de duração.");
    }

    public Boolean checkFilme(String titulo){
        return (this.titulo.equals(titulo));
    }
    
    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public void setDescricao(String descricao){
        this.descricao = descricao;
    }

    public void setDuracao(int duracaoMin){
        this.duracaoMin = duracaoMin;
    }

    public void setDiretor(String nome, int experiencia, String origem){
        this.diretor = new Diretor(nome, experiencia, origem);
    }

    public String getTitulo(){
        return titulo;
    }

    public String getDescricao(){
        return descricao;
    }

    public int getDuracao(){
        return duracaoMin;
    }

    public Diretor getDiretor(){
        return diretor;
    }
}
