package com.larissacsf;

import java.util.Arrays;

public class PendingBooks {
    private Student[] list;

    public PendingBooks(Student[] list) {
        this.list = list;
    }

    public Student[] getList() {
        return list;
    }

    public PendingBooks setList(Student[] list) {
        this.list = list;
        return this;
    }

    @Override
    public String toString() {
        String pendentBooks = "";
        pendentBooks += "Students With Pending Books: ";
        for(Student s : this.list){
            if(s != null){
                pendentBooks = pendentBooks + s + "\n";
            }
        }
        return pendentBooks;
    }
}
