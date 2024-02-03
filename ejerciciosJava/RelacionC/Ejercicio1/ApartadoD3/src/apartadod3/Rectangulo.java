/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package apartadod3;

/**
 *
 * @author Víctor Quirós Pavón
 */
public class Rectangulo {
    private int x1;
    private int x2;
    private int y1;
    private int y2;
    
    
    
//    public Rectangulo(int x1, int y1, int x2, int y2){
//        
//        if (x2 > x1 && y2 > y1){
//            this.x1 = x1;
//            this.y1 = y1;
//            this.x2 = x2;
//            this.y2 = y2;
//        }
//        else{
//            
//            System.err.println("ERROR al instanciar Rectagulo...");
//            
//        } 
//    }
    
    
//    public void modificaValores(int x1_m, int x2_m, int y1_m, int y2_m){
//        
//        if (x2 > x1 && y2 > y1){
//            setX1(x1_m);
//            setX2(x2_m);
//            setY1(y1_m);
//            setY2(y2_m);
//        }
//        else{
//            System.err.println("ERROR al instanciar Rectagulo...");
//        }
//        
//    }

   
    public int getX1() {
        return x1;
    }


    public int getX2() {
        return x2;
    }

    
    public int getY1() {
        return y1;
    }


    public int getY2() {
        return y2;
    }


    public void setX1(int x1) {
        if (this.x2 > x1){
            this.x1 = x1;
        }
        else{
            System.err.println("ERROR al instanciar Rectagulo...");
        }
    }


    public void setX2(int x2) {
        if (this.x2 > x1){
            this.x2 = x2;
        }
        else{
            System.err.println("ERROR al instanciar Rectagulo...");
        }
    }


    public void setY1(int y1) {
        if (this.x2 > x1){
            this.y1 = y1;
        }
        else{
            System.err.println("ERROR al instanciar Rectagulo...");
        }
    }


    public void setY2(int y2) {
        if (this.x2 > x1){
            this.y2 = y2;
        }
        else{
            System.err.println("ERROR al instanciar Rectagulo...");
        }
    }
    
    
    public void imprime(){
        
        System.out.println("Rectángulo: "+x1+":"+ y1+"    "+x2+":"+ y2);
        
    }
    
    public void setX1Y1(int x1, int y1) {
        
        this.x1 = x1;
        this.y1 = y1;
    }
    
    public void setX2Y2(int x2, int y2){
        
        this.x2 = x2;
        this.y2 = y2;  
    }
    
    public void setAll(int x1, int y1, int x2, int y2){
        
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
}
    
    public int getPerimetro(){
        int largo;
        int ancho;
        int resultado;
        
        largo = x2-x1;
        ancho = y2 - y1;
        resultado = 2*(largo + ancho);
        
        return resultado;
        
}
    
    public int getArea(){
        int largo;
        int ancho;
        int resultado;
        
        largo = x2 - x1;
        ancho = y2 - y1;
        resultado = largo * ancho;
        
        return resultado;
        
    }
    
    
    
    
    
    
    
    
    
}
