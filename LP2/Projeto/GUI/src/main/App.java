package main;

import javafx.application.Application;
import javafx.stage.Stage;
import view.LoginGUI;

public class App extends Application{
    
    /** 
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        Application.launch(args);
    }

    
    /** 
     * @param stage
     * @throws Exception
     */
    @Override
    public void start(Stage stage) throws Exception {
        new LoginGUI();
    }
}
