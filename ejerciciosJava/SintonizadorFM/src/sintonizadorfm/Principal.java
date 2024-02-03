/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package sintonizadorfm;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int respuesta = 0;
        
        Sintonizador s1 = new Sintonizador();
        
        
        do {
            System.out.println("--------MENÚ--------");
            System.out.println("1. Insertar frecuencia");
            System.out.println("2. Subir frecuencia");
            System.out.println("3. Bajar frecuencia");
            System.out.println("4. Mostrar frecuencia");
            System.out.println("5. Salir");
            respuesta = sc.nextInt();
            
            switch (respuesta) {
                case 1:
                    s1.insertarFrecuencia();
                    break;
                
                case 2:
                    s1.up();
                    break;
                    
                case 3:
                    s1.down();
                    break;
                    
                case 4:
                    s1.display();
                    break;    
                
                case 5:
                    break;   
                    
                default:
                    throw new AssertionError();
            }

        } while (respuesta != 5);
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
//        System.out.println("Establecer frecuencia a 92");
//        s1.setFrecuencia(92);
//        
//        System.out.println("Salto a 10");
//        s1.setSalto(10);
//        
//        System.out.println("Muestro resultado:");
//        System.out.println(s1.getFrecuencia());
        
        
    }
    
}
