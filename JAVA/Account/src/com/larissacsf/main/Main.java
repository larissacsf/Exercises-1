package com.larissacsf.main;

import com.larissacsf.classes.Bank;
import com.larissacsf.classes.BankAccount;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // write your code here
        Bank b = new Bank(new ArrayList<BankAccount>());
        b.addAccount(184433, 167.90);
        b.addAccount(239867, 675.89);
        b.addAccount(456430, 453.76);
        System.out.println("Account with higher balance" + b.highestBalance());
    }
}
