package com.larissacsf.classes;

public class BankAccount {
    private int accountNumber;
    private double accountBalance;

    public BankAccount(int accountNumber, double accountBalance) {
        this.accountNumber = accountNumber;
        this.accountBalance = accountBalance;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;

    }

    public double getAccountBalance() {
        return accountBalance;
    }

    public void setAccountBalance(double accountBalance) {
        this.accountBalance = accountBalance;

    }

    @Override
    public String toString() {
        return "\nAccount Number: " + this.accountNumber + "\nAccount Balance: R$ " + this.accountBalance;
    }
}
