package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

/*
 * Classe responsável por gerar a tela de login
 */
public class LoginGUI{
    public LoginGUI(Stage login) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("./LoginGUI.fxml"));

        Scene scene = new Scene(root);
        
        login = new Stage();
        login.setScene(scene);
        login.show();
    }

}
