/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package piramide;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Piramide {
    
    private int altura;

    
    
    public Piramide() {
        
    }
    
    
    
    public void mostrarPiramide(int altura){
        int blancos;
        int asteriscos;
        
        blancos = altura -1;
        asteriscos = 1;
        
        if (altura < 0) {
            System.out.println("El número debe ser mayor que 0");
        }
        else{
            for (int i = 1; i <= altura; i++){

                for (int j = 1; j <= blancos; j++){  
                    System.out.print(" ");        
                }

                for (int j = 1; j <= asteriscos; j++){
                    System.out.print("*");
                }

                blancos--;
                asteriscos+=2;
                System.out.println("");
            }

        }
     }
        
        
    
    
    
    
    
    
}
