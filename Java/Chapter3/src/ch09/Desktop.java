package ch09;

public class Desktop extends Computer {

	@Override
	public void display() {
		
		System.out.println("Desktop display");
	}

	@Override
	public void typing() {
		
		System.out.println("Desktop typing");
		
	}
	
	// 메서드 재정의도 가능
	@Override
	public void turnOff() {
		
		System.out.println("Desktop turnoff");
		
	}
	
	
	
	

}
