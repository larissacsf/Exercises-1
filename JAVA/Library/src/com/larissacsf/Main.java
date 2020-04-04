package com.larissacsf;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Book b1 = new Book("Effective Java", "0134685997");
        Book b2 = new Book("Java: A Beginner's Guide", "1260440214");
        Book b3 = new Book("Introduction to Machine Learning with Python", " 1449369413");
        Book b4 = new Book("Head First Python 2", "1491919531");
        Book b5 = new Book("Windows 10 for Dummies", "1119049369");
        Book b6 = new Book("Linux for Dummies", "0470467010");

        Student s1 = new Student("Larissa", "20192007035", "Internet Systems");
        s1.addBooks(b1);
        s1.addBooks(b4);

        Student s2 = new Student("Ana", "20192007030", "Internet Systems");
        s2.addBooks(b2);
        s2.addBooks(b3);

        Student s3 = new Student("Maria", "20192007023", "Internet Systems");
        s3.addBooks(b2);
        s3.addBooks(b5);
        s3.addBooks(b6);

        Student[] studentList = new Student[3];
        studentList[0] = s1;
        studentList[1] = s3;

        PendingBooks pb = new PendingBooks(studentList);
        System.out.println(pb.toString());










    }
}
