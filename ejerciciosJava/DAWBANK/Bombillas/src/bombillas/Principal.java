package bombillas;
//import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        
        
        Bombilla b1 = new Bombilla();
        Bombilla b2 = new Bombilla();
        
        System.out.println("\nEncender bombilla");
        System.out.println("------------------------");
        b1.encenderBombilla();
        
        System.out.println("Estado bombilla:");
        b1.estadoBombilla();
        
        
        System.out.println("\nApagar bombilla");
        System.out.println("------------------------");
        b1.apagarBombilla();
        
        System.out.println("Estado bombilla:");
        b1.estadoBombilla();
        
        
        System.out.println("\nApagar interruptor general");
        System.out.println("------------------------");
        Bombilla.general = false;
        
        System.out.println("Estado bombilla:");
        b1.estadoBombilla();
        
        
        System.out.println("\nEncender interruptor general");
        System.out.println("------------------------");
        Bombilla.general = true;
        
        System.out.println("Estado bombilla:");
        b1.estadoBombilla();
        
        
        
        
    }//main

}//class
