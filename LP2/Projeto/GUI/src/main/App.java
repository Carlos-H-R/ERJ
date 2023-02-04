package main;

import javafx.application.Application;
import javafx.stage.Stage;
import view.LoginGUI;

public class App extends Application{
    private static Stage stg;

    public static void main(String[] args) throws Exception {
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        stg = stage;
        stage.setResizable(false);
        new LoginGUI(stg);
    }
}
