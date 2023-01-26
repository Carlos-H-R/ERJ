package dados;

// import dados.Paciente;
import java.util.Scanner;

public class CadastroPaciente {
    Scanner input = new Scanner(System.in);
    private int cmd;
    public String info;

    public CadastroPaciente(){
        this.cmd = 0;
        this.info = ("\n"+
                     "\n1 - Cadastrar paciente"+
                     "\n2 - Buscar cliente pelo código"+
                     "\n3 - Exibir dados dos pacientes"+
                     "\n4 - Sair"+
                     "\n");
    }

    public void CadastrarPaciente(Paciente[] novo, int p){
        System.out.print("\nCódigo: ");
        long codigo = input.nextLong();

        System.out.print("Nome: ");
        String nome = input.next();

        System.out.print("CPF: ");

        long cpf = input.nextLong();

        System.out.print("Telefone: ");
        long telefone = input.nextLong();

        novo[p] = new Paciente(codigo, nome, cpf, telefone);
    }

    public String toString(){
        return info;
    }

    public void options(){
        Paciente[] pacientes = new Paciente[50];

        while (cmd != 4){
            
            System.out.print(info+"\n--> ");
            this.cmd = input.nextInt();

            switch (cmd) {
                case 1:
                    for (int i=0;i < pacientes.length; i++){
                        if (pacientes[i] == null){
                            CadastrarPaciente(pacientes,i);
                            break;
                        }
                    }
                    break;
                
                case 2:
                    System.out.print("\nCódigo: ");
                    long cod = input.nextLong();
                    boolean encontrou = false;

                    for (int i=0;i<pacientes.length;i++){
                        if (pacientes[i] != null){
                            if (pacientes[i].checaCodigo(cod)){
                                System.out.println("\nPaciente encontrado\n");
                                System.out.println(pacientes[i]);
                                encontrou = true;
                                break;
                            }
                        }
                    }
                    
                    if (!encontrou){
                        System.out.println("\nPaciente não encontrado\n");
                    }

                    break;

                case 3:
                    for (int i=0;i<pacientes.length;i++){
                        if (pacientes[i] != null){
                            System.out.println(pacientes[i]);
                        }
                    }
                    break;

                case 4:
                    System.out.println("\n\nMenu Encerrado!\n\n");
                default:
                    System.out.println("\nComando inválido!\n");
                    break;
            }
        }
    }

}
