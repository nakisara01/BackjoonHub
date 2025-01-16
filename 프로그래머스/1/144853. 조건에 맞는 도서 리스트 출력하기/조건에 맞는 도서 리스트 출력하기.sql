-- 코드를 입력하세요
SELECT BOOK_ID, SUBSTRING(PUBLISHED_DATE,1,10) as PUBLISHED_DATE
FROM BOOK
WHERE category in ('인문') and published_date like ('2021%')