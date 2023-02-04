package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import model.DadosUsuario;
import model.Usuario;

public class FXMLCadastroUsuarioController {
    @FXML protected TextField nome;
    @FXML protected TextField login;
    @FXML protected TextField senha;
    @FXML protected TextField confirmaSenha;
    @FXML protected Label messageBlank;
    @FXML protected Label messageNotEqual;

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        limparCampos();
        messageNotEqual.setVisible(false);
        messageBlank.setVisible(false);
    }

    /*
     * Verifica se os campos estão vazios.
     * Verifica se o campo senha e condirma senha são iguais.
     * Após as verificações positivas gera novo usuario
     */
    @FXML protected void handleCadastrarButtonAction(ActionEvent event){
        try {
            if ((nome.getText().isEmpty()) || (login.getText().isEmpty()) || (senha.getText().isEmpty()) || (confirmaSenha.getText().isEmpty())){
                messageNotEqual.setVisible(false);
                messageBlank.setVisible(true);
            }
            
            else if (senha.equals(confirmaSenha)){
                new DadosUsuario(new Usuario(nome.getText(), login.getText(), senha.getText()));
    
                limparCampos();
                
                Stage stage = (Stage) senha.getScene().getWindow();
                stage.close();
            }
            else{
                messageBlank.setVisible(false);
                messageNotEqual.setVisible(true);
            }
        } catch (NullPointerException e) {
            System.out.println(e);
            messageNotEqual.setVisible(false);
            messageBlank.setVisible(true);
        }
    }
    
    protected void limparCampos(){
        nome.clear();
        login.clear();
        senha.clear();
        confirmaSenha.clear();
    }
}
