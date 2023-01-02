package ch04;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customerLee = new Customer(10010, "이순신");
//		customerLee.setCustomerName("이순신");
//		customerLee.setCustomerID(10010);
		
		customerLee.bonusPoint = 1000;
		int price = customerLee.calcPrice(1000);
		System.out.println(customerLee.showCustomerInfo() + price);
		
		
		VIPCustomer customerKim = new VIPCustomer(10020, "김유신");
//		customerKim.setCustomerName("김유신");
//		customerKim.setCustomerID(10020);
		
		customerKim.bonusPoint = 10000;
		//VIPCustomer에서 재정의한 calcPrice 호출
		price = customerKim.calcPrice(1000);
		System.out.println(customerKim.showCustomerInfo() + price);
	
		// 하위클래스는 상위클래스로 형변환 가능
		// but 형변환된 상위클래스의 속성만 사용가능
		Customer vc = new VIPCustomer(12345, "noname");
		
		// VIPCustomer의 calcPrice가 호출
		// 가상메서드의 원리
		// 항상 인스턴스의 메서드가 호출
		System.out.println(vc.calcPrice(1000));
		
		
	}

}
