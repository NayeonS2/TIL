package ch06;
import java.util.Arrays;
import java.util.function.BinaryOperator;

// 람다식으로 구현할 내용이 너무 많으면 BinaryOperator사용해서 구현
class CompareString implements BinaryOperator<String>{

	@Override
	public String apply(String s1, String s2) {
		{if(s1.getBytes().length >= s2.getBytes().length) return s1;
		else return s2;
	}
	}
}



// reduce이용해서 스트림에서 제공되는 연산외에 직접 구현가능!

public class ReduceTest {

	public static void main(String[] args) {
		
		String greetings[] = {"안녕하세요~~","hello", "good morning","반갑습니당"};
		
		System.out.println(Arrays.stream(greetings).reduce("",(s1,s2)->
		
			{if(s1.getBytes().length >= s2.getBytes().length) return s1;
			else return s2;}
		
				));
		// binaryoperator로 구현한 클래스를 넣어주면됨
		String str = Arrays.stream(greetings).reduce(new CompareString()).get();
		System.out.println(str);


}}