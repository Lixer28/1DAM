/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bombillas;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Bombilla {
    
    //
    private boolean encendida = false;
    public static boolean general = false;
    
    
    public Bombilla() {
        this.encendida = encendida;
    }

    
    public void estadoBombilla(){
        
        if (this.encendida == true){
            System.out.println("La bombilla está encendida");
        }
        else{
            System.out.println("La bombilla está apagada");
        }
        
        
}
    
    public void encenderBombilla(){
        
        this.encendida = true;
//        System.out.println("Bombilla encendida");
        
}
    
    public void apagarBombilla(){
        
        this.encendida = false;
//        System.out.println("Bombilla apagada");
        
}
    

    
    
    
    
    
    
}

