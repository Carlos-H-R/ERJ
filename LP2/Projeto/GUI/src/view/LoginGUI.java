package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class LoginGUI{
    private Stage login;

    public LoginGUI() throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("./LoginGUI.fxml"));

        login = new Stage();

        Scene scene = new Scene(root);

        this.login.setScene(scene);
        this.login.show();
    }

}
