package ch13;

import java.util.Comparator;
import java.util.TreeSet;

class MyCompare implements Comparator<String> {

	@Override
	public int compare(String s1, String s2) {
		// 내림차순으로 변경
		return s1.compareTo(s2) * (-1);
	}
	
}

public class MemberTreeSetTest {

	public static void main(String[] args) {
		
//		TreeSet<String> set = new TreeSet<String>();
//		
//		set.add("홍길동");
//		set.add("강감찬");
//		set.add("이순신");
//		
//		// 정렬되어 나옴
//		System.out.println(set);
		
		
//		
//		MemberTreeSet memberTreeSet = new MemberTreeSet();
//		Member memberHong = new Member(1004,"홍길동");
//		Member memberLee = new Member(1001,"이순신");
//		Member memberKim = new Member(1002,"김유신");
//		Member memberKang = new Member(1003,"강감찬");
//		
//		memberTreeSet.addMember(memberHong);
//		memberTreeSet.addMember(memberLee);
//		memberTreeSet.addMember(memberKim);
//		memberTreeSet.addMember(memberKang);
//		
//		// equals, hashCode 구현 후에는 동일 아이디가진 객체 안들어감
//		
//		
//		
//		// set은 들어간 순서대로 나오진 않음
//		memberTreeSet.showAllMember();
		
		TreeSet<String> set = new TreeSet<String>(new MyCompare());
		set.add("Park");
		set.add("Kim");
		set.add("Lee");
		
		// 순서대로 나옴
		// String엔 Comparable이 이미 구현된 상태
		System.out.println(set);
	}

}
