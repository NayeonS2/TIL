package ch09;

public class Student {
	
	int studentId;
	String studentName;
	
	Subject korea; // 만들어놓은 참조 변수 사용
	Subject math;
	
	Student(int studentId, String studentName) {
		this.studentId = studentId;
		this.studentName = studentName;
		
		korea = new Subject(); // 생성자로 생성해줘야 사용가능!!!
		math = new Subject();
		
	}
	
	public void setKoreaSubject(String name, int score) {
		korea.subjectName = name;
		korea.score = score;
	}
	
	public void setMathSubject(String name, int score) {
		math.subjectName = name;
		math.score = score;
	}
	
	public void showScoreInfo() {
		int total = korea.score + math.score;
		System.out.println(studentName+"학생의 총점은"+total+"점 입니다.");
	}
	
	
}
