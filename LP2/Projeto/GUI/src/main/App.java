package main;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application{
    public static void main(String[] args) throws Exception {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("Tela de login.fxml"));
        Parent root = fxmlLoader.load();
        Scene telaLogin = new Scene(root);

        primaryStage.setTitle("Login de Usuário");
        primaryStage.setScene(telaLogin);
        primaryStage.show();
    }
}
