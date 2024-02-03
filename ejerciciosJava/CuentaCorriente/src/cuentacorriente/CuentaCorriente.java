/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cuentacorriente;
import java.util.Scanner;
/**
 *
 * @author Víctor Quirós Pavón
 */
public class CuentaCorriente {
    
    private final int ncuenta;
    private double saldo;

    public CuentaCorriente(double saldo) {
        this.ncuenta = (int)Math.random()*90000;
        this.saldo = saldo;
    }

    public CuentaCorriente() {
        this.ncuenta = (int)Math.random()*90000;
        this.saldo = 0;
        
    }

    
    
    
    
    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    

    
    
    
    public double ingresar(double cantidad){
        Scanner sc = new Scanner(System.in);
        

        this.saldo = this.saldo + cantidad;
        return this.saldo;
    }
    
    public double gastar(double cantidad){
        Scanner sc = new Scanner(System.in);
        

        this.saldo = this.saldo - cantidad;
        return this.saldo;
    }
    
    
    public void transferencia(CuentaCorriente c1, CuentaCorriente c2, int ingreso){
        
        c1.saldo = c1.saldo - ingreso;       
        c2.saldo = c2.saldo + ingreso;       
        
    }
    
    
    
    
    
    
    
    
    
}
