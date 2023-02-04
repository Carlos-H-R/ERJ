package model;

import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;

import org.json.simple.*;
import org.json.simple.parser.JSONParser;

public class DadosUsuario{
    
    /*
     * Recebe um usuário, convertendo seu dados em um objeto Json e incluindo na base de dados
     * Pasta Defaut para base de dados "DadosUsuario.json"
     */
    @SuppressWarnings("unchecked")
    public DadosUsuario(Usuario novoUsuario){
        HashMap<String,String> dados = new HashMap<String,String>();
        dados.put("nome",novoUsuario.nome);
        dados.put("senha",novoUsuario.senha);
        
        JSONObject dadosJson = new JSONObject(dados);
        
        HashMap<String,JSONObject> usuarioMap = new HashMap<String,JSONObject>();
        usuarioMap.put(novoUsuario.usuario, dadosJson);
        
        JSONArray baseDeDados;
        
        JSONObject usuarioJson = new JSONObject(usuarioMap);
        
        
        try {
            FileReader fileReader = new FileReader("DadosUsuario.json");
            
            JSONParser jsonParser = new JSONParser();
            Object obj = jsonParser.parse(fileReader);
            baseDeDados = (JSONArray) obj;
            fileReader.close();

        } catch (Exception e) {
            baseDeDados = new  JSONArray();
            baseDeDados.add(usuarioJson);
        }

        try {
            FileWriter file = new FileWriter("DadosUsuario.json");
            file.append(baseDeDados.toJSONString());
            file.flush();
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}