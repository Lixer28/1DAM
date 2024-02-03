package dawbank;
import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class DawBank {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int respuesta;
        String iban;
        String titular;
        int saldo;
        

        System.out.println("--------------------------------------");
        System.out.println("\tCREACIÓN DE LA CUENTA");
        System.out.println("--------------------------------------");
        System.out.println("Introducir IBAN:");
        iban = sc.nextLine();

        System.out.println("Introducir Titular (nombre completo):");
        titular = sc.nextLine();
        
        
        
        CuentaBancaria cuenta1 = new CuentaBancaria(iban , titular, 0);
        
        
        do{
            
        System.out.println("\n------------------------------------");
        System.out.println("1. Datos de la cuenta");
        System.out.println("2. IBAN");
        System.out.println("3. Titular");
        System.out.println("4. Saldo");
        System.out.println("5. Ingreso");
        System.out.println("6. Retirada");
        System.out.println("7. Movimientos");
        System.out.println("8. Salir");
        respuesta = sc.nextInt();
    
    
            switch (respuesta){
                case 1:
                    cuenta1.printITS();
                    break;
                    
                case 2:
                    cuenta1.printIBAN();
                    break;
                    
                case 3:
                    cuenta1.printTitular();
                    break;
                    
                case 4:
                    cuenta1.printSaldo();
                    break;
                
                case 5:
                    cuenta1.ingreso();
                    break;
                    
                case 6:
                    cuenta1.retirada();
                    break;
                    
                case 7:
                    cuenta1.getMovimientos();
                    break;

                case 8:
                    break;
                    
                default:
                    throw new AssertionError();
            }

        } while (respuesta != 8);
        
        
        
        
        
        
        
    }//main

}//class
