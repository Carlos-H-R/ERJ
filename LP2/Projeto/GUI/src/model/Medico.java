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

    
    /** 
     * @return String
     */
    public String getTelefone() {
        return (telefone);
    }

    
    /** 
     * @param telefone
     */
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    
    /** 
     * @return String
     */
    public String getNome() {
        return nome;
    }

    
    /** 
     * @param nome
     */
    public void setNome(String nome) {
        this.nome = nome;
    }

    
    /** 
     * @return String
     */
    public String getCrm() {
        return crm;
    }

    
    /** 
     * @param crm
     */
    public void setCrm(String crm) {
        this.crm = crm;
    }

    
    /** 
     * @return String
     */
    public String getCpf() {
        return cpf;
    }

    
    /** 
     * @param cpf
     */
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
}
