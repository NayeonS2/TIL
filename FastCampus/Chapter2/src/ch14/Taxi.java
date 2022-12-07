package ch14;

public class Taxi {
	
	String taxiCompany;
	int passengerCount;
	int money;
	
	public Taxi(String taxiCompany) {
		this.taxiCompany = taxiCompany;
	}
	
	public void take(int money) {
		this.money += money;
		
	}
	
	public void showTaxiInfo() {
		System.out.println(taxiCompany +" 수입은 "+money+"원 입니다.");
	}
	
	
}
