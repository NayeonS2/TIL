package ch01;

class OutClass{
	
	private int num = 10;
	private static int sNum = 20;
	private InClass inClass;
	
	public OutClass() {
		inClass = new InClass();
	}
	
	// 외부 클래스 변수 사용 가능
	// 스태틱 변수 사용 가능 (인스턴스보다 먼저 생성)
	
	class InClass{
		
		int iNum = 100;
		
		//인스턴스 innerclass 내부에서는 스태틱 변수 사용 불가
		//static int sInNum = 500;
		
		void inTest() {
			System.out.println("OutClass num = " +num + "(외부 클래스의 인스턴스 변수)");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수)");
			System.out.println("InClass iNum = " + iNum + "(내부 클래스의 인스턴스 변수)");

		}
	}
	
	public void usingClass() {
		inClass.inTest();
	}
	
	static class InStaticClass {
		
		int iNum = 100;
		static int sInNum = 200;
		
		// 스태틱 클래스에서 외부 클래스의 인스턴스 변수는 사용불가
		void inTest() {
			System.out.println("InClass num = " +iNum + "(내부 클래스의 인스턴스 변수)");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수)");
			System.out.println("InClass sNum = " + sInNum + "(내부 클래스의 스태틱 변수)");

		}
		
		static void sTest() {
			// 내부클래스의 인스턴스 변수 사용 불가
			//System.out.println("InClass num = " +iNum + "(내부 클래스의 인스턴스 변수)");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 스태틱 변수)");
			System.out.println("InClass sNum = " + sInNum + "(내부 클래스의 스태틱 변수)");

		}
		
	}
}


public class InnerTest {

	public static void main(String[] args) {
		
		/*
		 * OutClass outClass = new OutClass(); outClass.usingClass();
		 */
	
		OutClass.InStaticClass sInClass = new OutClass.InStaticClass();
		sInClass.inTest();
		
		// 바로호출가능
		OutClass.InStaticClass.sTest();
	}

}
