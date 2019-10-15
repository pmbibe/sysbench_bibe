if sysbench.cmdline.command == nil then
   error("Command is required. Supported commands: run")
end
sysbench.cmdline.options = {
	point_selects = {"Number of point SELECT queries to run", 10},
	skip_trx = {"Do not use BEGIN/COMMIT; Use global auto_commit value", false}
}
local select_counts = {
	"SELECT employees1.first_name,employees1.last_name, departments.dept_name FROM employees1 LEFT JOIN titles ON titles.emp_no=employees1.emp_no LEFT JOIN dept_emp ON dept_emp.emp_no=employees1.emp_no LEFT JOIN departments ON dept_emp.dept_no = departments.dept_no WHERE titles.title = 'Manager' GROUP BY departments.dept_name",
	"SELECT DISTINCT first_name,last_name,title FROM employees1 LEFT JOIN titles ON employees1.emp_no = titles.emp_no JOIN dept_manager WHERE DATEDIFF(CURRENT_DATE,employees1.hire_date) > 9000 ORDER BY datediff(titles.to_date, titles.from_date) DESC",
	"SELECT COUNT(employees1.emp_no),departments.dept_name from employees1 LEFT JOIN dept_emp ON employees1.emp_no=dept_emp.emp_no LEFT JOIN departments ON dept_emp.dept_no=departments.dept_no GROUP BY departments.dept_name",
	"SELECT employees1.first_name,employees1.last_name, departments.dept_name FROM employees1 LEFT JOIN titles ON titles.emp_no=employees1.emp_no LEFT JOIN dept_emp ON dept_emp.emp_no=employees1.emp_no LEFT JOIN departments ON dept_emp.dept_no = departments.dept_no WHERE titles.title = 'Manager' GROUP BY departments.dept_name",
	"SELECT employees1.first_name, employees1.last_name,DATE_FORMAT (employees1.birth_date,'%D-%M') AS BIRTHDAY FROM employees1 WHERE  DATE_FORMAT (CURRENT_DATE,'%M') = DATE_FORMAT(employees1.birth_date,'%M')"
}
function execute_selects()
	for i, o in ipairs(select_counts) do
		con:query(o)
	end
end
function thread_init()
	drv = sysbench.sql.driver()
	con = drv:connect()
end
function thread_done()
	con:disconnect()
end
function event()
	if not sysbench.opt.skip_trx then
		con:query("BEGIN")
	end
	for i = 1, sysbench.opt.point_selects do
	execute_selects()
	end
	if not sysbench.opt.skip_trx then
		con:query("COMMIT")
	end
end
