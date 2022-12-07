package ch06;

// 얘는 클래스 생성만 담당
public class Student {
	
	public int studentNumber;
	public String studentName;
	public int grade;
	// 객체가 만들어질때 자동으로 초기화됨
	
	public Student() {}
	// 직접 생산자 만들기
	public Student(int studentNumber, String studentName, int grade) {
		
		this.studentNumber = studentNumber;
		this.studentName = studentName;
		this.grade = grade;
	}
	
	
	public String showStudentInfo() {
		
		return studentName + "학생의 학번은" + studentNumber + "이고" + grade +"학년입니다.";
		
	}
}
