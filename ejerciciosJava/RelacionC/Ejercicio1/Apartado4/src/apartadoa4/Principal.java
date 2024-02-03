package apartadoa4;
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
        
        Articulo a1 = new Articulo();
        System.out.print("Nombre: ");
        a1.nombre = sc3.next();
        System.out.print("Precio: ");
        a1.precio = sc3.nextDouble();
        System.out.println("IVA: 21%");
        System.out.println(a1.nombre+" - "+"Precio: "+a1.precio+"€ - IVA: 21% - "+
                "PVP:"+a1.precio*(a1.iva) );
        
        
        
    }//main

}//class
