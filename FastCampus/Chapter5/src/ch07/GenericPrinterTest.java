package ch07;

public class GenericPrinterTest {

	public static void main(String[] args) {
		
		Powder powder = new Powder();
		// 다이아몬드 연산자 <>
		// 타입지정안하면 Object로 인식
		GenericPrinter<Powder> powderPrinter = new GenericPrinter<>();
		powderPrinter.setMaterial(powder);
		
		// 형변환이 필요없는 이유
		// T가 자동으로 powder로 바뀜
		Powder p = powderPrinter.getMaterial();
		System.out.println(powderPrinter.toString());
	
		
	}

}
