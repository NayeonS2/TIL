package ch11;

public class OperatorTest {

	public static void main(String[] args) {
		int gameScore = 150;
		//int lastScore = ++gameScore; // gameScore += 1; gameScore = gameScore + 1;
		
		int lastScore = gameScore++; // 값이 들어가고나서 ++
		
		System.out.println(lastScore); // 그래서 150
		System.out.println(gameScore); // 151
	}

}
