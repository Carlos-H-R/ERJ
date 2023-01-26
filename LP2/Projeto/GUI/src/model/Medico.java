package model;

public class Medico {
    private String nome;
    private long crm;
    private long cpf;

    public Medico(String nome, long crm, long cpf) {
        this.nome = nome;
        this.crm = crm;
        this.cpf = cpf;
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
