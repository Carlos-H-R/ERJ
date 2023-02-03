package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import model.DadosMedicos;
import model.Medico;

/*
 * Classe que extrai os dados dos campos preenchido
 */
public class FXMLCadastroMedicoController {
    @FXML private TextField crm;
    @FXML private TextField nome;
    @FXML private TextField cpf;
    @FXML private TextField telefone;


    protected void limparCampos(){
        crm.setText(null);
        nome.setText(null);
        cpf.setText(null);
        telefone.setText(null);
    }

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        limparCampos();
    }

    /*
     * Ao acionar o botão Enviar os campos são recolhidos,
     * É criado o objeto novoMedico e em seguida chamado  o construtor da classe DadosMedicos
     */
    @FXML protected void handleEnviarButtonAction(ActionEvent event){
        if (crm.equals(null) || nome.equals(null) || cpf.equals(null) || telefone.equals(null)){}

        else{
            Medico novoMedico = new Medico(
                nome.getText(), 
                Long.parseLong(crm.getText()), 
                Long.parseLong(cpf.getText()),
                Long.parseLong(telefone.getText()));

            new DadosMedicos(novoMedico);
            limparCampos();
        }
    }
}
