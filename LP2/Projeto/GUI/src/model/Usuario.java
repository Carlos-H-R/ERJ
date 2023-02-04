package model;

public class Usuario {
    protected String nome;
    protected String usuario;
    protected String senha;
    
    public Usuario(String nome, String usuario, String senha) {
        this.nome = nome;
        this.usuario = usuario;
        this.senha = senha;
    }
    
    /** 
     * @return String
     */
    public String getUsuario() {
        return usuario;
    }
    
    /** 
     * @param usuario
     */
    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }
    
    /** 
     * @return String
     */
    public String getSenha() {
        return senha;
    }
    
    /** 
     * @param senha
     */
    public void setSenha(String senha) {
        this.senha = senha;
    }

    
}
