package apartadoa3;
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
        
        r1.x1 = 0;    r1.y1 = 0;
        r2.x2 = 5;    r2.y2 = 5;
        
        System.out.println("Perímetro: "+(r1.x1+r2.x2) +":"+ (r1.y1+r2.y2));

        r1.x1 = 7;    r1.y1 = 9;
        r2.x2 = 2;    r2.y2 = 3;
        
        
        System.out.println("Perímetro: "+(r1.x1+r2.x2) +":"+ (r1.y1+r2.y2));
        
        
        
        
    }//main

}//class
