package apartadoa2;
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
        Scanner sc2 = new Scanner (System.in);
        
        Persona pe1 = new Persona();
        Persona pe2 = new Persona();
        
        System.out.println("Escribe tu nombre:");
        pe1.nombre = sc1.next();
        
        System.out.println("Escribe tus apellidos:");
        pe1.apellidos = sc1.next();
        
        System.out.println("Escribe tu DNI:");
        pe1.dni = sc1.nextInt();
        
        System.out.println("Escribe tu edad:");
        pe1.edad = sc1.nextInt();
        
        
        if (pe1.edad >= 18){
            System.out.println(pe1.nombre+" "+pe1.apellidos+" con DNI "+pe1.dni+" es mayor de edad");
        }
        else{
            System.out.println(pe1.nombre+" "+pe1.apellidos+" con DNI "+pe1.dni+" no es mayor de edad");
        }
        
        System.out.println("");
        System.out.println("Escribe tu nombre:");
        pe2.nombre = sc2.next();
        
        System.out.println("Escribe tus apellidos:");
        pe2.apellidos = sc2.next();
        
        System.out.println("Escribe tu DNI:");
        pe2.dni = sc2.nextInt();
        
        System.out.println("Escribe tu edad:");
        pe2.edad = sc2.nextInt();
        
        
        
        if (pe1.edad >= 18){
            System.out.println(pe1.nombre+pe1.apellidos+"con DNI"+pe1.dni+"es mayor de edad");
        }
        else{
            System.out.println(pe1.nombre+pe1.apellidos+"con DNI"+pe1.dni+"no es mayor de edad");
        }
        
        
        
    }//main

    
    
    
    
}//class
