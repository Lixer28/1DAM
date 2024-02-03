/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadod4;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Articulo {
    
    private String nombre;
    private double precio;
    private final double ivaG = 21;
    private double ivaR = 10;
    private double ivaSP = 4;
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


    public double getIvaG() {
        return ivaG;
    }
    
    
    public double getIvaR() {
        return ivaG;
    }
    
    
    public double getIvaSR() {
        return ivaG;
    }


    public int getCuantosQuedan() {
        return cuantosQuedan;
    }
    
    
    public double getPVP(){
        double PVP;
        PVP = precio * ivaG;
        return PVP;
    }
    
    public double getPVPDescuento(double descuento){
        double precio = this.getPVP();

        return precio - (precio * descuento /100.0);
        
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


    public void setIvaG(double ivaG) {
        if (ivaG == 21){
            this.ivaG = ivaG;
        }
        else{
            System.err.println("ERROR el IVA debe ser 21...");
        }
    }
    
    
    /**
     * @param ivaR the ivaR to set
     */
    public void setIvaR(double ivaR) {
        this.ivaR = ivaR;
    }

    /**
     * @param ivaSP the ivaSP to set
     */
    public void setIvaSP(double ivaSP) {
        this.ivaSP = ivaSP;
    }
    
    
    



    public void setCuantosQuedan(int cuantosQuedan) {
        if (cuantosQuedan <0){
            System.err.println("ERROR, no puede haber menos de 0 productos...");
        }
        else{
            this.cuantosQuedan = cuantosQuedan;
        }
    } 
    
    
    public void imprime(){
        
        System.out.println(nombre+ precio+ iva+ cuantosQuedan);
        
    }
    
    
    
    public boolean vender(int x){
        
        if (cuantosQuedan < x) {
            cuantosQuedan = cuantosQuedan - x;
            return true;
        }
        else{
            return false;
        }
    }
    
    
    public boolean almacenar(int x){
        
        if (cuantosQuedan > x) {
            cuantosQuedan = cuantosQuedan + x;
            return true;
        }
        else{
            return false;
        }
    }

    
    
    
    
}
