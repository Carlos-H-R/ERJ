package Exercicio_2.models;

public class EquipamentoSonoro extends Equipamento{
    protected short volume;
    protected Boolean stereo;

    public EquipamentoSonoro(String nome) {
        super(nome);
    }

    public void ativarMono(){
        stereo = false;
    }

    public void ativarStereo(){
        stereo = true;
    }

    @Override
    public void liga() {
        super.liga();
        volume = 5;
    }
    
}
