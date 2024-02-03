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
    
    private String nombre;
    private double precio;
    private double iva = 21;
    private int cuantosQuedan;
    
    
    
//    public Articulo(String nombre, double precio, double iva, int cuantosQuedan){
//        
//        this.nombre = nombre;
//        this.precio = precio;
//        this.iva = iva;
//        this.cuantosQuedan = cuantosQuedan;
//        
//    }
//    


    public String getNombre() {
        return nombre;
    }


    public double getPrecio() {
        return precio;
    }


    public double getIva() {
        return iva;
    }


    public int getCuantosQuedan() {
        return cuantosQuedan;
    }


    public void setNombre(String nombre) {
        if (nombre.isEmpty()){
            System.err.println("ERROR con el nombre introducido...");
        }
        else{
            this.nombre = nombre;
        }
    }


    public void setPrecio(double precio) {
        if (precio > 0){
            this.precio = precio;
        }
        else{
            System.err.println("ERROR, el precio debe ser mayor que 0...");
        }
    }


    public void setIva(double iva) {
        if (iva == 21){
            this.iva = iva;
        }
        else{
            System.err.println("ERROR el IVA debe ser 21...");
        }
    }


    public void setCuantosQuedan(int cuantosQuedan) {
        if (cuantosQuedan <0){
            System.err.println("ERROR, no puede haber menos de 0 productos...");
        }
        else{
            this.cuantosQuedan = cuantosQuedan;
        }
    } 
    
    
    
    
}
