/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio8libro;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        Terminal t1 = new Terminal("123 45 67 89");
        Terminal t2 = new Terminal("987 65 43 21");
        Terminal t3 = new Terminal("456 78 23 91");
        
        
        t1.getNum();
        t2.getNum();
        
        t2.llama(t1, 320);
        t2.llama(t1, 100);
        t3.llama(t2, 50);
        
        t1.getNum();
        t2.getNum();
        
        
    }
    
}
