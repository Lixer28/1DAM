/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dawbank;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class CuentaBancaria {
    
    //Constantes de clase (estáticas)
    private static int MOV = 100;
    private static int DESCUBIERTO = -50;
    private static int HACIENDA = 3000;
    
    //Constantes de instancia
    private String iban;
    private String titular;
    
    //Variables de instancia
    private double saldo = 0;
    private double[] movimientos;
    private int nMov = 0;
    
    
//CONSTRUCTOR
    
    public CuentaBancaria(String iban, String titular, int saldo) {
        
        this.iban = iban;
        this.titular = titular;
        this.movimientos = new double[MOV];
}
     
    
    
    
//GETTERS Y SETTERS
    
    
    public static int getMOV() {
        return MOV;
    }

    public static void setMOV(int aMOV) {
        MOV = aMOV;
    }

    

    public static int getDESCUBIERTO() {
        return DESCUBIERTO;
    }

    public static void setDESCUBIERTO(int aDESCUBIERTO) {
        DESCUBIERTO = aDESCUBIERTO;
    }

    
    
    public static int getHACIENDA() {
        return HACIENDA;
    }

    public static void setHACIENDA(int aHACIENDA) {
        HACIENDA = aHACIENDA;
    }

    
    
    public String getiban() {
        return iban;
    }


    public String getTitular() {
        return titular;
    }


    
    public double getSaldo() {
        return saldo;
    }

    
    public double[] getMovimientos() {
        double movimiento;
        for (int i = 0; i < movimientos.length; i++) {
            movimiento = movimientos[i];
            System.out.println(movimientos[i]);
        }
        return movimientos;
}

    
    
    public void setMovimientos(double[] movimientos) {
        this.movimientos = movimientos;
    }

    
    
    public int getnMov() {
        return nMov;
    }

    public void setnMov(int nMov) {
        this.nMov = nMov;
    }

    
     
// FUNCIONES
    
//    public static void pideDatos() {
//        Scanner sc = new Scanner (System.in);
//        
//        System.out.println("Introducir IBAN:");
//        IBAN = sc.nextLine();
//        
//        System.out.println("Introducir Titular:");
//        titular = sc.nextLine();
//        
//}

//    public static void DatosCuenta() {
//        
//        System.out.println(this);
//        
//}
    
    public void printITS() {
    System.out.println("IBAN: " + this.iban);
    System.out.println("Titular: " + this.titular);
    System.out.println("Saldo: " + this.saldo+"€");
}//IBAN, TITULAR, SALDO
    
    
    public void printIBAN() {
    System.out.println("IBAN: " + this.iban);
}//IBAN
    
    public void printTitular() {
    System.out.println("Titular: " + this.titular);
}//TITULAR
    
    public void printSaldo() {
    System.out.println("Saldo: " + this.saldo+"€");
}//SALDO

    public void ingreso(){
        Scanner sc = new Scanner(System.in);
        double cantidad;
        System.out.println("¿Cuánta cantidad quieres ingresar?");
        
        if (this.nMov >= MOV) {
            System.out.println("No se pueden realizar más ingresos, ha alcanzado el límite");
        }
        else{
            cantidad = sc.nextDouble();
            if (cantidad >0) {
                this.saldo = this.saldo + cantidad;
            }
            else{
                System.out.println("El ingreso debe ser mayor de 0");
            }
            nMov ++;
            if (this.saldo >= 3000) {
                System.out.println("AVISO: Notificar a hacienda");
            }
        }
    }//INGRESO
    
    
    
    public void retirada(){
        Scanner sc = new Scanner(System.in);
        double cantidad;
        System.out.println("¿Cuánta cantidad quieres retirar?");
        cantidad = sc.nextDouble();
        
        if ((this.saldo-cantidad) <0) {
            System.out.println("AVISO: Saldo negativo");
        }
        else{
            if (cantidad >0) {
                this.saldo = this.saldo - cantidad;
            }
            else{
                System.out.println("La retirada debe ser mayor de 0");
            }
            
            nMov ++;
        }
        
        if ((this.saldo - cantidad) < -50) {
                System.out.println("No se puede retirar más dinero, ha alcanzado el límite");
        }
        else{
            this.saldo = this.saldo - cantidad;
        }
        
    }//RETIRADA
    
    
    public void movimientos(){
        
        System.out.println("Nº movimientos = "+ getnMov());
        for (int i = 0; i < nMov; i++){
            System.out.println((i+1)+". "+ movimientos[i]);;
            
        }
        System.out.println("");
        
    }
    
    
    
}
