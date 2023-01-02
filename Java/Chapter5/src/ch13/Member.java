package ch13;

import java.util.Comparator;
// 일반적으론 Comparable씀
public class Member implements Comparator<Member>{
	
	private int memberId;        //회원 아이디
	private String memberName;   //회원 이름
	
	public Member() {}
	
	public Member(int memberId, String memberName){ //생성자
		this.memberId = memberId;
		this.memberName = memberName;
	}
	
	public int getMemberId() {  //
		return memberId;
	}
	public void setMemberId(int memberId) {
		this.memberId = memberId;
	}
	public String getMemberName() {
		return memberName;
	}
	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}
	

	// hashset사용하려면 equals랑 hashCode 함수구현해야함
	// 중복 방지를 위해!
	@Override
	public int hashCode() {
		
		return memberId;
		
	}

	@Override
	public boolean equals(Object obj) {
		
		if(obj instanceof Member) {
			
			Member member = (Member)obj;
			if(this.memberId == member.memberId) {
				return true;
			}
			else {
				return false;
			}
		}
		return false;
	}
	
	
	
	@Override
	public String toString(){   //toString 메소드 오버로딩
		return memberName + " 회원님의 아이디는 " + memberId + "입니다";
	}
	
	// Comparable
//	@Override
//	public int compareTo(Member member) {
//		// 오름차순
////		if(this.memberId > member.memberId) {
////			return 1;
////		}
////		else if(this.memberId< member.memberId) {
////			return -1;
////		}
////		else {
////			return 0;
////		}
//		
//		return (this.memberId - member.memberId);
//	}

	@Override
	public int compare(Member member1, Member member2) {
		
		return (member1.memberId-member2.memberId);
		
	}
	

}
