package ch15;

public class CustomerTest {

	public static void main(String[] args) {
		
		Customer customer = new Customer();
		customer.buy();
		customer.sell();
		customer.order();
		customer.hello();
		
		Buy buyer = customer;
		buyer.buy();
		//가상 메서드에 의해 재정의된 메서드가 호출됨!
		buyer.order();
		
		
		Sell seller = customer;
		seller.sell();
		//가상 메서드에 의해 재정의된 메서드가 호출됨!
		seller.order();
	}

}
