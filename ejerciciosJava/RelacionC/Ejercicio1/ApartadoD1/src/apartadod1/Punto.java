/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadod1;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Punto {
    private int x;
    private int y;
    
    
    
    
//    public Punto(int x, int y){
//        this.x = x;
//        this.y = y;
//        
//    }// public Punto

   
    
    public void modificaValores(int x_m, int y_m){
        x = x_m;
        y = y_m;
    }
    
    
    
    public int getX() {
        return x;
    }

    
    public int getY() {
        return y;
    }

   
    public void setX(int x) {
        this.x = x;
    }

    
    public void setY(int y) {
        this.y = y;
    }

    public void setXY(int x, int y){
        
        this.x = x;
        this.y = y;
        
    }
    
    
    public void imprime(){
        System.out.println(this.x+":"+this.y);
    }
    
    
    public void desplaza(int dx, int dy){
        
        this.x = this.x + dx;
        this.y = this.y + dy;
        
    }
    
    public int distancia(int x2, int y2){
        int puntop;
        puntop=(int)Math.sqrt((Math.pow((x2 - x),2)) + (Math.pow((y2-y),2)));
        return puntop;
    }
    
    
    
}// public class Punto



