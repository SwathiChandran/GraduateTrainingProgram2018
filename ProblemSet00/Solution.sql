-- ProblemSet00<No.>, November <25> <2018>--
Submission by <s.aa.ravichandran> 
1)Select the Employee with the top three salaries
SELECT NAME FROM EMPLOYEE WHERE SALARY >=(SELECT MAX(SALARY) FROM EMPLOYEE WHERE SALARY <(SELECT MAX(SALARY) FROM EMPLOYEE WHERE SALARY <(SELECT MAX(SALARY) FROM EMPLOYEE)))ORDER BY SALARY;
ADAM WAYNE
PAUL VINCENT
TARA CUMMINGS
Record count=3
2)Select the Employee with the least salary
SELECT MIN(SALARY) FROM EMPLOYEE;
15380
3)Select the Employee who does not have a manager in the department table
4)Select the Employee who is also a Manager
SELECT DISTINCT NAME  FROM EMPLOYEE E INNER JOIN EMPLOYEE D ON E.E_ID=D.MANGER_ID;
