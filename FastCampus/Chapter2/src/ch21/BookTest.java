package ch21;

public class BookTest {

	public static void main(String[] args) {
		//객체 배열은 바로 객체 5개가 잡히는게 아님!
		Book[] library = new Book[5];
		
//		for(int i=0; i<library.length; i++) {
//			System.out.println(library[i]); //null
//			
//		}
		
		library[0] = new Book("태백산맥1", "조정래");
		library[1] = new Book("태백산맥2", "조정래");
		library[2] = new Book("태백산맥3", "조정래");
		library[3] = new Book("태백산맥4", "조정래");
		library[4] = new Book("태백산맥5", "조정래");
		
		for(Book book : library) {
			System.out.println(book);
			book.showInfo();
		}
		
	}

}
