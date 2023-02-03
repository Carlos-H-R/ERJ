package model;

import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class DadosMedicos {
    Medico novoMedico;
    
    @SuppressWarnings("unchecked")
    public DadosMedicos(Medico novoMedico){
        HashMap<String,String> dados = new HashMap<String,String>();
        dados.put("nome",novoMedico.getNome());
        dados.put("crm",novoMedico.getCrm());
        dados.put("cpf",novoMedico.getCpf());
        dados.put("telefone",novoMedico.getTelefone());
        
        JSONObject medicosJson = new JSONObject(dados);

        JSONObject baseDeDados;

        try {
            FileReader fileReader = new FileReader("DadosMedicos.json");
            
            JSONParser jsonParser = new JSONParser();
            Object obj = jsonParser.parse(fileReader);
            baseDeDados = (JSONObject) obj;

            baseDeDados.put(novoMedico.getNome(),medicosJson);
            
        } catch (Exception e) {
            baseDeDados = new JSONObject();
            baseDeDados.put(novoMedico.getNome(),medicosJson);
        }

        try {
            FileWriter file = new FileWriter("DadosMedicos.json");
            file.write(baseDeDados.toJSONString());
            file.flush();
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
