package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import model.Usuario;

public class FXMLCadastroUsuarioController {
    @FXML protected TextField nome;
    @FXML protected TextField login;
    @FXML protected TextField senha;
    @FXML protected TextField confimaSenha;

    protected void limparCampos(){
        nome.setText(null);
        login.setText(null);
        senha.setText(null);
        confimaSenha.setText(null);
    }

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        limparCampos();
    }

    @FXML protected void handleCadastrarButtonAction(ActionEvent event){
        if (senha.equals(confimaSenha)){
            // Usuario novoUsuario = 
            new Usuario(nome.getText(), login.getText(), senha.getText());

            // Guarda novo usuario na base de dados

            limparCampos();
            
            // Fecha a janela
        }
        else{
            // Expoe mensagem informando senha incorreta
        }
    }
}
