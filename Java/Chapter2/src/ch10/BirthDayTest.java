package ch10;

public class BirthDayTest {

	public static void main(String[] args) {
		
		// 접근제어기능 -> 정보보호
		
		BirthDay date = new BirthDay();
		date.setYear(2019);
		date.setMonth(12);
		date.setDay(30);
		
		date.showDate();
	}

}
