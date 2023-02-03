package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class CadastroMedico {
    private Stage cadastro;

    public CadastroMedico() throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("CadastroMedico.fxml"));

        Scene scene = new Scene(root);
        
        cadastro = new Stage();
        cadastro.setScene(scene);
        cadastro.show();
    }
}
