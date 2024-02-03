package apartadob1;
import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        Scanner sc1 = new Scanner (System.in);
        
        Punto pu1 = new Punto();
        Punto pu2 = new Punto();
        Punto pu3 = new Punto();
        
        pu1.modificaValores(10, 15);
        pu2.modificaValores(20, 25);
        pu3.modificaValores(30, 35);
        
        
        System.out.println("Punto 1 = "+pu1.getX()+":"+pu1.getY());
        System.out.println("Punto 2 = "+pu2.getX()+":"+pu2.getY());
        System.out.println("Punto 3 = "+pu3.getX()+":"+pu3.getY());




    }//main

}//class
