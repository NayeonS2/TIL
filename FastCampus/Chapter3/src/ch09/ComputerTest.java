package ch09;

public class ComputerTest {

	public static void main(String[] args) {
		
		// 추상클래스는 new 될수없다!!
		Computer desktop = new Desktop();
		desktop.display();
	}

}
