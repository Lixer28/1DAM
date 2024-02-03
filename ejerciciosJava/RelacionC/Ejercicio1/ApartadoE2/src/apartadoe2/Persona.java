/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadoe2;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Persona {
    
    private int edad;
    private final String dni;
    private String nombre, apellidos;
    private static final int mayoriaEdad = 18;
    
    
    public Persona(String dni, int edad, String nombre, String apellidos){
        
        this.dni = dni;
        this.edad = edad;
        this.nombre = nombre;
        this.apellidos = apellidos;
        
    }
    
    public void modificaValores(String dni_p, int edad_p, String nombre_p, String apellidos_p){
        
        setDni(dni_p);
        setEdad(edad_p);
        setNombre(nombre_p);
        setApellidos(apellidos_p);
        
    }

   
    public String getDni() {
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

// Se quita según el enunciado
//    public void setDni(int dni) {
//        this.dni = dni;
//    }

    
    public void setEdad(int edad) {
        this.edad = edad;
    }

  
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
    
    public void imprime(){
        
        System.out.println("Nombre:"+this.nombre+" Apellido:"
                + this.apellidos+" Edad:"+ this.edad+" DNI:"+this.dni);
        
    }
    
    
    public boolean esMayorEdad(){

       return this.edad >= 18;
    }
    
    public boolean esJubilado(){
        
        return this.edad >= 65;
    }
    
    
    public int diferenciaEdad(Persona p){
        
        return this.edad - p.edad;
        
    }
    

    
    public boolean esMayorEdad(int edad){
        return edad >= mayoriaEdad;
    }
    
    
//    public static boolean validarDNI(String dni) {
//        
//
//        
//    }
    
}
