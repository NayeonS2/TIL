package ch08;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileExceptionHandling {

	public static void main(String[] args) {
		
		// try 구문안에 쓰면 close가 같이 된다는 의미
		// autoclosable
		// 자바7부터지원
		try(FileInputStream fis = new FileInputStream("a.txt")) {

			System.out.println("read");
			
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		System.out.println("end");
	}

}
