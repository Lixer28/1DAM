/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadob4;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Articulo {
    
    String nombre;
    double precio;
    double iva = 21;
    int cuantosQuedan;
    
    
    
    public Articulo(String nombre, double precio, double iva, int cuantosQuedan){
        
        this.nombre = nombre;
        this.precio = precio;
        this.iva = iva;
        this.cuantosQuedan = cuantosQuedan;
        
    }
    
    
}
