package ch22;

class Bank{
	
	private int money = 10000;
	
	// 동기화 필요한 메서드에 synchronized
	// 하나메서드가 수행이끝난뒤에 다음 메서드가 실행됨
	public void saveMoney(int save) {
		
		int m = getMoney();
		
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		setMoney(m + save);
	}
	
	public void minusMoney(int minus) {
		
		int m = getMoney();
		
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		setMoney(m - minus);
	}
	
	
	public int getMoney() {
		return money;
	}

	public void setMoney(int money) {
		this.money = money;
	}
	
	
}

// 스레드 생성
class Park extends Thread{
	
	public void run() {
		// 어떤 resource에 sync걸건지 지정
		synchronized (SyncMain.myBank) {
			System.out.println("start save");
			SyncMain.myBank.saveMoney(3000);
			System.out.println("saveMoney(3000) : "+SyncMain.myBank.getMoney());
		}
		
	}
}

class ParkWife extends Thread{
	
	public void run() {
		synchronized (SyncMain.myBank) {
			System.out.println("start minus");
			SyncMain.myBank.minusMoney(1000);
			System.out.println("minusMoney(1000) : "+SyncMain.myBank.getMoney());
		}
		
	}
}



public class SyncMain {
	// shared resource
	public static Bank myBank = new Bank();	
	
	
	public static void main(String[] args) {
		
		Park p = new Park();
		p.start();
		
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		ParkWife pw = new ParkWife();
		pw.start();
		
	}

}
