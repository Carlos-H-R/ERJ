package controller;

import java.io.FileReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;

@SuppressWarnings("unchecked")
public class FXMLListaMedicosController {
    @FXML protected TableColumn medico;
    @FXML protected TableColumn crm;
    @FXML protected TableColumn cpf;
    @FXML protected TableColumn telefone;

    @FXML protected void handleListUpdate(){
        try {
            FileReader fileReader = new FileReader("DadosMedicos.json");
            
            JSONParser jsonParser = new JSONParser();
            Object obj = jsonParser.parse(fileReader);

            JSONObject baseDeDados = (JSONObject) obj;

            baseDeDados.keySet().forEach(keyStr ->
            {
                JSONObject keyvalue = (JSONObject) baseDeDados.get(keyStr);
                medico.setText((String) keyvalue.get("nome"));
                cpf.setText((String) keyvalue.get("cpf"));
                crm.setText((String) keyvalue.get("crm"));;
                telefone.setText((String) keyvalue.get("telefone"));;
            });
            
        } catch (Exception e) {
        
        }
    }

    @FXML protected void handleNovoButtonAction(ActionEvent event){

    }
}
