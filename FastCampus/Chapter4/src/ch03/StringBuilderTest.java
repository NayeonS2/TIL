package ch03;

public class StringBuilderTest {

	public static void main(String[] args) {
		
		String java = new String("java");
		String android = new String("android");
		
		// stringbuilder는 단일 스레드에서 사용
		// stringbuffer는 멀티 스레드에서 사용
		StringBuilder buffer = new StringBuilder(java);
		
		
		System.out.println(System.identityHashCode(buffer));
		
		buffer.append(android);
		
		// 항상 같은 주소값
		System.out.println(System.identityHashCode(buffer));
		
		String test = buffer.toString();
		System.out.println(test);
	}

}
