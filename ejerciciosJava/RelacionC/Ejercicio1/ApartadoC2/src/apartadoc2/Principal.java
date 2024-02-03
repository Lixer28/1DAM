package apartadoc2;
//import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        
        Persona p1 = new Persona();
        
        
        p1.modificaValores(123456789, 18, "Víctor", "Quirós");
        
        if (p1.getEdad() >= 18){
            System.out.println(p1.getNombre()+" "+p1.getApellidos()+" con DNI "+p1.getDni()+" es mayor de edad");
        }
        else{
            System.out.println(p1.getNombre()+" "+p1.getApellidos()+" con DNI "+p1.getDni()+" no es mayor de edad");
        }
        
        
    }//main

}//class
