package main;

import javafx.application.Application;
import javafx.stage.Stage;
import view.CadastroUsuario;
import view.LoginGUI;

public class App extends Application{

    public static void main(String[] args) throws Exception {
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        LoginGUI login = new LoginGUI();
        CadastroUsuario cadastroUsuario = new CadastroUsuario();
    }

}
