package ch16;

public class Employee {
	// static 변수
	private static int serialNum = 1000;
	
	
	private int employeeId;
	private String employeeName;
	private String department;
	
	
	// 객체생성시 초기화작업은 생성자에서!
	public Employee() {
		
		serialNum++;
		
		// 사원마다 다른값이어야하니 멤버변수에 복사!
		employeeId = serialNum;
	}
	
	
	
	public static int getSerialNum() {
		// 지역변수는 상관없음
		//int i = 0;
		// 인스턴스가 생성되지 않은 상태에선 인스턴스 변수 사용 x
		//employeeName = "Lee";
		
		return serialNum;
	}



	public int getEmployeeId() {
		return employeeId;
	}
	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}
	public String getEmployeeName() {
		return employeeName;
	}
	public void setEmployeeName(String employeeName) {
		this.employeeName = employeeName;
	}
	public String getDepartment() {
		return department;
	}
	public void setDepartment(String department) {
		this.department = department;
	}
	
	
	
}
