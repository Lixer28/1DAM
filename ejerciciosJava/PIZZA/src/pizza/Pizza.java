/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pizza;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Pizza {
    private String tamaño;
    private String tipo;
    private String estado;

    public Pizza(String tamaño, String tipo) {
        this.tamaño = tamaño;
        this.tipo = tipo;
        this.estado = "pedida";
    }

    
    public String getTamaño() {
        return tamaño;
    }

    public void setTamaño(String tamaño) {
        this.tamaño = tamaño;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
    
    
    
    public void sirve(){
        int contP = 0;
        int contS = 0;
        
        if (estado == "pedida") {
            estado = "servida";
            contP++;
            System.out.println("Pedidas: "+contP);
        }
        if (estado == "servida") {
            contS++;
        }
        
        
    }
    
    
    
    
    
    
}
