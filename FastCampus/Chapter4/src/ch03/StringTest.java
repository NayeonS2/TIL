package ch03;

public class StringTest {

	public static void main(String[] args) {
		
		String java = new String("java");
		String android = new String("android");
		
		System.out.println(System.identityHashCode(java));
		java = java.concat(android);
		
		System.out.println(java);
		// 주소값이 다름! (새로운 메모리가 생성됨)
		System.out.println(System.identityHashCode(java));
		
		
	}

}
