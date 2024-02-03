package apartadob4;
//import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        

        Articulo a1 = new Articulo();
        
        
        System.out.println("Nombre: "+a1.getNombre()+" - Precio: "+a1.getPrecio()+"€"+
                " - IVA: "+a1.getIva()+"%"+" - Quedan: "+a1.getCuantosQuedan());
        
        
        a1.setNombre("Pijama");
        a1.setPrecio(12);
        a1.setIva(21);
        a1.setCuantosQuedan(-1);
        
        
        

    }//main

}//class
