package ch15;

import java.util.ArrayList;

public class Shelf {
	
	protected ArrayList<String> shelf;
	
	// 생성자가 호출될때 멤버변수 초기화
	public Shelf() {
		shelf = new ArrayList<String>();
		
	}
	
	public ArrayList<String> getShelf() {
		return shelf;
	}
	
	public int getCount() {
		return shelf.size();
	}
	
	
	
	
}
