package ch13.web.userinfo;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import ch13.domain.userinfo.UserInfo;
import ch13.domain.userinfo.dao.UserInfoDao;
import ch13.domain.userinfo.dao.mysql.UserInfoMySqlDao;
import ch13.domain.userinfo.dao.oracle.UserInfoOracleDao;

public class UserInfoClient {

	public static void main(String[] args) throws IOException {
		// 파일열기
		FileInputStream fis = new FileInputStream("db.properties");
		
		// key=value 형태를 pair로 읽어들일 수 있음
		Properties prop = new Properties();
		prop.load(fis);
		
		// key에 대한 value값 
		String dbType = prop.getProperty("DBTYPE");
		
		UserInfo userInfo = new UserInfo();
		userInfo.setUserID("12345");
		userInfo.setPassword("!@##$%");
		userInfo.setUserName("Lee");
		
		// 인터페이스 타입으로 선언
		UserInfoDao userInfoDao = null;
		
		if( dbType.equals("ORACLE")) {
			
			userInfoDao = new UserInfoOracleDao();
		}
		else if( dbType.equals("MYSQL")) {
			
			userInfoDao = new UserInfoMySqlDao();
		}
		else {
			
			System.out.println("db error");
			return;
		}
		
		
		userInfoDao.insertUserInfo(userInfo);
		userInfoDao.updateUserInfo(userInfo);
		userInfoDao.deleteUserInfo(userInfo);
	}

}
