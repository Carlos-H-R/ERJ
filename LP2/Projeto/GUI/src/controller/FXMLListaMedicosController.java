package controller;

import java.io.FileReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;
import model.Medico;
import view.CadastroMedico;
import view.CadastroUsuario;
import view.MedicoGUI;

public class FXMLListaMedicosController implements Initializable{
    @FXML protected TableView<Medico> table;
    @FXML protected TableColumn<Medico,String> medico;
    @FXML protected TableColumn<Medico,String> crm;
    @FXML protected TableColumn<Medico,String> cpf;
    @FXML protected TableColumn<Medico,String> telefone;

    ObservableList<Medico> list = FXCollections.observableArrayList(new Medico());
    
    
    /** 
     * @param location
     * @param resources
     */
    /*
     * Realiza a leitura da base de dados dos medicos e cria as celulas para acomodar os dados.
     */
    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println(location);
        System.out.println(resources);

        medico.setCellValueFactory(new PropertyValueFactory<Medico,String>("nome"));
        crm.setCellValueFactory(new PropertyValueFactory<Medico,String>("crm"));
        cpf.setCellValueFactory(new PropertyValueFactory<Medico,String>("cpf"));
        telefone.setCellValueFactory(new PropertyValueFactory<Medico,String>("telefone"));

        try {
            FileReader fileReader = new FileReader("DadosMedicos.json");
            JSONParser jsonParser = new JSONParser();

            JSONObject jsonObject = (JSONObject) jsonParser.parse(fileReader);

            ArrayList<Medico> arrayList = new ArrayList<Medico>(0);

            var test = jsonObject.keySet();
            for (Object i : test){
                JSONObject data;
                data = (JSONObject) jsonObject.get(i.toString());
                arrayList.add(new Medico(data.get("nome").toString(), data.get("crm").toString(), data.get("cpf").toString(), data.get("telefone").toString()));
            }

            ObservableList<Medico> dados = FXCollections.observableArrayList(arrayList);

            table.setItems(dados);
            table.refresh();

        }catch(Exception e) {
            System.out.println(e);
        }
    }

    /*
     * Reinicia a tela e atualiza os dados.
     */
    @FXML protected void handleAtualizar(ActionEvent event) throws Exception{
        new MedicoGUI();
        
        Stage stage = (Stage) table.getScene().getWindow();
        stage.close();
    }
    
    /*
     * Gera janela para cadastrar novo medico
     */
    @FXML protected void handleCadastrar(ActionEvent event) throws Exception{
        new CadastroMedico();
    }

    /*
     * Gera janela para cadastrar novo usuario
     */
    @FXML protected void handleCadastraUsuario() throws Exception{
        new CadastroUsuario();
    }

}
