package ch20;

public class ArrayTest {

	public static void main(String[] args) {
		
		int[] arr = new int[10];
		int total = 0;
		
		for(int i=0, num=1; i<arr.length; i++) {
			arr[i] = num++; // 값을 넣고나서 증가
		}
		
		// 처음부터 끝까지 다돌때 주로 사용
		for(int num : arr) {
			total += num;
		}
		System.out.println(total);
		
	}

}
