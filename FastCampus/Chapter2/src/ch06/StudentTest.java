package ch06;

// 얘는 클래스를 사용하는, 클라이언트 역할
public class StudentTest {

	public static void main(String[] args) {
		
		// 디폴트 생산자 (생성후에 매개변수 할당)
		Student studentLee = new Student();
		
		System.out.println(studentLee.showStudentInfo());
		
		
		// 매개변수 넣어서 만드는 생성자
		Student studentKim = new Student(123456, "Kim", 3);
		
		System.out.println(studentKim.showStudentInfo());
		
		
	}

}
