package apartadob2;
//import java.util.Scanner;

/*
ENUNCIADO:


*\
/**
 * @author Víctor Quirós Pavón
 */
public class Principal {

    
    public static void main(String[] args) {
        
        Persona p1 = new Persona (123456789, 18, "Víctor", "Quirós");
        
        
        if (p1.edad >= 18){
            System.out.println(p1.nombre+" "+p1.apellidos+" con DNI "+p1.dni+" es mayor de edad");
        }
        else{
            System.out.println(p1.nombre+" "+p1.apellidos+" con DNI "+p1.dni+" no es mayor de edad");
        }
        
        
    }//main

}//class
