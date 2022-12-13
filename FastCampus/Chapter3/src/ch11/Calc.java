package ch11;
// 인터페이스는 리모콘 같은 것!
// 인터페이스는 구현 코드가 없음
// 데베마다 다른 로직의 메서드
// 그 내부를 사용자는 알 필요가 없음
// 인터페이스만 보고 사용하는 것 !
public interface Calc {
	
	double PI = 3.14;
	int ERROR = -99999999;
	
	int add(int num1, int num2);
	int substract(int num1, int num2);
	int times(int num1, int num2);
	int divide(int num1, int num2);
	
}
