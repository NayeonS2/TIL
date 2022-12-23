package ch23;

import java.util.ArrayList;

class FastLibrary{
	
	public ArrayList<String> shelf = new ArrayList();
	
	public FastLibrary() {
		
		shelf.add("태백산맥1");
		shelf.add("태백산맥2");
		shelf.add("태백산맥3");
	
		
	}
	
	public synchronized String lendBook() throws InterruptedException {
		// 메서드 수행중인 스레드 정보
		Thread t = Thread.currentThread();
		while(shelf.size()==0) {
			// 책없으면 기다려
			// wait은 object메서드
			System.out.println(t.getName()+" waiting start");
			wait();
			System.out.println(t.getName()+" waiting end");
		}
		
		
		// 책이없는데 가져가려하면 에러가남
		
		if(shelf.size()>0) {
			String book = shelf.remove(0);
			System.out.println(t.getName()+" : "+book+" lend");
			return book;
		}
		else return null;
	}
	
	public synchronized void returnBook(String book) {
		
		Thread t = Thread.currentThread();
		
		shelf.add(book);
		// notify도 object 메서드
		notifyAll();
		System.out.println(t.getName()+" : "+book+" return");

	}
}

// 수행할 스레드
class Student extends Thread{
	
	public Student(String name) {
		super(name);
	}
	public void run() {
		
		try {
			String title = LibraryMain.library.lendBook();
			
			if (title==null) {
				System.out.println(getName()+" 빌리지 못함");
				return;
			}
			
			sleep(5000);
			
			LibraryMain.library.returnBook(title);
		}catch(InterruptedException e) {
			System.out.println(e);
		}
	}
}



public class LibraryMain {
	//공유자원
	public static FastLibrary library = new FastLibrary();
	
	public static void main(String[] args) {
		
		// 스레드 실행
		Student std1 = new Student("std1");
		Student std2 = new Student("std2");
		Student std3 = new Student("std3");
		Student std4 = new Student("std4");
		Student std5 = new Student("std5");
		Student std6 = new Student("std6");
		
		std1.start();
		std2.start();
		std3.start();
		std4.start();
		std5.start();
		std6.start();
	}

}
