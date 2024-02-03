/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejercicio8libro;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Terminal {
    private final String NUM;
    private int tiempo;

    
    public Terminal(String num) {
        this.NUM = num;
    }

    
    
    
    
    public String getNum() {
        return NUM;
    }

    public int getTiempo() {
        return tiempo;
    }

    public void setTiempo(int tiempo) {
        this.tiempo = tiempo;
    }

   
    
    

    
    
    public void llama(Terminal t1, int tiempo){
        
        
        System.out.println(t1.getNum()+" - "+tiempo+"s de conversación");
        t1.tiempo += this.tiempo;
        
    }
    
//public void llama(Terminal t, int segundosDeLlamada) {
//    this.tiempoDeConversacion += segundosDeLlamada;
//    t.tiempoDeConversacion += segundosDeLlamada;
//  }
    
    
    
}
