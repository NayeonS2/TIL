package ch21;

public class JoinTest extends Thread{
	
	int start;
	int end;
	int total;
	
	public JoinTest(int start, int end) {
		this.start = start;
		this.end = end;
	}
	
	public void run() {
		
		int i;
		for(i=start; i<=end; i++) {
			
			total += i;
		}
	}
	
	
	public static void main(String[] args) {
		
		
		
		JoinTest jt1 = new JoinTest(1,50);
		JoinTest jt2 = new JoinTest(51,100);
	
		jt1.start();
		jt2.start();
		
		
		
		try {
			// 수행끝날때까지 기다림
			jt1.join();
			jt2.join();
			// join 쓸땐 InterreuptedException 처리 필수
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		// 값을 계산하는 중
		int lastTotal = jt1.total + jt2.total;
		
		System.out.println("jt1.total = "+jt1.total);
		System.out.println("jt2.total = "+jt2.total);
		System.out.println("lastTotal = "+ lastTotal);
	
	
	}

}
