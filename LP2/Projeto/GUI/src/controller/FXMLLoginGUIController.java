package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import view.MedicoGUI;

public class FXMLLoginGUIController{
    @FXML private Button limpar;
    @FXML private Button enviar;
    @FXML private TextField login;
    @FXML private PasswordField senha;
    @FXML private Label messageBlank;
    @FXML private Label messageInvalid;
    @FXML private Pane loginPane;

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        limpaCampos();
    }
    
    @FXML protected void handleEntrarButtonAction(ActionEvent event) throws Exception{
        
        /*
         * Caso o login e senha estejam corretos abre a janela com os dados dos medico.
         */
        if (login.getText().toString().equals("Carlitos") && (senha.getText().toString().equals("12345"))){
            messageBlank.setVisible(false);
            messageInvalid.setVisible(false);
            limpaCampos();
            new MedicoGUI();

            Stage stage = (Stage) senha.getScene().getWindow();
            stage.close();
        }

        /*
         * Apresenta mensagem indicando que os campos estão vazios.
         */
        else if (login.getText().isEmpty() && senha.getText().isEmpty()){
            messageInvalid.setVisible(false);
            messageBlank.setVisible(true);
            limpaCampos();
        }

        /*
         * Exibe mensagem caso o usuário ou senha esteja incorreto
         */
        else{
            messageBlank.setVisible(false);
            messageInvalid.setVisible(true);
            limpaCampos();
        }
    }
    
    /* 
     * Limpa os campos 
     */
    protected void limpaCampos(){
        login.clear();
        senha.clear();
        messageBlank.setVisible(false);
        messageInvalid.setVisible(false);
    }
}
