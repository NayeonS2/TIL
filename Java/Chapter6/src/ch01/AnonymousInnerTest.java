package ch01;

class Outer2{
	
	int outNum = 100;
	static int sNum = 200;
	
	
	Runnable getRunnable(int i) {
		//메서드의 호출이 끝나면 메서드에 사용된 지역변수의 유효성은 사라짐
		int num = 10;
		
		
		// Local Inner Class
		
		// 익명 내부 클래스
		return new Runnable(){
			
			int localNum = 1000;
			
			@Override
			public void run() {
				//메서드 호출 이후에도 사용해야 하는 경우가 있을 수 있으므로 
				//지역 내부 클래스에서 사용하는 메서드의 지역 변수나 매개 변수는final로 선언됨
				
				// 함수 쓰는건 상관없는데 값 변경은 안됨!
				//num = 200;   //에러 남. 지역변수는 상수로 바뀜
				//i = 100;     //에러 남. 매개 변수 역시 지역변수처럼 상수로 바뀜
				System.out.println("i =" + i); 
				System.out.println("num = " +num);  
				System.out.println("localNum = " +localNum);
					
				System.out.println("outNum = " + outNum + "(외부 클래스 인스턴스 변수)");
				System.out.println("Outter.sNum = " + Outer2.sNum + "(외부 클래스 정적 변수)");

			}
			
		};
		
	}
	
	Runnable runnable = new Runnable() {

		@Override
		public void run() {
			
			System.out.println("Runnable class");
		}
		
	};
}



public class AnonymousInnerTest {

	public static void main(String[] args) {
		
		Outer2 out = new Outer2();
		Runnable runner = out.getRunnable(100);
		
		runner.run();
		
		out.runnable.run();
	}

}
