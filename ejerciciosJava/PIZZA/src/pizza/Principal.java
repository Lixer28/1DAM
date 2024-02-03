/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pizza;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Pizza p1 = new Pizza("mediana", "margarita");
        Pizza p2 = new Pizza("pequeña", "funghi");
        Pizza p3 = new Pizza("pequeña", "funghi");
        
        System.out.println(p1.getEstado());
        System.out.println(p2.getEstado());
        p1.sirve();
        p2.sirve();
        p3.sirve();
        
        
        
    }
    
}
