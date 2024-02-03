/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fraccion;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class Fraccion {
    
    //DECLARACIÓN
    
    
    
    //Variables de clase
    public int numerador;
    public int denominador;
    
    
    //CONSTRUCTOR

    public Fraccion(int numerador, int denominador) {
        this.numerador = numerador;
        this.denominador = denominador;
    }
    
    
    //GETTERS Y SETTERS 
    
    
    
    
    //MÉTODOS
    
    
    public void mostrar(){
        
        System.out.println("Fracción: "+numerador+"/"+denominador);
        
}   
    
    
    
    public void invierte(){
        int numer = this.denominador;
        int denom = this.numerador;
        
        this.numerador  = numer;
        this.denominador = denom;
        
}
    
    public void simplifica(){
        
        int resultado;
        resultado = this.numerador / this.denominador;
        
}
    
    public void multiplica(){
        Scanner sc = new Scanner (System.in);
        double num;
        double resultado;
        System.out.println("¿Por que número quieres multiplicar la fracción?");
        num = sc.nextDouble();
        
        resultado = this.numerador * num;
        System.out.println(resultado+"/"+this.denominador);
        
}
    
    public void divide(){
        Scanner sc = new Scanner (System.in);
        double num;
        double resultado;
        double resultado2;
        System.out.println("¿Por que número quieres dividir la fracción?");
        num = sc.nextDouble();
        
        resultado = this.numerador / this.denominador;
        resultado2 = this.denominador / this.numerador;
        System.out.println(resultado+"/"+resultado2);
       
        
}
    
    
    
    
    
}
