package controller;

import java.io.FileReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

public class FXMLLoginGUIController {
    // protected Boolean Autenticado;
    @FXML private TextField login;
    @FXML private PasswordField senha;

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        limpaCampos();
    }
    
    @FXML protected void handleEntrarButtonAction(ActionEvent event){
        try {
            FileReader fileReader = new FileReader("DadosUsuario.json");
            JSONParser jsonParser = new JSONParser();

            Object object = jsonParser.parse(fileReader);

            JSONObject userList = (JSONObject) object;

            Object dadovalidacao = userList.get("Carlitos");
            System.out.println(dadovalidacao);
            // JSONObject dadoValidacao = (JSONObject) userList.get("Carlitos");
            // String senha = (String) dadoValidacao.get("senha");

            // if(autentica(senha)){
            //     System.out.println("work bitch");
            // }

            // else{
            //     System.out.println("shit");
            // }

        } catch (Exception e) {}
    }
    
    protected void limpaCampos(){
        login.setText(null);
        senha.setText(null);
    }

    protected Boolean autentica(String usuario){
        Boolean result = senha.equals(senha) ? true : false;
        return result;
    }
}
