package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

/*
 * Classe responsável por gerar a tela de cadastro de novo usuário
 */
public class CadastroUsuario {
    private Stage cadastro;

    public CadastroUsuario() throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("./CadastroUsuario.fxml"));

        Scene scene = new Scene(root);
        
        cadastro = new Stage();
        cadastro.setScene(scene);
        cadastro.show();
    }
}
