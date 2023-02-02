package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class FXMLCadastroMedicoController {
    @FXML private TextField crm;
    @FXML private TextField nome;
    @FXML private TextField cpf;
    @FXML private TextField telefone;

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        crm.setText(null);
        nome.setText(null);
        cpf.setText(null);
        telefone.setText(null);
    }

    @FXML protected void handleEnviarButtonAction(ActionEvent event){
        
    }
}
