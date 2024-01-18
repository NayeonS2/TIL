package prac;

public class prac1 {
	class Atom {
	 Atom() { System.out.print("atom "); }
	}
	class Rock extends Atom {
	 Rock(String type) { System.out.print(type); }
	}
	public class Mountain extends Rock {
	 Mountain() {
	 super("granite ");
	 new Rock("granite ");
	 }
	}
}
