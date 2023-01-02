package ch11;

public class MakeReport {
	
	// 메모리 오버헤드 피하기 위해 buffer 사용
	StringBuffer buffer = new StringBuffer();
	
	private String line = "===========================================\n";
	private String title = "이름\t 주소 \t\t 전화번호 \n";
	private void makeHeader() {
		
		buffer.append(line);
		buffer.append(title);
		buffer.append(line);
		
	}
	
	private void generateBody() {
		
		buffer.append("James \t");
		buffer.append("Seoul Korea \t");
		buffer.append("010-2222-3333\n");
		
		buffer.append("Tomas \t");
		buffer.append("NewYork US \t");
		buffer.append("010-7777-0987 \n");
	}
	
	private void makeFooter() {
		
		buffer.append(line);
	}
	
	// 세부 메소드는 private으로하고 public은 getReport하나만!
	// 클라이언트 쪽에서는 알 필요가없기때문에 private으로 hide
	public String getReport() {
		makeHeader();
		generateBody();
		makeFooter();
		return buffer.toString();
	}
}
