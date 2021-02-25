BEGIN TRANSACTION;
CREATE TABLE users(id INTERGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'bkwag','bkwag@naver.com','010-1111-2345','bkwag.git','2021-02-25 13:27:12');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-1111-1111','Park.com','2021-02-25 13:27:24');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-02-25 13:30:46');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2021-02-25 13:30:46');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2021-02-25 13:30:46');
COMMIT;
