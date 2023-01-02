package ch05;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class ArrayListStreamTest {

	public static void main(String[] args) {
		
		List<String> sList = new ArrayList<String>();
		
		sList.add("Tomas");
		sList.add("Edward");
		sList.add("Jack");
		// collection메서드는 스트림 호출 가능
		Stream<String> stream = sList.stream();
		stream.forEach(s->System.out.println(s));
		// 연산이 객체를 바꾸진 않음
		sList.stream().sorted().forEach(s->System.out.println(s));
		sList.stream().map(s->s.length()).forEach(n->System.out.println(n));
		sList.stream().filter(s->s.length()>=5).forEach(s->System.out.println(s));
	
	}

}
