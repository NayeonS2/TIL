import ch16.Employee;

public class EmployeeTest {

	public static void main(String[] args) {
		
		Employee employeeLee = new Employee();
		
		employeeLee.setEmployeeName("이순신");
		
		//System.out.println(employeeLee.serialNum);
		// static변수는 클래스명과함께 많이 사용!
		System.out.println(Employee.getSerialNum());
		
		Employee employeeKim = new Employee();
		employeeKim.setEmployeeName("김유신");
		//employeeKim.serialNum++;
		
		//둘다 1이 증가함 -> 같은 메모리 공유!
//		System.out.println(employeeLee.serialNum);
//		System.out.println(employeeKim.serialNum);
		
		
		System.out.println(employeeLee.getEmployeeName()+"님의 사번은 "+employeeLee.getEmployeeId());
		System.out.println(employeeKim.getEmployeeName()+"님의 사번은 "+employeeKim.getEmployeeId());

	}

}
