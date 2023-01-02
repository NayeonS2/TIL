package ch08;

public class Person {

	public int tall;
	public int weight;
	public String sex;
	public String name;
	public int age;
	
	public Person(int tall, int weight, String sex,String name, int age) {
		this.tall = tall;
		this.weight = weight;
		this.sex = sex;
		this.name = name;
		this.age = age;
		
	}
	
	public void showInfo() {
		System.out.println("키가"+tall+"이고 몸무게가 "+ weight + "킬로인" + sex + " 이 있습니다. 이름은 "+name+"이고 나이는 "+age+"세 입니다.");
	}
}
