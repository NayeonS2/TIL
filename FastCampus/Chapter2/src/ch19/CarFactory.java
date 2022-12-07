package ch19;

public class CarFactory {
	
	private static CarFactory factory = new CarFactory();
	
	private CarFactory() {
		
	}
	
	public static CarFactory getInstance() {
		
		if(factory == null) {
			factory = new CarFactory();
		}
		return factory;
	}
	
	public Car createCar() {
		Car car = new Car();
		return car;
	}
}
