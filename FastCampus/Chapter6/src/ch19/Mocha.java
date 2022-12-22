package ch19;

public class Mocha extends Decorator {

	public Mocha(Coffee coffee) {
		super(coffee);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void brewing() {
		
		super.brewing();
		System.out.print(" Adding Mocha Syrup ");
	}
	
}
