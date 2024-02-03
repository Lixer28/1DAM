/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package piramide;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Rectangulo {
    private int altura;
    private int base;

    public Rectangulo() {
    }
    
    
    public void mostrarRectangulo(int base, int altura){
        
        if (base < 0 && altura < 0) {
            System.out.println("El número debe ser mayor que 0");
        }
        else{
            for (int i = 0; i <= base; i++) {
                System.out.print("*");
                
                for (int j = 0; j <= altura; j++) {
                    System.out.print("*");
                }
                System.out.println("");
            }
            
        }
            
            
    }
   
    
    
    
    
    
    
    
    
    
}
