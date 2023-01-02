package ch03;

public class VIPCustomer extends Customer {
	
	double salesRatio;
	private String agentID;
	
//	public VIPCustomer() {
//		//super는 하위클래스가 상위클래스의 참조값을 가지게됨!
//		//this와 유사하게 디폴트 constructor을 불러옴
//		super(0, "no-name");	// 직접안써도 상관없음
//		
//		bonusRatio = 0.05;
//		salesRatio = 0.1;
//		customerGrade = "VIP";
//		
//		//시스템 호출시 상속 로그 찍어보기
//		System.out.println("VIPCustomer() call");
//	}
	
	public VIPCustomer(int customerID, String customerName) {
		// 상위클래스에 기본생성자가아닌 다른 생성자만 있는경우
		// super이용해 명시적으로 생성자 호출해야함!
		
		super(customerID, customerName);
		
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;
		
		System.out.println("VIPCustomer(int, String) call");
	}

	public String getAgentID() {
		return agentID;
	}

	public void setAgentID(String agentID) {
		this.agentID = agentID;
	}
	
	
}
