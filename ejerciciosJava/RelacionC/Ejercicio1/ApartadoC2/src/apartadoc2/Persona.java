/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadoc2;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Persona {
    
    private int dni, edad;
    private String nombre, apellidos;
    
    
//    public Persona(int dni, int edad, String nombre, String apellidos){
//        
//        this.dni = dni;
//        this.edad = edad;
//        this.nombre = nombre;
//        this.apellidos = apellidos;
//        
//    }
    
    public void modificaValores(int dni_p, int edad_p, String nombre_p, String apellidos_p){
        
        setDni(dni_p);
        setEdad(edad_p);
        setNombre(nombre_p);
        setApellidos(apellidos_p);
        
    }

   
    public int getDni() {
        return dni;
    }

    
    public int getEdad() {
        return edad;
    }

    
    public String getNombre() {
        return nombre;
    }

   
    public String getApellidos() {
        return apellidos;
    }

    
    public void setDni(int dni) {
        this.dni = dni;
    }

    
    public void setEdad(int edad) {
        this.edad = edad;
    }

  
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
    
    
    
    
}
