package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class CadastroUsuario {
    private Stage cadastro;

    public CadastroUsuario() throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("CadastroMedico.fxml"));

        cadastro = new Stage();

        Scene scene = new Scene(root);

        cadastro.setScene(scene);
        cadastro.show();
    }
}
