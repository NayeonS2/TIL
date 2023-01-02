package ch02;

public class EqualsTest {

	public static void main(String[] args) throws CloneNotSupportedException {
		
		
		Student std1 = new Student(100, "Lee");
		Student std2 = new Student(100, "Lee");
		
		// 물리적으론 다름
		System.out.println(std1 == std2);
		
		// 논리적으로 같음 by studentNum
		System.out.println(std1.equals(std2));
		
		// 논리적으로 같기때문에 같은 해쉬값
		System.out.println(std1.hashCode());
		System.out.println(std2.hashCode());
		
		// 실제 해시는 다름
		System.out.println(System.identityHashCode(std1));
		System.out.println(System.identityHashCode(std2));
		
		String str1 = new String("abc");
		String str2 = new String("abc");
		
		System.out.println(str1.equals(str2));
		
		System.out.println(str1.hashCode());
		System.out.println(str2.hashCode());
		
		
		std1.setStudentName("Kim");
		// 이름바꾼것도 그대로 복제됨
		Student copyStudent = (Student)std1.clone();
		System.out.println(copyStudent.toString());
	}

}
