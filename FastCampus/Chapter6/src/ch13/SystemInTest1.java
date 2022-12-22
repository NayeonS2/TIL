package ch13;

import java.io.IOException;
import java.io.InputStreamReader;

public class SystemInTest1 {

	public static void main(String[] args) {
		
		System.out.println("알파벳 하나를 쓰고 [Enter]를 누르세요");
		
		int i;
		
		try {
			// 한 바이트씩 읽어서 한글은 깨짐! (보조스트림으로 감싸야함)
			InputStreamReader irs = new InputStreamReader(System.in);
			while((i = irs.read()) != '\n') {
				//System.out.println(i);
				System.out.print((char)i);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
