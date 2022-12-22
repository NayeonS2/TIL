package ch19;

public class Latte extends Decorator{
	// 상위클래스에 디폴트 생성자가 없으면
	// 상속받는 하위클래스에서 super을 명시적으로 호출해야함!
	public Latte(Coffee coffee) {
		super(coffee);
	}
	
	
	@Override
	public void brewing() {
		
		super.brewing();
		System.out.print(" Adding Milk ");
	}
}
