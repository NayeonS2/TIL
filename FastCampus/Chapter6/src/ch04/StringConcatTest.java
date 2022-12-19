package ch04;

public class StringConcatTest {

	public static void main(String[] args) {
		
		String s1 = "Hello";
		String s2 = "World";
		
		
		StringConcatImpl strImpl = new StringConcatImpl();
		strImpl.makeString(s1, s2);
		
		// 클래스 없이 람다식 가능한 것이아니라
		// 익명 내부 클래스가 만들어지는것 (익명 객체 생성)
		StringConcat concat = (s,v) -> System.out.println(s + "," + v);
		concat.makeString(s1, s2);
		

	}

}
