package ch05;

import java.util.Arrays;
import java.util.stream.IntStream;

public class IntArrayStreamTest {

	public static void main(String[] args) {
		
		int[] arr = {1,2,3,4,5};
		
		for(int num:arr) {
			System.out.println(num);
		}
		
		// 스트림 생성
		// 자료처리에 대한 추상화
		// 일관적 기능
		IntStream is = Arrays.stream(arr);
		is.forEach(n->System.out.println(n));
		
		// 스트림은 재사용 불가!
		int sum = Arrays.stream(arr).sum();
		System.out.println(sum);
	
		
	}

}
