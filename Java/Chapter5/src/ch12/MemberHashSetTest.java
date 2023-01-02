package ch12;

public class MemberHashSetTest {

	public static void main(String[] args) {
		
		
		MemberHashSet memberHashSet = new MemberHashSet();
		
		Member memberLee = new Member(1001,"이순신");
		Member memberKim = new Member(1002,"김유신");
		Member memberKang = new Member(1003,"강감찬");
		
		
		memberHashSet.addMember(memberLee);
		memberHashSet.addMember(memberKim);
		memberHashSet.addMember(memberKang);
		
		// equals, hashCode 구현 후에는 동일 아이디가진 객체 안들어감
		Member memberHong = new Member(1003,"홍길동");
		memberHashSet.addMember(memberHong);
		
		// set은 들어간 순서대로 나오진 않음
		memberHashSet.showAllMember();
		
		
	}

}
