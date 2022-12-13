package ch15;

public interface Queue {
	
	void enQueue(String title);
	// 꺼낼땐 책 이름 반환
	String deQueue();
	
	int getSize();
}
