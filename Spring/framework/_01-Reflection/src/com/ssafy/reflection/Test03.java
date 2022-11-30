package com.ssafy.reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class Test03 {
    public static void main(String[] args) throws Exception {
        exam();
        exam2();
    }

    // 1.리플렉션 이용해 객체 생성
    private static void exam() throws Exception {
        //Dog d = new Dog(); 이게 하고싶음
        Class<Dog> clz = Dog.class;
        Constructor<Dog> constructor = clz.getDeclaredConstructor();
        Dog dog = constructor.newInstance();

        // Dog dog = Dog.class.getDeclaredConstructor().newInstance(); 와 같음

        dog.setName("마루");
        System.out.println(dog.getName());
    }

    // 2.리플렉션 이용해 메서드 실행
    private static void exam2() throws Exception {
        Class<?> clz = Class.forName("com.ssafy.reflection.Dog");

        Object obj = clz.getDeclaredConstructor().newInstance();

        //setName이라는 메서드 얻기
        Method method = clz.getDeclaredMethod("setName", String.class);

        //메서드를 실행하는 방법 : invoke(객체, 매개변수)
        method.invoke(obj, "마리");

        method = clz.getDeclaredMethod("getName");
        String name = (String)method.invoke(obj);
        System.out.println(name);


    }
}



