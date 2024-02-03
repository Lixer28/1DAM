/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package cuentacorriente;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
        CuentaCorriente c1 = new CuentaCorriente(1000);
        CuentaCorriente c2 = new CuentaCorriente();
        
        
        System.out.println(c1.getSaldo());
        System.out.println(c2.getSaldo());
        
        c1.ingresar(300);
        c2.gastar(20);
        
        
        c1.transferencia(c1, c2, 300);
        
        System.out.println(c1.getSaldo());
        System.out.println(c2.getSaldo());
        
        
    }
    
}
