package ch08;

public class AutoCloseableObj implements AutoCloseable{

	@Override
	public void close() throws Exception {
		
		System.out.println("closing...");
	}

}
