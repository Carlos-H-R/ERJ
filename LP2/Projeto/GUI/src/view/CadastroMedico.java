package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import main.App;

/*
 * Classe responsável por gerar a tela de novo médico
 */
public class CadastroMedico extends App{
    public CadastroMedico() throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("CadastroMedico.fxml"));

        Scene scene = new Scene(root);
        
        Stage cadastro = new Stage();
        cadastro.setScene(scene);
        cadastro.show();
    }
}
