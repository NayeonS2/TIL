package ch10;

public abstract class Car {
	
	public abstract void drive();
	public abstract void stop();
	public abstract void wiper();
	
	public void startCar() {
		System.out.println("시동을 겁니다");
	}
	
	public void turnOff() {
		System.out.println("시동을 끕니다");
	}
	
	// 구현이 안된게 아님!
	// 추상메소드가 아님
	// 하위에서 정의안해도 에러 안남
	// 재정의는 필요할때만!
	public void washCar() {}
	
	
	// 템플릿 메소드
	// 하위클래스에서 재정의 불가!
	// 순서가 지켜져야할 메소드에 사용
	final public void run() {
		startCar();
		drive();
		wiper();
		stop();
		turnOff();
		washCar();
	}
	
}
