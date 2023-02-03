package main;

import javafx.application.Application;
import javafx.stage.Stage;
import view.CadastroMedico;
import view.CadastroUsuario;
import view.LoginGUI;
import view.MedicoGUI;

public class App extends Application{

    public static void main(String[] args) throws Exception {
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        new LoginGUI();
        new CadastroMedico();
        new CadastroUsuario();
        new MedicoGUI();
    }

}
