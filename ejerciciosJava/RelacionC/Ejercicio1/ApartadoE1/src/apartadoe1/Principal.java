package apartadoe1;
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
        
//        Punto pu1 = new Punto(1, 1);
//        Punto pu2 = new Punto(20, 25);
//        Punto pu3 = new Punto(30, 35);
//        
//        pu1.modificaValores(1, 1);
//        pu2.modificaValores(20, 25);
//        pu3.modificaValores(30, 35);
//        
//        pu1.imprime();
//        pu2.imprime();
//        pu3.imprime();
//        
//        
//        pu1.setXY(2, 5);
//        pu2.setXY(2, 5);
//        pu3.setXY(2, 5);
//        
//        
//        pu1.desplaza(2,5);
//        pu2.desplaza(2,5);
//        pu3.desplaza(2,5);
//        
//        
//        pu1.distancia(10, 20);
//        pu2.distancia(15, 25);
//        pu3.distancia(0, 2);
//        
//
//        
//        System.out.println("Punto 1 = "+pu1.getX()+":"+pu1.getY());
//        System.out.println("Punto 2 = "+pu2.getX()+":"+pu2.getY());
//        System.out.println("Punto 3 = "+pu3.getX()+":"+pu3.getY());

        
        Punto puntoAleatorio1 = Punto.creaPuntoAleatorio();
        Punto puntoAleatorio2 = Punto.creaPuntoAleatorio();
        
        
        System.out.println("Punto aleatorio 1: "+ puntoAleatorio1.getX()+
                ":"+ puntoAleatorio1.getY());
        
        System.out.println("Punto aleatorio 2: "+ puntoAleatorio2.getX()+
                ":"+ puntoAleatorio1.getY());
        
        
        

    }//main

}//class
