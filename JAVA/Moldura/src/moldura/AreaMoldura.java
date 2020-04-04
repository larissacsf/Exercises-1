/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package moldura;

/**
 *
 * @author laris
 */
public class AreaMoldura {
    float base;
    float altura;
    float largura;
    

    public AreaMoldura(float base, float altura, float largura) {
        this.base = base;
        this.altura = altura;
        this.largura = largura;
    }
    
    public float area(){
        float moldura = ((this.base * this.altura) - ((this.base - (2 * this.largura))) * (this.altura - (2 * this.largura)));
        return moldura;
    }
}
