package model;

public class Medico {
    private String nome;
    private String crm;
    private String cpf;
    private String telefone;

    public Medico(){}

    public Medico(String nome, String crm, String cpf, String telefone) {
        this.nome = nome;
        this.crm = crm;
        this.cpf = cpf;
        this.telefone = telefone;
    }

    public String getTelefone() {
        return (telefone);
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCrm() {
        return crm;
    }

    public void setCrm(String crm) {
        this.crm = crm;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
}
