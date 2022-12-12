package ch03;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10010, "이순신");
//		customerLee.setCustomerName("이순신");
//		customerLee.setCustomerID(10010);
		customerLee.bonusPoint = 1000;
		
		System.out.println(customerLee.showCustomerInfo());
		
		
		VIPCustomer customerKim = new VIPCustomer(10020, "김유신");
//		customerKim.setCustomerName("김유신");
//		customerKim.setCustomerID(10020);
		customerKim.bonusPoint = 10000;
		
		System.out.println(customerKim.showCustomerInfo());
	
		// Customer vc = new VIPCustomer(12345, "noname");
		// 하위클래스는 상위클래스로 형변환 가능
		// but 형변환된 상위클래스의 속성만 사용가능
		
	}

}
