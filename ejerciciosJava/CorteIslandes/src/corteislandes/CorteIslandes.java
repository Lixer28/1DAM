/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package corteislandes;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class CorteIslandes {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
        TarjetaRegalo t1 = new TarjetaRegalo(50);
        TarjetaRegalo t2 = new TarjetaRegalo();
        
        System.out.println(t1);
        System.out.println(t2);
        t1.establecerPin();
        
        
    }
    
}
