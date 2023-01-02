package ch21;

public class BreakTest {

	public static void main(String[] args) {
		
		int sum = 0;
		int num;
		
		for(num=1; ; num++) {
			sum += num;
			if(sum >= 100) {
				break;	// 얼마인 순간에 100이넘느냐를 알려면 중간에 빠져나와야함
			}
		}
		System.out.println(sum);
		System.out.println(num);
	}

}
