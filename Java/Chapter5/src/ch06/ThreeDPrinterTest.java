package ch06;

public class ThreeDPrinterTest {

	public static void main(String[] args) {
		
		
		Powder powder = new Powder();
		ThreeDPrinter3 printer = new ThreeDPrinter3();
		
		printer.setMaterial(powder);
		
		// 강제 형변환 필요 (제네릭 프로그래밍 등장 이유)
		Powder p = (Powder)printer.getMaterial();
	}

}
