package ch08;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ThrowsException {
	// throws이용해서 예외를 미루고
	public Class loadCalss(String fileName, String className) throws FileNotFoundException, ClassNotFoundException {
		
		FileInputStream fis = new FileInputStream(fileName);
		Class c = Class.forName(className);
		return c;
	}
	
	
	public static void main(String[] args) {
		// 사용하는 부분에서 예외를 처리!
		ThrowsException test = new ThrowsException();
		
		try {
			test.loadCalss("a.txt", "java.lang.String");
		} catch (ClassNotFoundException e) {
			System.out.println(e);
		} catch (FileNotFoundException e) {
			System.out.println(e);
		} catch (Exception e) {
			// 디폴트 exception
			// 모든 예외의 최상위
			// 위치는 맨 아래!
			System.out.println(e);
		}
		
		System.out.println("end");
		
	}

}
