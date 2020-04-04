package com.larissacsf.classes;

import java.util.ArrayList;

public class Bank {
    private ArrayList<BankAccount> accountList = new ArrayList<BankAccount>();

    public Bank(ArrayList<BankAccount> accountList) {
        this.accountList = accountList;
    }

    public ArrayList<BankAccount> getAccountList() {
        return accountList;
    }

    public void setAccountList(ArrayList<BankAccount> accountList) {
        this.accountList = accountList;
    }

    public void addAccount(int number, double balance) {
        BankAccount a = new BankAccount(number, balance);
        this.accountList.add(a);
    }

    public BankAccount highestBalance(){
        double balance = 0;
        BankAccount biggerAccount = null;
        for(BankAccount a : this.accountList){
            if (a.getAccountBalance() > balance){
                balance = a.getAccountBalance();
                biggerAccount = a;
            }
        }
        return biggerAccount;
    }

    @Override
    public String toString() {
        return "Account Information: " + this.accountList;
    }
}
