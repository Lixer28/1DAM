package apartadod3;
//import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        
        Rectangulo r1 = new Rectangulo();
        Rectangulo r2 = new Rectangulo();
        
        
//        r1.modificaValores(0, 0, 5, 5);
//        r2.modificaValores(9, 7, 2, 3);
        
//        r1.setX1(0);    r1.setX2(0);
//        r1.setY1(5);    r1.setY2(5);
////        
//        System.out.println("Perímetro: "+((r1.getX2()-r1.getX1())*2 + (r1.getY2()+r1.getY1())*2));
//        
//        
//        r2.setX1(9);    r2.setX2(7);
//        r2.setY1(2);    r2.setY2(3);
//
//        System.out.println("Perímetro: "+((r2.getX2()+r2.getX1())*2 + (r2.getY2()+r2.getY1())*2));
        
        
        r1.setAll(10, 15,20,25);
        r2.setAll(10, 15,20,25);
        
        
        r1.imprime();
        r2.imprime();

        
        
        
        
    }//main

}//class
