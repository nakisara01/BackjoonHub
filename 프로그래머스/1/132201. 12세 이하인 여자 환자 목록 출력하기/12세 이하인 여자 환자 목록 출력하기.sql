-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, COALESCE(TLNO, 'NONE') as TLNO
from patient
where AGE <= 12 AND GEND_CD in ('W')
order by age desc, pt_name asc