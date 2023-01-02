package ch09;

// 추상 메서드 추상 클래스
// 추상클래스는 상속을 위한것!!
public abstract class Computer {
	
	// 상속을 위한 추상 메서드
	// 추상메서드는 기능 정의없이 선언만 한 것
	// 상속을 받는 클래스가 구현하도록 놔둠!
	public abstract void display();
	public abstract void typing();
	
	public void turnOn() {
		
		System.out.println("전원을 켭니다");
	}
	
	public void turnOff() {
		
		System.out.println("전원을 끕니다");
	}
}
