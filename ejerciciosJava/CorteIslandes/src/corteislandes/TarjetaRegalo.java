/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package corteislandes;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class TarjetaRegalo {
   
    //Variables
    private double saldo;
    private int pin;
    

    
    //Constructor
    public TarjetaRegalo(double saldo) {
        this.saldo = saldo;
        
    }
    
     public TarjetaRegalo() {
         this.saldo = 0;
    }
    
    
    //Getters y Setters

   
    
    
    
    
    
    //Métodos
    
    public double establecerPin(){
    
        this.pin = (int)Math.random()*10000;
        return this.pin;
    }
    
    public void gasta(){
        Scanner sc = new Scanner(System.in);
        double cantidad;
        System.out.println("¿Cuánto quieres gastar?");
        cantidad = sc.nextDouble();
        
        if (this.saldo > 0) {
            this.saldo = this.saldo - cantidad;
        }
        else{
            System.out.println("No puedes gastar más, has llegado a 0");
        }
    }
        
//    public double fusionaCon(){
//        
//        
//        
//    }
    
    
    
    
}
    

    
    
    
    


    
