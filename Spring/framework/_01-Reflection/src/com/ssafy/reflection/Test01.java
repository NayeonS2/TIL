package com.ssafy.reflection;

public class Test01 {
    public static void main(String[] args) throws ClassNotFoundException {
        exam();
    }


    // 클래스를 접근하는 3가지 방법 (클래스영역에 있는 클래스에 대한 정보들을 가져오는 것)
    private static void exam() throws ClassNotFoundException {
        //1. 클래스이름.class
        Class<?> clz = Dog.class;

        //2. Class.forName("패키지 포함 클래스명")
        Class<?> clz2 = Class.forName("com.ssafy.reflection.Dog");

        //3. 객체(인스턴스).getClass()
        Dog d = new Dog();
        Class<?> clz3 = d.getClass();

        System.out.println(clz == clz2);    // true
        System.out.println(clz2 == clz3);   // true

        String name = clz.getName();
        String sName = clz.getSimpleName();

        System.out.println(name);   // com.ssafy.reflection.Dog (기본은 풀 패키지명!!)
        System.out.println(sName);  // Dog
    }
}
