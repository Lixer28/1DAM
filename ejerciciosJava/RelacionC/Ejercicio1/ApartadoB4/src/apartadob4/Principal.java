package apartadob4;
import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        
        
        Scanner sc3 = new Scanner(System.in);
        
        Articulo a1 = new Articulo("Pijama",12,21,3);
        
        System.out.println("Nombre: "+a1.nombre+" - Precio: "+a1.precio+"€"+" - IVA: "+a1.iva+"%"+" - Quedan: "+a1.cuantosQuedan);
        

    }//main

}//class
