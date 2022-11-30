package com.ssafy.reflection;

public class Dog {
    private String name;
    private int age;

    // method를 쓰면 그 안에서 로직을 처리 가능!

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
