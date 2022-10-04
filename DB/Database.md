# Database

## Database 정의
- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 검색, 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
  - 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
  - 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜 놓은 자료의 집합체
- Database를 조작하는 프로그램 = DBMS(Database Management System)
  - Oracle, MySQL, SQLite
  - DBMS에서 Database를 조작하기 위해 사용하는 언어 : SQL
- 웹 개발에서 대부분 DB는 '관계형 데이터베이스 관리 시스템(RDBMS)'을 사용하여 SQL로 데이터와 프로그래밍을 구성

---
# RDB

## RDB 란
- Relational Database(관계형 데이터베이스)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화
- 자료를 여러 테이블로 나누어 관리, 테이블간 관계를 설정해 여러 데이터를 쉽게 조작 가능
- SQL을 사용하여 데이터를 조회, 조작

## RDB 기본 구조
### 스키마(Schema)
- 테이블의 구조(Structure)
- 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술

### 테이블(Table)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름
1. 필드(field)
- 속성, 컬럼(Column)
2. 레코드(record)
- 튜플, 행(Row)
3. PK (Primary Key)
- 기본키
- 각 레코드의 고유한 값 (각 데이터를 구분할 수 있는 고윳값)
- 기술적으로 다른 항목과 절대 중복 불가한 단일 값(unique)

## 관계형 DB의 이점
- 데이터를 직관적으로 표현
- 관련 각 데이터에 쉽게 접근 가능
- 대량 데이터도 효율적 관리

## RDBMS
- Relational Database Management System (관계형 데이터베이스 관리 시스템)
- 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램
- ex) **SQLite**, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등

## SQLite
- 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
- 안드로이드, iOS, macOS에 기본적으로 탑재
- 임베디드 소프트웨어에서도 많이 활용
- 오픈소스 프로젝트이기때문에 자유롭게 사용가능
- 단점
  - 대규모 동시 처리작업은 적합X
  - 다른 RDBMS에서 지원하는 SQL기능을 지원하지 않을 수 있음
- 학습 이유
  - 어떤 환경에서나 실행가능한 호환성
  - 데이터 타입이 비교적 적고 강하지 않기 때문에 유연한 학습 환경 제공
  - Django Framework 기본 데이터베이스

---

# SQL

## SQL 이란
- "Structured Query Language"
- RDBMS의 데이터를 관리하기 위해 설계된 특수 목적 프로그래밍 언어
- RDBMS에서 데이터베이스 스키마를 생성 및 수정 가능
- 테이블에서의 자료 검색 및 관리 가능
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리하도록 할 수 있음
- 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택

## SQL 정리
- SQL은 데이터베이스와 상호작용하는 방법

---
# SQL Commands
1. DDL (Data Definition Language)
2. DML (Data Manipulation Language)
3. DCL (Data Control Language)


---
# SQL Syntax

- 모든 SQL문(statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작
- 하나의 statement는 **세미콜론(;)**으로 끝남
  - 세미콜론은 각 SQL문을 구분하는 표준 방법
- SQL 키워드는 대소문자 구분 X
  - 하지만 대문자 작성 권장

## Statement & Clause
- Statement (문)
  - 독립적으로 실행가능한 완전한 코드 조각
  - statement는 clause로 구성
- Clause (절)
  - statement의 하위 단위

---

# DDL
- "Data definition"
- SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법 학습
- 테이블 구조를 관리
  - CREATE, ALTER, DROP

# CREATE TABLE statement
- "Create a new table in the database."
- 데이터베이스에 새 테이블 만듦
- id 컬럼은 우리가 직접 기본키 역할의 컬럼을 정의하지 않으면 자동으로 **rowid** 라는 컬럼으로 만들어짐
```sql
CREATE TABLE table_name (
    column_1 data_type constraints, -- 컬럼 정의 (스키마)
    column_2 data_type constraints,
    column_3 data_type constraints
);
```
```sql
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

## SQLite Data Types
### Data Types 종류
1. NULL
   - NULL value
   - 정보가 없거나 알 수 없음 (missing information or unknown)
2. INTEGER
   - 정수
   - 크기에 따라 0,1,2,3,4,6 또는 8바이트와 같은 가변 크기를 가짐
3. REAL
   - 실수
   - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
   - 문자 데이터
5. BLOB (Bianary Large Object)
   - 입력된 그대로 저장된 데이터 덩어리 (대용 타입x)
   - 바이너리 등 멀티미디어 파일
   - ex) 이미지 데이터

- [참고]
1. Boolean type
   - SQLite에는 별도의 Boolean 타입이 없음
   - Boolean값은 정수 0(false)과 1(true)로 저장됨
2. Date & Time Datatype
   - SQLite에는 날짜 및 시간을 저장하기 위한 타입 x
   - SQLite의 built-in "Date And Time Functions"으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
3. Binary Data
   - 데이터의 저장과 처리를 목적으로 0과 1의 이진형식으로 인코딩 된 파일
   - 기본적으로 컴퓨터의 모든 데이터는 binary data
   - 다만, 이를 필요에 따라 텍스트 타입으로 변형해서 사용

### SQLite는 다음 규칙을 기반으로 데이터 타입을 결정
- 값에 둘러싸는 따옴표와 소수점 또는 지수가 없으면 -> INTEGER
- 값이 작은 따옴표나 큰따옴표로 묶이면 -> TEXT
- 값에 따옴표나 소수점, 지수가 없으면 -> REAL 
- 값이 따옴표 없이 NULL이면 -> NULL

### SQLite Datatypes 특징
- SQLite는 다른 모든 SQL 데이터베이스 엔진(MySQL, PostgreSQL 등)의 정적이고 엄격한 타입(static, rigid typing)이 아닌
- **"동적 타입 시스템(dynamic type system)"**을 사용
  - 컬럼에 선언된 데이터 타입에 의해서가 아닌, **컬럼에 저장된 값에 따라 데이터 타입이 결정**

- 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨
  - 동일 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정되고, 문자 '1'을 넣을 경우는 TEXT 타입으로 지정됨
  - 이러한 SQLite의 동적 타입 시스템을 사용하면 기존에 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행 가능
  - 게다가 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일 방식으로 작동
  - 다만 이는 다른 데이터베이스와의 호환성 문제가 있기에, 테이블 생성시 결국 **데이터 타입을 지정하는 것을 권장**!

- 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환
  - TEXT 타입 컬럼에 정수 1을 저장하면 문자 타입 '1'로 저장됨
  - 허용 가능 타입 변환
  - <img src="./DB_img/dt_type_table.png">

- [참고] "static, rigid typing" 데이터베이스
  - statically, rigidly typed databases 라고도 부름
  - 저장되는 값의 데이터 타입은 컬럼에 선언된 데이터 타입에 의해 결정
  - ```sql
      CREATE TABLE my_table(
        a INTEGER NOT NULL,
        b TEXT NOT NULL,
      );
    ```
  - a 컬럼에 '123', b 컬럼에 456 데이터를 삽입하려는 경우, 삽입 수행 전에 문자열 '123'd을 정수 123으로, 정수 456을 문자열 '456'으로 변환

### Type Affinity

<img src="./DB_img/Type_Affinity.png">

- "타입 선호도"
- 특정 컬럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC
- 타입 선호도 존재 이유
  - 다른 데이터베이스 엔진 간의 **호환성** 최대화
  - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

## Constraints
### 1. NOT NULL
- 컬럼이 NULL 값을 허용하지 않도록 지정
- 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함
### 2. UNIQUE
- 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
```sql
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```
### 3. PRIMARY KEY
- 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
- 각 테이블에는 하나의 기본 키만 있음
- 암시적으로 NOT NULL 제약 조건이 포함됨
- INTEGER 타입에만 사용 가능 (INT BIGINT 등 불가능)
```sql
CREATE TABLE table_name (
    id INTEGER PRIMARY KEY,
    ..
);
```
### 4. AUTOINCREMENT
- 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
- INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
- Django에서 테이블 생성시 id컬럼에 기본적으로 사용하는 제약조건
```sql
CREATE TABLE table_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ..
);
```

### rowid의 특징
- 테이블 생성시 마다 rowid라는 암시적 자동 증가 컬럼이 자동 생성
- 테이블 행을 고유하게 식별하는 64비트 부호있는 정수 값
- 테이블에 새 행 삽입시 마다 정수 값을 자동으로 할당
  - 값은 1부터
  - 데이터 삽입시에 rowid또는 INTEGER PRIMARY KEY컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동 할당 (AUTOINCREMENT 관계없이)
- 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭 (alias)이 됨
- 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가능
- 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용
- 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러 발생
- 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을 재사용하려고 시도 (AUTOINCREMENT가 없다면)


# ALTER TABLE
- "Modify the structure of an existing table."
- 기존 테이블의 구조를 수정(변경)
- SQLite의 ALTER TABLE문을 사용하면 기존 테이블을 다음과 같이 변경 가능
  - **Rename** a table (테이블명 변경)
  - **Rename** a column (컬럼명 변경)
  - **Add** a new column to a table (새 컬럼 추가)
  - **Delete** a column (컬럼 삭제)

```sql
-- 1. Rename a table
ALTER TABLE table_name RENAME TO new_table_name;
-- 예시
ALTER TABLE contacts RENAME TO new_contacts;

-- 2. Rename a column
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
-- 예시
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 3. Add a new column to a table
ALTER TABLE table_name ADD COLUMN column_definition;
-- 예시
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;

-- 4. Delete a column
ALTER TABLE table_name DROP COLUMN column_name;
-- 예시
ALTER TABLE new_contacts DROP COLUMN address;
```

> ALTER TABLE ADD COLUMN에서 만약 테이블에 기존 데이터가 있을 경우 에러 발생
- ```sql
    Cannot add NOT NULL column with default value NULL
  ```
- 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기에 NULL이 작성됨
- 그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기때문에 기본 값 없이는 추가될 수 없다는 에러 발생
- **DEFAULT** 제약 조건 (column 제약조건 중 하나로, 데이터 추가할 때 값을 생략 시에 기본값을 설정) 을 사용하여 해결 가능
- ```sql
    ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
  ```
- 이렇게 하면 address 컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼 값은 'no address'가 됨

> ALTER TABLE DROP COLUMN 에서 삭제하지 못하는 경우 존재
- 컬럼이 다른 부분에서 참조되는 경우
  - FOREIGN KEY(외래키) 제약 조건에서 사용되는 경우
  - PRIMARY KEY인 경우
  - UNIQUE 제약 조건이 있는 경우
  - ```sql
      ALTER TABLE new_contacts DROP COLUMN email;
      Cannot drop UNIQUE column: "email"
    ```


# DROP TABLE
- "Remove a table from the database."
- 데이터베이스에서 테이블을 제거
```sql
DROP TABLE table_name;
-- 예시
DROP TABLE new_contacts;
```
- 존재하지 않는 테이블을 제거하면 SQLite에서 오류 발생
```sql
no such table: table_name
```
- 한번에 하나의 테이블만 삭제 가능
- 여러 테이블 제거하려면 여러 DROP TABLE 문 실행
- DROP TABLE 문은 실행 취소하거나 복구 불가
- 각별히 주의하여 수행

# DDL 정리
- "데이터 정의 언어"
- CREATE TABLE
  - 데이터 타입과 제약 조건
- ALTER TABLE
  - RENAME
  - RENAME COLUMN
  - ADD COLUMN
  - DROP COLUMN
- DROP TABLE

---

# DML
- DML을 통해 데이터 조작하기 (CRUD)
- INSERT (C), **SELECT** (R), UPDATE (U), DELETE (D)

# Simple query
- SELECT문 사용하여 간단하게 단일 테이블에서 데이터 조회
```sql
SELECT column1, column2 FROM table_name;
```
- "Query data from a table"
- 특정 테이블에서 데이터를 조회하기 위해 사용
- 문법 규칙
  - SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
  - FROM 절(clause)에서 데이터를 가져올 테이블을 지정

## SELECT statement 실습
### 이름과 나이 조회하기
```sql
SELECT first_name, age
FROM users;
```

### 전체 데이터 조회하기
```sql
SELECT * FROM users;
```

### rowid 컬럼 조회
```sql
SELECT rowid, first_name FROM users;
```

# Sorting rows
- ORDER BY 



