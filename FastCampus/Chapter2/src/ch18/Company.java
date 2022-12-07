package ch18;
// 싱글톤패턴 (유일한 객체 제공시 사용)
public class Company {
	
	private static Company instance = new Company();
	
	// private 생성자 (외부에서 생성불가)
	private Company() {
		
	}
	
	// 외부에서 사용하게끔 static
	// instance는 단하나만!
	public static Company getInstance() {
		
		if(instance == null) {
			instance = new Company();
		}
		return instance;
	}
}
