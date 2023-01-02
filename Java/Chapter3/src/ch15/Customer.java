package ch15;

// 여러 인터페이스를 구현할 수 있다!
public class Customer implements Buy, Sell{

	@Override
	public void sell() {
		
		
		System.out.println("customer sell");
	}

	@Override
	public void buy() {
		
		System.out.println("customer buy");
	}
	
	// 디폴트 메서드가 중복된 경우 둘중하나 선택 or 재정의
	@Override
	public void order() {
		
		System.out.println("customer order");
	}
	
	public void hello() {
		
		System.out.println("hello");
	}
	
	
}
