package ch12;

public class Person {
	
	String name;
	int age;
	
	public Person() {
		// 다른 생성자 호출 가능
		// 만들어져있는 아래 생성자를 호출
		this("no name", 1);
		
	}
	
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	
	public void showPerson() {
		System.out.println(name + "," + age);
	}
	
	
	public Person getPerson() {
		return this;
	}
	
	
	public static void main(String[] args) {
		
		Person person = new Person();
		person.showPerson();
		
		System.out.println(person); // 아래와 같은 값
		
		Person person2 = person.getPerson();
		System.out.println(person2);
	}
	
}
