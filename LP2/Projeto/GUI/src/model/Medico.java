package model;

public class Medico {
    private String nome;
    private long crm;
    private long cpf;
    private long telefone;
    
    public Medico(String nome, long crm, long cpf, long telefone) {
        this.nome = nome;
        this.crm = crm;
        this.cpf = cpf;
        this.telefone = telefone;
    }

    public long getTelefone() {
        return telefone;
    }

    public void setTelefone(long telefone) {
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public long getCrm() {
        return crm;
    }

    public void setCrm(long crm) {
        this.crm = crm;
    }

    public long getCpf() {
        return cpf;
    }

    public void setCpf(long cpf) {
        this.cpf = cpf;
    }
    
}
