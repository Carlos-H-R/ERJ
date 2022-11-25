package dados;

public class Paciente {
    private long codigo;
    private String nome;
    private long cpf;
    private long telefone;

    public Paciente(long codigo, String nome, long cpf, long telefone){
        this.codigo = codigo;
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
    }

    public String toString(){
        return ("\n"+
                "\nCodigo: "+codigo+
                "\nPaciente: "+nome+
                "\nCPF: "+cpf+
                "\nTelefone: "+telefone+
                "\n");
    }

    public boolean checaCodigo(long codigo){
        if (this.codigo == codigo){
            return true;
        }
        else{
            return false;
        }
    }

    public void setCodigo(long codigo){
        this.codigo = codigo;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setCPF(long cpf){
        this.cpf = cpf;
    }

    public void setTelefone(long telefone){
        this.telefone = telefone;
    }

    public long getCodigo(){
        return codigo;
    }

    public String getNome(){
        return nome;
    }

    public long getCPF(){
        return cpf;
    }

    public long getTelefone(){
        return telefone;
    }
    
}
