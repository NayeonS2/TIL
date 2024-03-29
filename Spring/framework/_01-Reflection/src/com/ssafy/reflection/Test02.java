package com.ssafy.reflection;

import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.lang.reflect.Type;

public class Test02 {
    public static void main(String[] args) throws NoSuchMethodException {
        exam();
    }

    private static void exam() throws NoSuchMethodException {
        Class<?> clz = Dog.class;

        System.out.println("Dog이 갖고있는 모든 메서드를 출력");

        Method[] mArr = clz.getDeclaredMethods();

        for(Method m : mArr) {
            System.out.println("메서드 이름 :" + m.getName());

            Class<?> rClz = m.getReturnType();
            System.out.println("반환타입 : " + rClz.getName());

//            Dog이 갖고있는 모든 메서드를 출력
//            메서드 이름 :getName
//            메서드 이름 :setName
//            메서드 이름 :getAge
//            메서드 이름 :setAge


            // 파라미터 정보를 가져와보자!!
            Parameter[] pArr = m.getParameters();
            for(Parameter p : pArr) {
                Type t = p.getParameterizedType();
                System.out.println(t.getTypeName() + " " + p.getName());
            }


        }

//        Method m = clz.getDeclaredMethod("setAge", int.class);
//        System.out.println(m.getName());    // setAge
    }
}
