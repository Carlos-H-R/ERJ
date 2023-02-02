package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class FXMLLoginGUIController {
    @FXML private TextField login;
    @FXML private TextField senha;

    @FXML protected void handleLimparButtonAction(ActionEvent event){
        login.setText(null);
        senha.setText(null);
    }

    @FXML protected void handleEntrarButtonAction(ActionEvent event){
        
    }
}
