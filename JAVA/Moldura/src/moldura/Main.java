/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package moldura;

import javax.swing.JOptionPane;

/**
 *
 * @author laris
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        float b = Float.parseFloat(JOptionPane.showInputDialog(null, "Base: "));
        float a = Float.parseFloat(JOptionPane.showInputDialog(null, "Altura: "));
        float l = Float.parseFloat(JOptionPane.showInputDialog(null, "Largura: "));
        AreaMoldura am = new AreaMoldura(a, b, l);
        JOptionPane.showMessageDialog(null, "Área da moldura: " + am.area());
    }
    
}
