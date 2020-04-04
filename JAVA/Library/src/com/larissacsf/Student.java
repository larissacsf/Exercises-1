package com.larissacsf;

public class Student {
    private String name;
    private String registration;
    private String course;
    private int totBooks;
    private Book[] list = new Book[3];

    public Student(String name, String registration, String course) {
        this.name = name;
        this.registration = registration;
        this.course = course;

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRegistration() {
        return registration;
    }

    public void setRegistration(String registration) {
        this.registration = registration;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public int getTotBooks() {
        return totBooks;
    }

    public Student setTotBooks(int totBooks) {
        this.totBooks = totBooks;
        return this;
    }

    public Book[] getList() {
        return list;
    }

    public void setList(Book[] list) {
        this.list = list;
    }

    public boolean addBooks(Book book){
        if(totBooks == 3){
            return false;
        }
        list[totBooks] = book;
        totBooks++;
        return true;
    }


    @Override
    public String toString() {
        String studentInfo = "";
        studentInfo += "\nName: " + this.name + "\nRegistration: " + this.registration + "\nCourse: " + this.course + "\nBook List: " ;
        for(Book b : this.list){
            if(b != null){
                studentInfo = studentInfo + b + "\n";
            }
        }
        return studentInfo;

    }
}


