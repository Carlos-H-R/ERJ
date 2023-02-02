package main;

import javafx.application.Application;
import javafx.stage.Stage;
// import model.Dados;
import view.LoginGUI;

public class App extends Application{

    public static void main(String[] args) throws Exception {
        // Dados dataBase;
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        new LoginGUI();
    }

}
