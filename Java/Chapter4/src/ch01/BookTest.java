package ch01;


class Book{
	
	private String title;
	private String author;
	
	public Book(String title, String author) {
		this.title = title;
		this.author = author;
	}
	
	// 오버라이딩
	@Override
	public String toString() {
		return title + "," + author;
	}
	
	
}


public class BookTest {
	
	public static void main(String[] args) {
		
		Book book = new Book("데미안", "헤르만 헤세");
		
		System.out.println(book);
		
		// 인스턴스지만 문자열 값이 나옴
		// 이미 toString이 오버라이딩된것
		String str = new String("test");
		System.out.println(str.toString());
	}

}
