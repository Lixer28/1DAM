/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package piramide;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Piramide p1 = new Piramide();
        
        Rectangulo r1 = new Rectangulo();
        
        p1.mostrarPiramide(4);
        System.out.println("");
        r1.mostrarRectangulo(4, 6);
        
    }
    
}
