package ch20;
// 1. extends Thread 스레드 상속받아서 멀티스레드 생성
// 2. implements Runnable 이미 스레드 상속받았을경우
class MyThread implements Runnable{
	
	@Override
	public void run() {
		
		int i;
		for(i=1;i<=200;i++) {
			System.out.print(i+"\t");
		}
	}
	
}


public class ThreadTest {

	public static void main(String[] args) {
		System.out.println(Thread.currentThread()+" start");
		/*
		 * MyThread th1 = new MyThread(); 
		 * MyThread th2 = new MyThread();
		 * 
		 * // 두개스레드가 스위치되면서 찍힘 
		 * th1.start(); 
		 * th2.start();
		 */
		
		MyThread runnable = new MyThread(); 
		
		Thread th1 = new Thread(runnable);
		Thread th2 = new Thread(runnable);
		
		th1.start(); 
		th2.start();
		System.out.println(Thread.currentThread()+" end");
		
		// 스레드화될수있는 Runnable 인터페이스
		Runnable run = new Runnable() {
			// 바로 익명 함수 생성가능
			@Override
			public void run() {
				
				System.out.println("run");
			}
			
			
		};
		run.run();
	}

}
