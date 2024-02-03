/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package sintonizadorfm;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class Sintonizador {
    
    private static final double salto = 0.5;
    private static final double maximo = 108;
    private static final double minimo = 80;

    private double frecuencia;
    
    public Sintonizador() {
        frecuencia = minimo;
    }

    
    
    
    
    
    public static double getSalto() {
        return salto;
    }

    public static double getMaximo() {
        return maximo;
    }

    public static double getMinimo() {
        return minimo;
    }

    public double getFrecuencia() {
        return frecuencia;
    }

    public void setFrecuencia(double frecuencia) {
        this.frecuencia = frecuencia;
    }
    
    

    
    
    
    
    

    public void display(){
        System.out.println("Frecuencia: "+this.frecuencia);
    }
    
    
    public void insertarFrecuencia(){
        Scanner sc = new Scanner(System.in);
        double frecuencia = sc.nextDouble();
        this.frecuencia = frecuencia;
    }
    
    public void up(){
        
        frecuencia = frecuencia + salto;
        
        if (frecuencia > maximo) {
            frecuencia = minimo;
        }
        
    }
    
    public void down(){
        frecuencia = frecuencia - salto;
        
        if (frecuencia < minimo) {
            frecuencia = maximo;
        }
        
    }
    
    
    
    
}
