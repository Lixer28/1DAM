package apartadod2;
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
        
        p1.imprime();

        
       if (p1.esMayorEdad() == true) {
            System.out.println(p1.getNombre()+" es mayor de edad");
        }
        else{
            System.out.println(p1.getNombre()+" no es mayor de edad");
        }
        
        
        if (p1.esJubilado() == true) {
            System.out.println(p1.getNombre()+" es jubilado");
        }
        else{
            System.out.println(p1.getNombre()+" no es jubilado");
        }
        
        p1.diferenciaEdad(p1);
    
        
        
        
//        if (p1.getEdad() >= 18){
//            System.out.println(p1.getNombre()+" "+p1.getApellidos()+" con DNI "+p1.getDni()+" es mayor de edad");
//        }
//        else{
//            System.out.println(p1.getNombre()+" "+p1.getApellidos()+" con DNI "+p1.getDni()+" no es mayor de edad");
//        }
        
        
    }//main

}//class
