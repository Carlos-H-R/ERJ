package view;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class MedicoGUI {
    private Stage medicos;

    public MedicoGUI() throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("./MedicoGUI.fxml"));

        Scene scene = new Scene(root);
        
        medicos = new Stage();
        medicos.setScene(scene);
        medicos.show();
    }
}
