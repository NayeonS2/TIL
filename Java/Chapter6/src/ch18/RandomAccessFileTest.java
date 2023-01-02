package ch18;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;

public class RandomAccessFileTest {

	public static void main(String[] args) throws IOException {
		
		RandomAccessFile rf = new RandomAccessFile("random.txt", "rw");
		
		// 4바이트
		rf.writeInt(100);
		System.out.println("pos: "+rf.getFilePointer());
		// 8바이트
		rf.writeDouble(3.14);
		System.out.println("pos: "+rf.getFilePointer());
		// 3바이트 * 5 + 널키트 2바이트
		rf.writeUTF("안녕하세요");
		System.out.println("pos: "+rf.getFilePointer());
		
		// 읽기전에 맨앞으로 가라!
		rf.seek(0);
		
		int i = rf.readInt();
		double d = rf.readDouble();
		String str = rf.readUTF();
		
		System.out.println(i);
		System.out.println(d);
		System.out.println(str);
	}

}
