package school;

import java.util.ArrayList;

public class School {
	
	// 학교라는 개체는 여러개일수 없음
	// 싱글톤 패턴
	
	private static School instance = new School();
	
	private ArrayList<Student> studentList = new ArrayList<Student>();
	private ArrayList<Subject> subjectList = new ArrayList<Subject>();
	
	
	
	public ArrayList<Student> getStudentList() {
		return studentList;
	}

	public void setStudentList(ArrayList<Student> studentList) {
		this.studentList = studentList;
	}

	public ArrayList<Subject> getSubjectList() {
		return subjectList;
	}

	public void setSubjectList(ArrayList<Subject> subjectList) {
		this.subjectList = subjectList;
	}

	
	public void addStudent(Student student) {
		studentList.add(student);
	}
	
	public void addSubject(Subject subject) {
		subjectList.add(subject);
	}
	
	
	private School() {}
	
	public static School getInstance() {
		
		if(instance == null) {
			instance = new School();
		}
		return instance;
	}
}
