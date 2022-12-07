package ch08;

public class Order {
	
	public String orderId;
	public String phoneNumber;
	public String address;
	public String orderDate;
	public String orderTime;
	public int price;
	public String menuId;
	
	public Order(String orderId,String phoneNumber, String address, String orderDate, String orderTime, int price, String menuId) {
		this.orderId = orderId;
		this.phoneNumber = phoneNumber;
		this.address = address;
		this.orderDate = orderDate;
		this.orderTime = orderTime;
		this.price = price;
		this.menuId = menuId;
	}
	public void orderInfo() {
		System.out.println("주문접수번호 " + orderId +"\n주문핸드폰번호 "+phoneNumber+"\n주문집주소 "+address+"\n주문날짜 "+orderDate+"\n주문시간 "+orderTime+"\n주문가격 "+price+"\n메뉴번호 "+menuId);
	}
	
}
