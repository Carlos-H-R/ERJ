package model;

import java.util.ArrayList;

public class Dados{
    private ArrayList<Usuario> usuarios = new ArrayList<Usuario>(0);
    private ArrayList<Medico> medicos = new ArrayList<Medico>(0);

    public Dados(){
        usuarios = new ArrayList<Usuario>(0);
        medicos = new ArrayList<Medico>(0);
    }

    public void adicionaUsuario(Usuario novoUsuario){
        usuarios.add(novoUsuario);
    }

    public void adicionarMedico(Medico novoMedico){
        medicos.add(novoMedico);
    }
}