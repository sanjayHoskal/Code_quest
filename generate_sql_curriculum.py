# generate_sql_curriculum.py
# Generates authentic SQL questions across all 6 game modes, 3 difficulties, and 4 levels
from curriculum_builder import create_order_q, create_fill_q, create_debug_q, create_predict_q, create_mcq_q
import copy

def generate_sql():
    sql = {
        "Drag & Drop": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Syntax Validator": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Code Arrangement": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "MCQ Challenge": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Debug the Code": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Predict the Output": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Fill in the Blanks": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
    }

    # =========================================================================
    # 1. DRAG & DROP & CODE ARRANGEMENT (order)
    # =========================================================================
    # Beginner L1: Basic SELECT, FROM, WHERE
    b_l1 = [
        create_order_q("Arrange clauses to select all columns for active users.",
                       ["SELECT *", "FROM users", "WHERE is_active = 1;"],
                       "Start with SELECT clause.", "Specify table name in FROM clause.",
                       "Standard SQL queries start with SELECT, followed by FROM and optional WHERE conditions."),
        create_order_q("Arrange clauses to retrieve employee names with salary above 50,000.",
                       ["SELECT first_name, last_name", "FROM employees", "WHERE salary > 50000;"],
                       "List columns in SELECT.", "Specify FROM employees.",
                       "SELECT lists desired fields, FROM specifies the source relation, and WHERE filters rows."),
        create_order_q("Arrange clauses to query distinct product categories.",
                       ["SELECT DISTINCT category", "FROM products", "WHERE in_stock = 1;"],
                       "DISTINCT comes right after SELECT.", "Filter available items in WHERE.",
                       "SELECT DISTINCT eliminates duplicate values from the output column."),
        create_order_q("Arrange clauses to find students enrolled in 'Computer Science'.",
                       ["SELECT student_id, student_name", "FROM students", "WHERE major = 'Computer Science';"],
                       "SELECT projections first.", "Identify the students table.",
                       "String literals in SQL WHERE clauses are wrapped in single quotes."),
        create_order_q("Arrange clauses to select order IDs placed after January 1st, 2024.",
                       ["SELECT order_id, order_date", "FROM orders", "WHERE order_date >= '2024-01-01';"],
                       "SELECT order columns.", "FROM orders table.",
                       "Dates in SQL are filtered using standard comparison operators (>=).")
    ]

    # Beginner L2: AND/OR, ORDER BY, LIMIT
    b_l2 = [
        create_order_q("Arrange clauses to get top 5 highest-priced products.",
                       ["SELECT product_name, price", "FROM products", "ORDER BY price DESC", "LIMIT 5;"],
                       "Sort by price descending.", "LIMIT goes at the end of the query.",
                       "ORDER BY sorts rows, DESC specifies descending order, and LIMIT restricts row count."),
        create_order_q("Arrange clauses to find customers in California or New York.",
                       ["SELECT customer_name, state", "FROM customers", "WHERE state = 'CA' OR state = 'NY'", "ORDER BY customer_name ASC;"],
                       "Filter with OR.", "ORDER BY comes after WHERE.",
                       "Logical OR matches either condition; ORDER BY ASC sorts alphabetically."),
        create_order_q("Arrange clauses to get 10 recent completed orders.",
                       ["SELECT id, total_amount", "FROM orders", "WHERE status = 'completed'", "ORDER BY created_at DESC", "LIMIT 10;"],
                       "Filter status first.", "Order by timestamp descending.",
                       "WHERE filters for completed orders before sorting and limiting to 10."),
        create_order_q("Arrange clauses to find high-rated books sorted by title.",
                       ["SELECT title, rating", "FROM books", "WHERE rating >= 4.5", "ORDER BY title ASC;"],
                       "WHERE filters rating.", "Sort alphabetically by title.",
                       "Filters numeric rating >= 4.5 and sorts ascending by title."),
        create_order_q("Arrange clauses to select lowest 3 inventory items.",
                       ["SELECT item_name, quantity", "FROM inventory", "WHERE quantity > 0", "ORDER BY quantity ASC", "LIMIT 3;"],
                       "Filter out out-of-stock items.", "Sort ascending to find lowest.",
                       "ORDER BY ASC sorts from lowest to highest, LIMIT 3 returns the top 3.")
    ]

    # Beginner L3: INSERT INTO, UPDATE, DELETE
    b_l3 = [
        create_order_q("Arrange the statement to insert a new user record.",
                       ["INSERT INTO users (username, email)", "VALUES ('alice', 'alice@code.org');"],
                       "INSERT INTO specifies table and columns.", "VALUES supplies the corresponding data.",
                       "INSERT INTO table (columns...) VALUES (values...) is the standard insertion syntax."),
        create_order_q("Arrange the statement to update an employee's salary.",
                       ["UPDATE employees", "SET salary = 75000", "WHERE employee_id = 101;"],
                       "UPDATE specifies the table.", "SET designates the column assignment.",
                       "UPDATE updates records; WHERE ensures only employee 101 is modified."),
        create_order_q("Arrange the statement to delete expired sessions.",
                       ["DELETE FROM sessions", "WHERE expires_at < CURRENT_TIMESTAMP;"],
                       "DELETE FROM specifies table.", "WHERE filters which rows to delete.",
                       "DELETE FROM removes matching records satisfying the WHERE filter."),
        create_order_q("Arrange the statement to insert a new product with stock count.",
                       ["INSERT INTO products (name, price, stock)", "VALUES ('Mechanical Keyboard', 89.99, 50);"],
                       "Specify column names in parentheses.", "Align values with column order.",
                       "Column names and values must align positionally in the INSERT statement."),
        create_order_q("Arrange the statement to deactivate accounts that have not logged in.",
                       ["UPDATE accounts", "SET status = 'inactive'", "WHERE last_login < '2023-01-01';"],
                       "UPDATE table name.", "SET column value.",
                       "SET assigns the new status, and WHERE selects stale records.")
    ]

    # Beginner L4 (Master): Aggregate functions and basic GROUP BY
    b_l4 = [
        create_order_q("Arrange query to compute total sales per region.",
                       ["SELECT region, SUM(amount) AS total_sales", "FROM sales", "GROUP BY region", "ORDER BY total_sales DESC;"],
                       "SELECT region and aggregate SUM.", "GROUP BY the non-aggregated column.",
                       "GROUP BY groups rows sharing the region, allowing SUM to calculate regional totals."),
        create_order_q("Arrange query to count employees in each department.",
                       ["SELECT department_id, COUNT(*) AS emp_count", "FROM employees", "GROUP BY department_id", "ORDER BY emp_count DESC;"],
                       "SELECT department and COUNT(*).", "GROUP BY department_id.",
                       "COUNT(*) tallies the number of rows within each department grouping."),
        create_order_q("Arrange query to find average rating for each genre.",
                       ["SELECT genre, ROUND(AVG(rating), 2) AS avg_score", "FROM movies", "GROUP BY genre", "ORDER BY avg_score DESC;"],
                       "Aggregate with AVG().", "Group by genre.",
                       "AVG() calculates the mean rating for each genre category."),
        create_order_q("Arrange query to find minimum and maximum product price per brand.",
                       ["SELECT brand, MIN(price) AS min_price, MAX(price) AS max_price", "FROM products", "GROUP BY brand;"],
                       "SELECT brand and MIN/MAX aggregates.", "GROUP BY brand.",
                       "MIN() and MAX() find the lowest and highest values in each group."),
        create_order_q("Arrange query to calculate total orders per customer.",
                       ["SELECT customer_id, COUNT(order_id) AS total_orders", "FROM orders", "WHERE status = 'delivered'", "GROUP BY customer_id;"],
                       "Filter with WHERE before grouping.", "GROUP BY customer_id.",
                       "WHERE filters rows prior to aggregation, and GROUP BY groups the remaining rows.")
    ]

    # Intermediate L1: GROUP BY with HAVING
    i_l1 = [
        create_order_q("Arrange query to find departments with more than 5 employees.",
                       ["SELECT department_id, COUNT(*) AS total_staff", "FROM employees", "GROUP BY department_id", "HAVING COUNT(*) > 5;"],
                       "GROUP BY department_id first.", "HAVING filters aggregate counts.",
                       "HAVING filters groups post-aggregation, whereas WHERE filters individual rows."),
        create_order_q("Arrange query to find categories with average price exceeding $100.",
                       ["SELECT category, AVG(price) AS avg_price", "FROM products", "GROUP BY category", "HAVING AVG(price) > 100", "ORDER BY avg_price DESC;"],
                       "Group by category.", "Filter groups with HAVING.",
                       "HAVING AVG(price) > 100 filters out categories whose average price is $100 or less."),
        create_order_q("Arrange query to find customers who placed at least 3 orders.",
                       ["SELECT customer_id, COUNT(id) AS order_count", "FROM orders", "GROUP BY customer_id", "HAVING COUNT(id) >= 3;"],
                       "GROUP BY customer_id.", "HAVING checks the count threshold.",
                       "HAVING COUNT(id) >= 3 restricts the output to repeat customers."),
        create_order_q("Arrange query to find stores generating over $50,000 in total revenue.",
                       ["SELECT store_id, SUM(revenue) AS total_rev", "FROM daily_sales", "GROUP BY store_id", "HAVING SUM(revenue) > 50000;"],
                       "Group daily sales by store.", "Filter aggregate total with HAVING.",
                       "SUM(revenue) aggregates daily records and HAVING checks the threshold."),
        create_order_q("Arrange query to find authors who published at least 2 books in 2024.",
                       ["SELECT author_id, COUNT(*) AS book_count", "FROM books", "WHERE publish_year = 2024", "GROUP BY author_id", "HAVING COUNT(*) >= 2;"],
                       "WHERE filters the year first.", "HAVING filters the aggregated book count.",
                       "Row filtering in WHERE occurs before aggregation; group filtering occurs in HAVING.")
    ]

    # Intermediate L2: INNER JOIN and LEFT JOIN
    i_l2 = [
        create_order_q("Arrange query to join employees with their department names.",
                       ["SELECT e.first_name, d.department_name", "FROM employees e", "INNER JOIN departments d", "ON e.department_id = d.id;"],
                       "Specify aliases e and d.", "Join on the foreign key relationship.",
                       "INNER JOIN matches rows where e.department_id equals d.id."),
        create_order_q("Arrange query to retrieve all customers and any matching orders.",
                       ["SELECT c.name, o.order_id, o.amount", "FROM customers c", "LEFT JOIN orders o", "ON c.id = o.customer_id;"],
                       "Start with FROM customers c.", "LEFT JOIN orders o ON c.id = o.customer_id.",
                       "LEFT JOIN preserves all customer records even if they have no corresponding orders."),
        create_order_q("Arrange query to join orders, order items, and products.",
                       ["SELECT o.id, p.product_name, oi.quantity", "FROM orders o", "JOIN order_items oi ON o.id = oi.order_id", "JOIN products p ON oi.product_id = p.id;"],
                       "Join order_items first.", "Then join products.",
                       "Chained joins connect relational entities through intermediate bridge tables."),
        create_order_q("Arrange query to list courses along with enrolled student count.",
                       ["SELECT c.course_name, COUNT(e.student_id) AS student_count", "FROM courses c", "LEFT JOIN enrollments e ON c.id = e.course_id", "GROUP BY c.id, c.course_name;"],
                       "LEFT JOIN enrollments.", "GROUP BY course identifier.",
                       "LEFT JOIN ensures courses with 0 enrollments still appear with count 0."),
        create_order_q("Arrange query to join students and advisors.",
                       ["SELECT s.name AS student, a.name AS advisor", "FROM students s", "INNER JOIN advisors a", "ON s.advisor_id = a.id;"],
                       "Aliased column projections.", "ON matches advisor_id to advisor id.",
                       "INNER JOIN pairs each student with their designated academic advisor.")
    ]

    # Intermediate L3: Subqueries, IN, BETWEEN, LIKE
    i_l3 = [
        create_order_q("Arrange query to find employees earning more than the company average.",
                       ["SELECT first_name, salary", "FROM employees", "WHERE salary > (", "    SELECT AVG(salary) FROM employees", ");"],
                       "Outer query filters salary.", "Subquery computes AVG(salary).",
                       "A scalar subquery calculates the overall average salary to compare against."),
        create_order_q("Arrange query to find users who placed an order in the last 30 days.",
                       ["SELECT id, username", "FROM users", "WHERE id IN (", "    SELECT DISTINCT user_id FROM orders WHERE order_date >= '2024-05-01'", ");"],
                       "Outer query selects users.", "IN operator tests membership against subquery.",
                       "IN checks if user id matches any ID returned by the inner query."),
        create_order_q("Arrange query to find products priced between $20 and $50.",
                       ["SELECT product_name, price", "FROM products", "WHERE price BETWEEN 20 AND 50", "ORDER BY price ASC;"],
                       "BETWEEN operator handles range.", "ORDER BY price ascending.",
                       "BETWEEN 20 AND 50 is inclusive of both boundary values."),
        create_order_q("Arrange query to find customers whose email ends with '@gmail.com'.",
                       ["SELECT customer_id, email", "FROM customers", "WHERE email LIKE '%@gmail.com'", "ORDER BY customer_id;"],
                       "LIKE operator with % wildcard.", "% matches any leading characters.",
                       "LIKE '%@gmail.com' matches any string ending in '@gmail.com'."),
        create_order_q("Arrange query to find products with no sales using NOT EXISTS.",
                       ["SELECT p.id, p.product_name", "FROM products p", "WHERE NOT EXISTS (", "    SELECT 1 FROM order_items oi WHERE oi.product_id = p.id", ");"],
                       "Outer query checks products.", "NOT EXISTS tests subquery non-existence.",
                       "Correlated subquery with NOT EXISTS returns products lacking sales records.")
    ]

    # Intermediate L4 (Master): Multi-table JOINs, CASE WHEN, UNION
    i_l4 = [
        create_order_q("Arrange query using CASE WHEN to classify order size.",
                       ["SELECT order_id, total_amount,", "CASE WHEN total_amount >= 500 THEN 'Large'", "     WHEN total_amount >= 100 THEN 'Medium'", "     ELSE 'Small' END AS order_size", "FROM orders;"],
                       "CASE expression evaluates conditions in order.", "ELSE provides fallback.",
                       "CASE WHEN acts as an inline conditional expression in SQL."),
        create_order_q("Arrange query to combine customer and supplier contact emails.",
                       ["SELECT email, 'Customer' AS role FROM customers", "UNION ALL", "SELECT email, 'Supplier' AS role FROM suppliers", "ORDER BY email;"],
                       "First SELECT branch.", "UNION ALL merges sets.",
                       "UNION ALL combines results from multiple queries without deduplication overhead."),
        create_order_q("Arrange query joining users, roles, and permissions.",
                       ["SELECT u.username, r.role_name, p.permission_name", "FROM users u", "JOIN user_roles ur ON u.id = ur.user_id", "JOIN roles r ON ur.role_id = r.id", "JOIN role_permissions rp ON r.id = rp.role_id", "JOIN permissions p ON rp.permission_id = p.id;"],
                       "Bridge through user_roles to roles.", "Bridge through role_permissions to permissions.",
                       "Multi-table joins link normalized schema tables through junction tables."),
        create_order_q("Arrange query calculating conditional employee bonuses.",
                       ["SELECT emp_id, salary,", "CASE WHEN performance_score >= 90 THEN salary * 0.20", "     WHEN performance_score >= 75 THEN salary * 0.10", "     ELSE 0 END AS bonus", "FROM employee_reviews;"],
                       "CASE checks performance thresholds.", "Multiplies salary by bonus rate.",
                       "CASE WHEN computes dynamic bonus amounts based on review scores."),
        create_order_q("Arrange query combining active and archived projects with UNION.",
                       ["SELECT project_id, title, 'Active' AS status FROM projects", "UNION", "SELECT project_id, title, 'Archived' AS status FROM archived_projects", "ORDER BY project_id;"],
                       "Query active projects.", "UNION deduplicates rows across both sets.",
                       "UNION combines distinct records from active and archive tables.")
    ]

    # Advanced L1: Window functions (ROW_NUMBER, RANK, DENSE_RANK, OVER)
    a_l1 = [
        create_order_q("Arrange query to assign sequential row numbers ordered by hire date.",
                       ["SELECT employee_id, first_name, hire_date,", "ROW_NUMBER() OVER (ORDER BY hire_date ASC) AS seq_num", "FROM employees;"],
                       "ROW_NUMBER() takes an OVER clause.", "ORDER BY inside OVER sorts the partition.",
                       "ROW_NUMBER() generates a unique sequential integer for each row."),
        create_order_q("Arrange query to rank employees by salary within each department.",
                       ["SELECT department_id, first_name, salary,", "DENSE_RANK() OVER (", "    PARTITION BY department_id", "    ORDER BY salary DESC", ") AS salary_rank", "FROM employees;"],
                       "PARTITION BY splits calculation by department.", "ORDER BY sorts salaries descending.",
                       "DENSE_RANK() ranks values without skipping rank numbers on ties."),
        create_order_q("Arrange query to calculate running total of sales over time.",
                       ["SELECT order_date, amount,", "SUM(amount) OVER (", "    ORDER BY order_date ASC", "    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW", ") AS running_total", "FROM orders;"],
                       "SUM() used as window function with OVER.", "ROWS frame specifies running accumulation.",
                       "A windowed SUM computes cumulative totals across sequential dates."),
        create_order_q("Arrange query to find previous day's sales using LAG().",
                       ["SELECT sale_date, daily_revenue,", "LAG(daily_revenue, 1) OVER (ORDER BY sale_date ASC) AS prev_day_revenue", "FROM store_sales;"],
                       "LAG() accesses data from a previous row.", "OVER specifies the chronological order.",
                       "LAG(col, offset) retrieves values from prior rows in the window."),
        create_order_q("Arrange query to compute department salary percentage of total.",
                       ["SELECT employee_id, department_id, salary,", "ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY department_id), 2) AS dept_pct", "FROM employees;"],
                       "Calculate ratio against windowed sum.", "PARTITION BY department_id.",
                       "SUM(salary) OVER (PARTITION BY dept) computes departmental total for each row.")
    ]

    # Advanced L2: CTEs (WITH clause)
    a_l2 = [
        create_order_q("Arrange query using a CTE to find departments with above-average budgets.",
                       ["WITH DeptBudgets AS (", "    SELECT department_id, SUM(salary) AS total_budget FROM employees GROUP BY department_id", ")", "SELECT d.department_name, b.total_budget", "FROM DeptBudgets b", "JOIN departments d ON b.department_id = d.id", "WHERE b.total_budget > 250000;"],
                       "WITH defines the Common Table Expression.", "Outer query joins CTE with departments.",
                       "CTEs provide modular temporary result sets that improve readability over nested subqueries."),
        create_order_q("Arrange query using a CTE to rank products and select the top product per category.",
                       ["WITH RankedProducts AS (", "    SELECT id, category, price, ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS rn FROM products", ")", "SELECT id, category, price", "FROM RankedProducts", "WHERE rn = 1;"],
                       "CTE computes row numbers partitioned by category.", "Outer query filters WHERE rn = 1.",
                       "Qualifying row_number = 1 in an outer query retrieves the top record per group."),
        create_order_q("Arrange query using multiple CTEs to compute monthly order comparisons.",
                       ["WITH MonthlySales AS (", "    SELECT strftime('%Y-%m', order_date) AS month, SUM(amount) AS total FROM orders GROUP BY 1", "),", "SalesDiff AS (", "    SELECT month, total, LAG(total) OVER (ORDER BY month) AS prev_total FROM MonthlySales", ")", "SELECT month, total, (total - prev_total) AS growth FROM SalesDiff;"],
                       "Define MonthlySales CTE first.", "Second CTE references MonthlySales.",
                       "Chained CTEs separated by commas allow multi-stage analytical transformations."),
        create_order_q("Arrange recursive CTE to generate numbers from 1 to 5.",
                       ["WITH RECURSIVE NumberSeq(n) AS (", "    SELECT 1", "    UNION ALL", "    SELECT n + 1 FROM NumberSeq WHERE n < 5", ")", "SELECT n FROM NumberSeq;"],
                       "WITH RECURSIVE declaration with anchor member.", "UNION ALL with recursive member.",
                       "Recursive CTEs consist of an anchor member and a recursive member terminating on a condition."),
        create_order_q("Arrange recursive CTE to traverse employee-manager hierarchy.",
                       ["WITH RECURSIVE OrgChart AS (", "    SELECT emp_id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL", "    UNION ALL", "    SELECT e.emp_id, e.name, e.manager_id, o.level + 1 FROM employees e JOIN OrgChart o ON e.manager_id = o.emp_id", ")", "SELECT * FROM OrgChart ORDER BY level, name;"],
                       "Anchor selects CEO (manager_id IS NULL).", "Recursive member joins employees to OrgChart.",
                       "Recursive hierarchy traversal increments depth level at each step.")
    ]

    # Advanced L3: Transactions, Indexes, Constraints
    a_l3 = [
        create_order_q("Arrange statement to create a composite unique index.",
                       ["CREATE UNIQUE INDEX idx_user_org", "ON user_memberships (user_id, organization_id);"],
                       "CREATE UNIQUE INDEX specifies index name.", "ON defines table and columns.",
                       "Composite unique indexes enforce uniqueness across multiple combined columns."),
        create_order_q("Arrange statements to transfer funds within a transaction.",
                       ["BEGIN TRANSACTION;", "UPDATE accounts SET balance = balance - 100 WHERE id = 1;", "UPDATE accounts SET balance = balance + 100 WHERE id = 2;", "COMMIT;"],
                       "BEGIN starts transaction.", "Perform updates atomically.",
                       "Transactions ensure atomicity: either both updates succeed or neither takes effect."),
        create_order_q("Arrange statements to rollback a transaction on error condition.",
                       ["BEGIN TRANSACTION;", "INSERT INTO audit_logs (action) VALUES ('purge');", "DELETE FROM old_records WHERE created_at < '2020-01-01';", "ROLLBACK;"],
                       "BEGIN starts transaction block.", "ROLLBACK reverts all changes made in block.",
                       "ROLLBACK discards changes made within an uncommitted transaction."),
        create_order_q("Arrange statement to create a table with foreign key constraint.",
                       ["CREATE TABLE orders (", "    order_id INT PRIMARY KEY,", "    customer_id INT NOT NULL,", "    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE", ");"],
                       "Define primary key column.", "FOREIGN KEY links to parent table.",
                       "ON DELETE CASCADE automatically removes child records when parent is deleted."),
        create_order_q("Arrange statement to alter table adding a CHECK constraint.",
                       ["ALTER TABLE products", "ADD CONSTRAINT chk_positive_price", "CHECK (price > 0 AND stock >= 0);"],
                       "ALTER TABLE products.", "ADD CONSTRAINT with CHECK expression.",
                       "CHECK constraints validate business rules before inserting or modifying rows.")
    ]

    # Advanced L4 (Master): Complex Analytical Queries, Optimization
    a_l4 = [
        create_order_q("Arrange query to calculate Customer Lifetime Value (CLV) cohorts.",
                       ["WITH CustomerSummary AS (", "    SELECT customer_id, MIN(order_date) AS first_order, SUM(total_amount) AS total_spent FROM orders GROUP BY customer_id", ")", "SELECT strftime('%Y', first_order) AS cohort_year, COUNT(*) AS customer_count, ROUND(AVG(total_spent), 2) AS avg_clv", "FROM CustomerSummary", "GROUP BY cohort_year", "ORDER BY cohort_year ASC;"],
                       "CTE computes first order and total spent.", "Outer query groups by cohort year.",
                       "Cohort analysis groups users by acquisition timestamp to observe lifetime metrics."),
        create_order_q("Arrange query using COALESCE to handle NULL values in contact info.",
                       ["SELECT id, name,", "COALESCE(work_email, personal_email, 'no-email@domain.com') AS primary_email", "FROM contacts", "ORDER BY name ASC;"],
                       "COALESCE checks expressions in order.", "Fallback string used if all prior are NULL.",
                       "COALESCE returns the first non-null argument among its parameters."),
        create_order_q("Arrange query to find gaps in sequential invoice numbers.",
                       ["SELECT invoice_id + 1 AS missing_start", "FROM invoices curr", "WHERE NOT EXISTS (", "    SELECT 1 FROM invoices next_inv WHERE next_inv.invoice_id = curr.invoice_id + 1", ") AND invoice_id < (SELECT MAX(invoice_id) FROM invoices);"],
                       "Detect gaps where id + 1 does not exist.", "Bound search by MAX(invoice_id).",
                       "Gap detection checks for non-existent consecutive primary key values."),
        create_order_q("Arrange query calculating moving 7-day average revenue.",
                       ["SELECT sale_date, daily_revenue,", "ROUND(AVG(daily_revenue) OVER (", "    ORDER BY sale_date", "    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW", "), 2) AS moving_avg_7d", "FROM daily_financials;"],
                       "Window AVG across 6 preceding rows and current row.", "Total window width is 7 days.",
                       "Moving averages smooth short-term fluctuations in time series data."),
        create_order_q("Arrange query using NTILE(4) to segment users into quartile spenders.",
                       ["SELECT user_id, total_spent,", "NTILE(4) OVER (ORDER BY total_spent DESC) AS spend_quartile", "FROM user_metrics;"],
                       "NTILE(4) divides partition into 4 equal buckets.", "Sorted by total_spent descending.",
                       "NTILE(4) segments ordered data into quartiles 1, 2, 3, and 4.")
    ]

    sql["Drag & Drop"]["Beginner"]["1"] = b_l1
    sql["Drag & Drop"]["Beginner"]["2"] = b_l2
    sql["Drag & Drop"]["Beginner"]["3"] = b_l3
    sql["Drag & Drop"]["Beginner"]["4"] = b_l4
    sql["Drag & Drop"]["Intermediate"]["1"] = i_l1
    sql["Drag & Drop"]["Intermediate"]["2"] = i_l2
    sql["Drag & Drop"]["Intermediate"]["3"] = i_l3
    sql["Drag & Drop"]["Intermediate"]["4"] = i_l4
    sql["Drag & Drop"]["Advanced"]["1"] = a_l1
    sql["Drag & Drop"]["Advanced"]["2"] = a_l2
    sql["Drag & Drop"]["Advanced"]["3"] = a_l3
    sql["Drag & Drop"]["Advanced"]["4"] = a_l4

    import curriculum_validator
    sql_val = curriculum_validator.get_sql_validator()
    sql["Syntax Validator"] = sql_val
    sql["Code Arrangement"] = sql_val

    # =========================================================================
    # 2. MCQ CHALLENGE (mcq)
    # =========================================================================
    # Beginner
    sql["MCQ Challenge"]["Beginner"]["1"] = [
        create_mcq_q("Which SQL keyword is used to retrieve data from a database?",
                     "SELECT column1 FROM table_name;",
                     ["A) GET", "B) SELECT", "C) EXTRACT", "D) FETCH"], "B",
                     "It is the first keyword in almost every read query.", "6 letters starting with S.",
                     "SELECT is the primary SQL DML statement for querying data."),
        create_mcq_q("Which clause is used to filter rows in a SQL query?",
                     "SELECT * FROM users _______ age >= 18;",
                     ["A) HAVING", "B) ORDER BY", "C) WHERE", "D) FILTER"], "C",
                     "Keyword specifying row-level conditions.", "5 letters starting with W.",
                     "WHERE specifies condition criteria for individual rows."),
        create_mcq_q("What does 'SELECT DISTINCT' accomplish?",
                     "SELECT DISTINCT country FROM customers;",
                     ["A) Selects only non-null values", "B) Removes duplicate rows from the output", "C) Sorts the result alphabetically", "D) Selects the first row"], "B",
                     "Think about unique values.", "Eliminates redundancy.",
                     "DISTINCT returns only unique values, stripping away duplicates."),
        create_mcq_q("Which operator tests for equality in SQL?",
                     "SELECT * FROM items WHERE price _______ 20;",
                     ["A) ==", "B) :=", "C) =", "D) EQUALS"], "C",
                     "SQL uses single character for equality.", "Standard equal sign.",
                     "In SQL, single '=' is the comparison operator for equality."),
        create_mcq_q("How do you select all columns from the 'employees' table?",
                     "SELECT _______ FROM employees;",
                     ["A) ALL", "B) %", "C) *", "D) #"], "C",
                     "Wildcard character representing all columns.", "Asterisk.",
                     "* is the wildcard meaning 'all columns'.")
    ]

    sql["MCQ Challenge"]["Beginner"]["2"] = [
        create_mcq_q("Which keyword is used to sort the result-set in SQL?",
                     "SELECT name FROM products _______ name ASC;",
                     ["A) SORT BY", "B) ORDER BY", "C) GROUP BY", "D) ARRANGE BY"], "B",
                     "Two-word clause starting with O.", "Specifies sorting column.",
                     "ORDER BY sorts rows based on one or more columns."),
        create_mcq_q("Which keyword sorts results from highest to lowest?",
                     "SELECT name, salary FROM employees ORDER BY salary _______;",
                     ["A) ASC", "B) HIGH", "C) DESC", "D) DOWN"], "C",
                     "Short for descending.", "4 letters starting with D.",
                     "DESC sorts in descending order (highest to lowest)."),
        create_mcq_q("Which clause limits the number of rows returned in SQLite / MySQL / PostgreSQL?",
                     "SELECT * FROM products ORDER BY price DESC _______ 5;",
                     ["A) TOP", "B) LIMIT", "C) MAX", "D) TAKE"], "B",
                     "5 letters starting with L.", "Standard pagination keyword.",
                     "LIMIT restricts the number of tuples in the result set."),
        create_mcq_q("Which logical operator returns true only if BOTH conditions are met?",
                     "SELECT * FROM users WHERE active = 1 _______ age >= 21;",
                     ["A) OR", "B) AND", "C) BOTH", "D) PLUS"], "B",
                     "Conjunction operator.", "3 letters.",
                     "AND requires both boolean expressions to evaluate to true."),
        create_mcq_q("How do you check if a value is not equal to 100 in standard SQL?",
                     "SELECT * FROM scores WHERE points _______ 100;",
                     ["A) <> or !=", "B) NOT 100", "C) !== 100", "D) IS NOT 100"], "A",
                     "Both <> and != are widely supported.", "Angle brackets or exclamation equal.",
                     "<> is standard SQL inequality; != is universally supported.")
    ]

    sql["MCQ Challenge"]["Beginner"]["3"] = [
        create_mcq_q("Which SQL statement is used to insert new records into a table?",
                     "_______ table_name (col1) VALUES ('val');",
                     ["A) INSERT INTO", "B) ADD RECORD", "C) UPDATE", "D) PUSH INTO"], "A",
                     "Two words starting with I.", "INSERT ...",
                     "INSERT INTO adds new rows to a table."),
        create_mcq_q("Which statement modifies existing records in a table?",
                     "_______ users SET active = 0 WHERE id = 5;",
                     ["A) MODIFY", "B) CHANGE", "C) UPDATE", "D) ALTER"], "C",
                     "6 letters starting with U.", "UPDATE statement.",
                     "UPDATE changes data in existing records."),
        create_mcq_q("How do you check for a NULL value in a WHERE clause?",
                     "SELECT * FROM users WHERE email _______;",
                     ["A) = NULL", "B) IS NULL", "C) == NULL", "D) EQUALS NULL"], "B",
                     "NULL represents missing data and cannot equal anything.", "Use the IS operator.",
                     "IS NULL tests for the presence of NULL; = NULL evaluates to unknown/falsy."),
        create_mcq_q("What happens if you run 'DELETE FROM employees;' without a WHERE clause?",
                     "DELETE FROM employees;",
                     ["A) Deletes only the first row", "B) Generates a syntax error", "C) Deletes all rows in the table", "D) Deletes the table definition"], "C",
                     "Think about missing filters.", "Affects every row.",
                     "Without a WHERE clause, DELETE removes all records from the table."),
        create_mcq_q("Which keyword specifies values to be inserted?",
                     "INSERT INTO logs (msg) _______ ('User login');",
                     ["A) DATA", "B) VALUES", "C) ITEMS", "D) SET"], "B",
                     "Plural noun indicating inserted entities.", "Starts with V.",
                     "VALUES defines the list of tuple values in an INSERT statement.")
    ]

    sql["MCQ Challenge"]["Beginner"]["4"] = [
        create_mcq_q("Which aggregate function calculates the total sum of a numeric column?",
                     "SELECT _______(salary) FROM employees;",
                     ["A) TOTAL()", "B) SUM()", "C) ADD()", "D) COUNT()"], "B",
                     "3 letters starting with S.", "SUM of numbers.",
                     "SUM() returns the arithmetic total of an expression."),
        create_mcq_q("Which function returns the number of rows matching a criteria?",
                     "SELECT _______(*) FROM orders;",
                     ["A) COUNT()", "B) SUM()", "C) LENGTH()", "D) NUM()"], "A",
                     "5 letters starting with C.", "Tallies items.",
                     "COUNT(*) counts all rows in the table or group."),
        create_mcq_q("What does AVG(price) return if all price values are NULL?",
                     "SELECT AVG(price) FROM empty_products;",
                     ["A) 0", "B) NULL", "C) Error", "D) -1"], "B",
                     "Aggregate functions ignore NULLs.", "If no non-null rows exist, result is NULL.",
                     "Aggregate functions (except COUNT) evaluate to NULL on empty/null sets."),
        create_mcq_q("Which keyword gives a column or table a temporary alias in query output?",
                     "SELECT first_name _______ given_name FROM users;",
                     ["A) TO", "B) AS", "C) LIKE", "D) ALIAS"], "B",
                     "Two-letter keyword.", "AS keyword.",
                     "AS renames columns or tables temporarily for query projection."),
        create_mcq_q("Which function finds the highest value in a column?",
                     "SELECT _______(score) FROM students;",
                     ["A) TOP()", "B) PEAK()", "C) MAX()", "D) HIGH()"], "C",
                     "3 letters starting with M.", "Maximum.",
                     "MAX() returns the greatest value in the set.")
    ]

    # Intermediate
    sql["MCQ Challenge"]["Intermediate"]["1"] = [
        create_mcq_q("What is the primary difference between WHERE and HAVING?",
                     None,
                     ["A) WHERE filters groups; HAVING filters individual rows",
                      "B) WHERE filters rows before aggregation; HAVING filters groups after aggregation",
                      "C) They are completely interchangeable",
                      "D) HAVING can only be used with SELECT *"], "B",
                     "One filters before grouping, the other after.", "HAVING works on aggregated results.",
                     "WHERE filters individual rows prior to GROUP BY; HAVING filters grouped results post-aggregation."),
        create_mcq_q("Which clause must precede HAVING in standard SQL?",
                     "SELECT dept, COUNT(*) FROM emp _______ HAVING COUNT(*) > 2;",
                     ["A) ORDER BY", "B) GROUP BY", "C) LIMIT", "D) WHERE"], "B",
                     "HAVING applies to groups formed by this clause.", "GROUP BY.",
                     "HAVING filters groups created by the GROUP BY clause."),
        create_mcq_q("What will happen if you SELECT a non-aggregated column that is not in GROUP BY?",
                     "SELECT dept, employee_name, COUNT(*) FROM emp GROUP BY dept;",
                     ["A) Always runs without issues in all SQL dialects",
                      "B) Strictly violates standard SQL and fails in SQLite (modern) and Postgres",
                      "C) Deletes the column automatically",
                      "D) Returns NULL for all rows"], "B",
                     "Standard SQL requires non-aggregated selected columns to be grouped.", "Syntax error in ANSI SQL.",
                     "Standard SQL requires every non-aggregate projection column to appear in GROUP BY."),
        create_mcq_q("Which statement filters groups with an average order value over 250?",
                     None,
                     ["A) WHERE AVG(order_total) > 250",
                      "B) HAVING AVG(order_total) > 250",
                      "C) GROUP BY order_total > 250",
                      "D) ORDER BY AVG(order_total) > 250"], "B",
                     "Aggregate conditions cannot appear in WHERE.", "Use HAVING for aggregate filters.",
                     "HAVING is required when filtering on aggregated expressions like AVG()."),
        create_mcq_q("How many rows are returned by 'SELECT COUNT(DISTINCT dept) FROM emp' if emp has 10 rows with 3 unique depts?",
                     None,
                     ["A) 10", "B) 3", "C) 1", "D) 0"], "C",
                     "COUNT returns a single scalar number.", "The count of unique depts is 3.",
                     "COUNT returns 1 row containing the scalar result 3.")
    ]

    sql["MCQ Challenge"]["Intermediate"]["2"] = [
        create_mcq_q("Which JOIN returns ONLY rows where there is a match in BOTH tables?",
                     None,
                     ["A) LEFT JOIN", "B) INNER JOIN", "C) RIGHT JOIN", "D) FULL OUTER JOIN"], "B",
                     "Intersection of both sets.", "Default join type.",
                     "INNER JOIN returns only records where the join predicate matches in both tables."),
        create_mcq_q("If table A has 5 rows and table B has no matching rows for A, how many rows does 'A LEFT JOIN B' return?",
                     None,
                     ["A) 0", "B) 5", "C) 10", "D) NULL"], "B",
                     "LEFT JOIN preserves all rows from the left table.", "Left table has 5 rows.",
                     "LEFT JOIN guarantees all rows from the left table are returned (with NULLs for right columns)."),
        create_mcq_q("What keyword specifies the join condition between two tables?",
                     "SELECT * FROM a JOIN b _______ a.id = b.a_id;",
                     ["A) WITH", "B) USING_ALL", "C) ON", "D) MATCH"], "C",
                     "2 letters.", "ON clause.",
                     "ON specifies the condition linking related columns across tables."),
        create_mcq_q("What is a Cartesian product (CROSS JOIN)?",
                     None,
                     ["A) A join that matches primary keys only",
                      "B) A join combining every row of the first table with every row of the second",
                      "C) A join that eliminates all duplicates",
                      "D) A join that returns empty sets"], "B",
                     "Multiplying row sets (m * n).", "Every combination.",
                     "CROSS JOIN produces a Cartesian product matching every left row with every right row."),
        create_mcq_q("What does a self-join do?",
                     "SELECT e.name, m.name FROM emp e JOIN emp m ON e.mgr_id = m.id;",
                     ["A) Joins a database with another database",
                      "B) Joins a table to itself using aliases",
                      "C) Automatically updates the primary key",
                      "D) Creates a duplicate copy of the table"], "B",
                     "Joining the same table twice.", "Used for hierarchies like employee and manager.",
                     "A self-join joins a table with itself using distinct table aliases.")
    ]

    sql["MCQ Challenge"]["Intermediate"]["3"] = [
        create_mcq_q("Which operator checks if a value matches any value in a subquery or list?",
                     "SELECT * FROM items WHERE category_id _______ (1, 2, 3);",
                     ["A) LIKE", "B) IN", "C) BETWEEN", "D) MATCHES"], "B",
                     "2-letter membership operator.", "IN keyword.",
                     "IN determines whether a specified value matches any value in a subquery or list."),
        create_mcq_q("What does the '%' wildcard represent in a SQL LIKE pattern?",
                     "SELECT * FROM users WHERE name LIKE 'A%';",
                     ["A) Exactly one character", "B) Zero, one, or multiple characters", "C) Only digits", "D) Any vowel"], "B",
                     "Matches arbitrary length string.", "Percent symbol.",
                     "'%' matches zero or more characters in LIKE expressions."),
        create_mcq_q("What does the '_' (underscore) wildcard represent in SQL LIKE?",
                     "SELECT * FROM codes WHERE code LIKE 'A_C';",
                     ["A) Any single character", "B) Any number of characters", "C) An underscore literal", "D) A whitespace"], "A",
                     "Single character placeholder.", "Exactly one character.",
                     "'_' matches exactly one single character in LIKE."),
        create_mcq_q("Is 'price BETWEEN 10 AND 20' inclusive of 10 and 20?",
                     None,
                     ["A) No, strictly exclusive (11-19)",
                      "B) Yes, inclusive of both 10 and 20",
                      "C) Only includes 10",
                      "D) Only includes 20"], "B",
                     "BETWEEN in SQL is inclusive on both ends.", ">= 10 AND <= 20.",
                     "BETWEEN low AND high is inclusive of both boundary endpoints."),
        create_mcq_q("Which operator returns TRUE if a subquery returns at least one row?",
                     "SELECT * FROM customers c WHERE _______ (SELECT 1 FROM orders o WHERE o.c_id = c.id);",
                     ["A) CONTAINS", "B) EXISTS", "C) HAS_ROWS", "D) SOME"], "B",
                     "6 letters starting with E.", "EXISTS operator.",
                     "EXISTS returns TRUE as soon as the inner subquery produces at least one matching row.")
    ]

    sql["MCQ Challenge"]["Intermediate"]["4"] = [
        create_mcq_q("What is the difference between UNION and UNION ALL?",
                     None,
                     ["A) UNION keeps duplicates; UNION ALL removes them",
                      "B) UNION removes duplicate rows; UNION ALL retains all rows",
                      "C) UNION works on tables; UNION ALL works on views",
                      "D) UNION ALL is not valid SQL"], "B",
                     "UNION implies distinct deduplication.", "UNION ALL is faster because it does not deduplicate.",
                     "UNION removes duplicate rows across datasets; UNION ALL preserves all rows."),
        create_mcq_q("How does a CASE statement end in SQL?",
                     "CASE WHEN x > 0 THEN 'Pos' ELSE 'Zero' _______",
                     ["A) STOP", "B) END", "C) DONE", "D) FINISH"], "B",
                     "3 letters.", "END keyword.",
                     "CASE statements terminate with the END keyword (e.g. END AS alias)."),
        create_mcq_q("What is the requirement for combining two queries with UNION?",
                     None,
                     ["A) Both queries must reference the exact same table",
                      "B) Both queries must have the same number of columns with compatible data types",
                      "C) Both queries must contain an ORDER BY clause",
                      "D) Both queries must have less than 100 rows"], "B",
                     "Column count and types must align.", "Positional schema compatibility.",
                     "UNION requires both SELECT statements to have matching column counts and compatible types."),
        create_mcq_q("What is a Database View?",
                     None,
                     ["A) A physical copy of data stored in memory",
                      "B) A virtual table based on the result-set of a stored SQL query",
                      "C) A graphical user interface tool",
                      "D) An index on the primary key"], "B",
                     "Virtual table definition.", "CREATE VIEW stores query logic.",
                     "A view is a stored virtual table executing an underlying SELECT query dynamically."),
        create_mcq_q("In a CASE statement, what does the ELSE branch provide?",
                     None,
                     ["A) An infinite loop safeguard",
                      "B) The default value if no WHEN condition evaluates to TRUE",
                      "C) A syntax error handler",
                      "D) Automatic NULL casting"], "B",
                     "Fallback return value.", "Default branch.",
                     "ELSE specifies the fallback result when no prior WHEN clause evaluates to true.")
    ]

    # Advanced
    sql["MCQ Challenge"]["Advanced"]["1"] = [
        create_mcq_q("What clause turns an aggregate function into a window function?",
                     "SELECT salary, AVG(salary) _______ () FROM employees;",
                     ["A) WINDOW", "B) OVER", "C) PARTITION", "D) ACROSS"], "B",
                     "4 letters starting with O.", "OVER clause.",
                     "The OVER() clause defines the window framing for window functions."),
        create_mcq_q("What is the difference between RANK() and DENSE_RANK()?",
                     None,
                     ["A) RANK leaves gaps in ranking numbers after ties; DENSE_RANK does not leave gaps",
                      "B) DENSE_RANK leaves gaps; RANK does not",
                      "C) RANK works on strings; DENSE_RANK works on numbers",
                      "D) They produce identical results"], "A",
                     "Ties in RANK (1, 2, 2, 4) vs DENSE_RANK (1, 2, 2, 3).", "DENSE leaves no gaps.",
                     "RANK skips ranks after ties (1, 2, 2, 4), whereas DENSE_RANK produces contiguous ranks (1, 2, 2, 3)."),
        create_mcq_q("What does PARTITION BY inside an OVER clause do?",
                     "ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY hire_date)",
                     ["A) Divides the table physically on disk",
                      "B) Resets the window calculation for each distinct partition group",
                      "C) Deletes duplicate records",
                      "D) Sorts the overall output table"], "B",
                     "Divides the result set into subsets for independent calculation.", "Resets numbering per group.",
                     "PARTITION BY divides rows into partitions where window calculations execute independently."),
        create_mcq_q("Which window function retrieves a value from the following (subsequent) row?",
                     None,
                     ["A) LAG()", "B) LEAD()", "C) NEXT()", "D) FORWARD()"], "B",
                     "Opposite of LAG().", "LEAD looks forward.",
                     "LEAD(col, offset) accesses data from subsequent rows without an explicit self-join."),
        create_mcq_q("What is the default window frame specification when ORDER BY is present in OVER()?",
                     None,
                     ["A) ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING",
                      "B) RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW",
                      "C) ALL ROWS IN PARTITION",
                      "D) ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING"], "B",
                     "Accumulates from the start of the partition up to the current row.", "Cumulative range.",
                     "By default, ORDER BY inside OVER() implies RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.")
    ]

    sql["MCQ Challenge"]["Advanced"]["2"] = [
        create_mcq_q("What keyword initiates a Common Table Expression (CTE)?",
                     "_______ CTE_Name AS (SELECT * FROM table1) SELECT * FROM CTE_Name;",
                     ["A) CTE", "B) WITH", "C) AS", "D) LET"], "B",
                     "4 letters starting with W.", "WITH clause.",
                     "A CTE begins with the WITH keyword: WITH cte_name AS (...)."),
        create_mcq_q("What modifier is required for a CTE that references itself recursively?",
                     "WITH _______ MyCTE AS (...) SELECT * FROM MyCTE;",
                     ["A) LOOP", "B) RECURSIVE", "C) REPEAT", "D) ITERATIVE"], "B",
                     "Starts with R.", "RECURSIVE.",
                     "WITH RECURSIVE is standard syntax for defining recursive CTEs in SQLite/Postgres/MySQL."),
        create_mcq_q("What two parts make up a recursive CTE?",
                     None,
                     ["A) Master query and Detail query",
                      "B) Anchor member and Recursive member (joined by UNION / UNION ALL)",
                      "C) Head and Tail loops",
                      "D) Try block and Catch block"], "B",
                     "Anchor starts base case; recursive member steps through iterations.", "Anchor + Recursive.",
                     "A recursive CTE contains an anchor query and a recursive query joined by UNION ALL."),
        create_mcq_q("What is a key advantage of CTEs over nested subqueries?",
                     None,
                     ["A) CTEs bypass all database security checks",
                      "B) CTEs dramatically enhance readability and can be referenced multiple times",
                      "C) CTEs run in O(1) time complexity always",
                      "D) CTEs convert SQL to C++ code"], "B",
                     "Improves clean query structure and modularity.", "Readable and reusable.",
                     "CTEs clarify complex multi-step queries and allow reuse within the same query scope."),
        create_mcq_q("Can multiple CTEs be defined in a single WITH statement?",
                     None,
                     ["A) No, only one CTE per query is permitted",
                      "B) Yes, separated by commas (WITH a AS (...), b AS (...))",
                      "C) Only in Oracle database",
                      "D) Yes, but only if they query different databases"], "B",
                     "Separate CTE definitions using commas.", "WITH cte1 AS (...), cte2 AS (...).",
                     "Multiple CTEs are separated by commas under a single leading WITH keyword.")
    ]

    sql["MCQ Challenge"]["Advanced"]["3"] = [
        create_mcq_q("What do the letters in ACID stand for in database management?",
                     None,
                     ["A) Atomicity, Consistency, Isolation, Durability",
                      "B) Asynchronous, Concurrent, Indexed, Distributed",
                      "C) Access, Control, Integrity, Definition",
                      "D) Accurate, Compact, Immutable, Durable"], "A",
                     "Core properties of transactional databases.", "A-C-I-D.",
                     "ACID stands for Atomicity, Consistency, Isolation, and Durability."),
        create_mcq_q("What command commits a pending transaction, persisting all changes permanently?",
                     None,
                     ["A) SAVE", "B) COMMIT", "C) APPLY", "D) PERSIST"], "B",
                     "6 letters starting with C.", "COMMIT statement.",
                     "COMMIT makes all data modifications of the current transaction permanent."),
        create_mcq_q("What is the primary purpose of a database index (e.g. B-Tree index)?",
                     None,
                     ["A) To compress the database to take zero storage space",
                      "B) To speed up data retrieval (SELECT) operations at the cost of additional write overhead",
                      "C) To encrypt sensitive column data",
                      "D) To prevent tables from exceeding 1,000 rows"], "B",
                     "Think about search speed vs write performance.", "Speeds up lookups.",
                     "Indexes optimize search and retrieval speeds while introducing slight overhead on INSERT/UPDATE."),
        create_mcq_q("What does 'ON DELETE CASCADE' do on a Foreign Key constraint?",
                     None,
                     ["A) Prevents deletion of the parent record",
                      "B) Automatically deletes child rows when the referenced parent row is deleted",
                      "C) Sets child foreign keys to NULL",
                      "D) Drops the child table completely"], "B",
                     "Cascades deletion from parent to child.", "Removes orphaned records.",
                     "ON DELETE CASCADE deletes corresponding child rows whenever the parent row is deleted."),
        create_mcq_q("Which index type enforces that no two rows can have the same value in indexed columns?",
                     None,
                     ["A) BITMAP INDEX", "B) UNIQUE INDEX", "C) CLUSTERED INDEX", "D) SPATIAL INDEX"], "B",
                     "Prevents duplicates.", "UNIQUE constraint backed by index.",
                     "A UNIQUE INDEX prevents duplicate values from being inserted into indexed columns.")
    ]

    sql["MCQ Challenge"]["Advanced"]["4"] = [
        create_mcq_q("What does COALESCE(val1, val2, val3) do?",
                     None,
                     ["A) Combines strings with hyphens",
                      "B) Returns the first non-NULL expression among its arguments",
                      "C) Calculates the average of non-zero numbers",
                      "D) Replaces all spaces with underscores"], "B",
                     "Finds the first non-null argument.", "COALESCE function.",
                     "COALESCE returns the first non-null expression from left to right."),
        create_mcq_q("When should you prefer EXISTS over IN for subquery filtering?",
                     None,
                     ["A) Never, IN is always superior",
                      "B) When the subquery evaluates a large dataset or contains NULL values",
                      "C) Only for SQLite memory tables",
                      "D) When comparing floating-point numbers only"], "B",
                     "EXISTS short-circuits on first match and handles NULL safely.", "Performance on large sets.",
                     "EXISTS short-circuits immediately upon finding a match and handles NULL subquery values safely."),
        create_mcq_q("What does the EXPLAIN QUERY PLAN statement do in SQL?",
                     "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE user_id = 42;",
                     ["A) Automatically rewrites and fixes bugs in the query",
                      "B) Shows how the database execution engine plans to scan tables and use indexes",
                      "C) Runs the query in benchmark mode 1,000 times",
                      "D) Deletes unused tables"], "B",
                     "Shows execution strategy.", "Index scans vs table scans.",
                     "EXPLAIN QUERY PLAN displays the execution strategy (e.g. index search vs full table scan)."),
        create_mcq_q("What does NTILE(4) compute for a result set of 100 rows?",
                     None,
                     ["A) 4 rows only",
                      "B) Divides the 100 rows into 4 equal quartiles (1, 2, 3, 4) of 25 rows each",
                      "C) Multiplies each row by 4",
                      "D) Ranks the top 4 rows"], "B",
                     "Splits into 4 equal buckets.", "Quartiles.",
                     "NTILE(4) segments the ordered rows into 4 equal buckets numbered 1 to 4."),
        create_mcq_q("What happens in SQL when a NULL is compared with anything using '=' (e.g. NULL = NULL)?",
                     None,
                     ["A) Evaluates to TRUE",
                      "B) Evaluates to FALSE",
                      "C) Evaluates to UNKNOWN (Three-Valued Logic)",
                      "D) Throws a NullPointerException"], "C",
                     "Three-Valued Logic in SQL.", "Neither True nor False.",
                     "In SQL Three-Valued Logic, comparing with NULL using = evaluates to UNKNOWN.")
    ]

    # =========================================================================
    # 3. FILL IN THE BLANKS (fill)
    # =========================================================================
    # Beginner
    sql["Fill in the Blanks"]["Beginner"]["1"] = [
        create_fill_q("Retrieve all records from the 'customers' table.", "SELECT * _______ customers;", "FROM", "Keyword specifying table source.", "4 letters.", "FROM specifies source table."),
        create_fill_q("Filter rows where status is active.", "SELECT * FROM accounts _______ status = 'active';", "WHERE", "Row filtering keyword.", "5 letters.", "WHERE filters rows before returning."),
        create_fill_q("Select only unique department names.", "SELECT _______ department FROM employees;", "DISTINCT", "Keyword removing duplicates.", "8 letters.", "DISTINCT removes duplicates."),
        create_fill_q("Project specific column from products.", "_______ product_name FROM products;", "SELECT", "Query projection keyword.", "6 letters.", "SELECT projects columns."),
        create_fill_q("Find items where stock is greater than 10.", "SELECT name FROM inventory WHERE stock _______ 10;", ">", "Greater-than operator.", "Single symbol.", "> checks strictly greater than.")
    ]

    sql["Fill in the Blanks"]["Beginner"]["2"] = [
        create_fill_q("Sort rows by salary in ascending order.", "SELECT name FROM employees ORDER BY salary _______;", "ASC", "Keyword for ascending.", "3 letters.", "ASC sorts ascending."),
        create_fill_q("Sort products by price in descending order.", "SELECT title FROM books ORDER BY price _______;", "DESC", "Keyword for descending.", "4 letters.", "DESC sorts descending."),
        create_fill_q("Limit result to 5 rows.", "SELECT * FROM articles ORDER BY id DESC _______ 5;", "LIMIT", "Keyword restricting row count.", "5 letters.", "LIMIT restricts rows."),
        create_fill_q("Combine conditions requiring both to be true.", "SELECT * FROM users WHERE active = 1 _______ verified = 1;", "AND", "Logical conjunction.", "3 letters.", "AND requires both conditions."),
        create_fill_q("Match either condition.", "SELECT * FROM flights WHERE origin = 'JFK' _______ origin = 'LGA';", "OR", "Logical disjunction.", "2 letters.", "OR matches either condition.")
    ]

    sql["Fill in the Blanks"]["Beginner"]["3"] = [
        create_fill_q("Insert a new record into table.", "INSERT _______ users (name) VALUES ('Sam');", "INTO", "Preposition following INSERT.", "4 letters.", "INSERT INTO adds records."),
        create_fill_q("Update column value in existing records.", "UPDATE users _______ role = 'admin' WHERE id = 1;", "SET", "Keyword assigning values in UPDATE.", "3 letters.", "SET assigns new values."),
        create_fill_q("Remove records from table.", "_______ FROM logs WHERE created_at < '2022-01-01';", "DELETE", "Keyword for record deletion.", "6 letters.", "DELETE FROM removes rows."),
        create_fill_q("Check for missing NULL values.", "SELECT * FROM orders WHERE shipped_date IS _______;", "NULL", "Keyword for null state.", "4 letters.", "IS NULL checks for missing values."),
        create_fill_q("Specify data values to be inserted.", "INSERT INTO tags (name) _______ ('database');", "VALUES", "Keyword introducing row values.", "6 letters.", "VALUES supplies row data.")
    ]

    sql["Fill in the Blanks"]["Beginner"]["4"] = [
        create_fill_q("Count all rows in orders table.", "SELECT _______(*) FROM orders;", "COUNT", "Counting function.", "5 letters.", "COUNT(*) counts all rows."),
        create_fill_q("Calculate sum of order totals.", "SELECT _______(amount) FROM payments;", "SUM", "Summation function.", "3 letters.", "SUM() totals values."),
        create_fill_q("Compute average score.", "SELECT _______(score) FROM exams;", "AVG", "Average function abbreviation.", "3 letters.", "AVG() computes arithmetic mean."),
        create_fill_q("Alias column header in output.", "SELECT count(*) _______ total_users FROM users;", "AS", "Aliasing keyword.", "2 letters.", "AS provides alias."),
        create_fill_q("Find minimum price.", "SELECT _______(price) FROM items;", "MIN", "Minimum function abbreviation.", "3 letters.", "MIN() returns lowest value.")
    ]

    # Intermediate
    sql["Fill in the Blanks"]["Intermediate"]["1"] = [
        create_fill_q("Group records by category.", "SELECT category, count(*) FROM products _______ BY category;", "GROUP", "Keyword preceding BY for grouping.", "5 letters.", "GROUP BY aggregates rows."),
        create_fill_q("Filter aggregated groups.", "SELECT dept, count(*) FROM emp GROUP BY dept _______ count(*) > 3;", "HAVING", "Post-aggregation filter keyword.", "6 letters.", "HAVING filters groups."),
        create_fill_q("Check membership in a set of values.", "SELECT * FROM products WHERE id _______ (10, 20, 30);", "IN", "Membership operator.", "2 letters.", "IN checks set inclusion."),
        create_fill_q("Check if value falls within an inclusive range.", "SELECT * FROM sales WHERE amount _______ 100 AND 500;", "BETWEEN", "Range operator.", "7 letters.", "BETWEEN checks inclusive range."),
        create_fill_q("Pattern matching operator.", "SELECT * FROM users WHERE username _______ 'dev_%';", "LIKE", "Wildcard string comparison.", "4 letters.", "LIKE matches string patterns.")
    ]

    sql["Fill in the Blanks"]["Intermediate"]["2"] = [
        create_fill_q("Join two tables matching foreign key.", "SELECT * FROM orders o INNER _______ customers c ON o.c_id = c.id;", "JOIN", "Joining keyword.", "4 letters.", "INNER JOIN connects tables."),
        create_fill_q("Specify join condition predicate.", "SELECT * FROM a JOIN b _______ a.id = b.a_id;", "ON", "Join predicate keyword.", "2 letters.", "ON defines link condition."),
        create_fill_q("Preserve all left rows even if no match.", "SELECT * FROM users u _______ JOIN profiles p ON u.id = p.u_id;", "LEFT", "Left outer join keyword.", "4 letters.", "LEFT JOIN preserves left table."),
        create_fill_q("Check if subquery returns any rows.", "SELECT * FROM users u WHERE _______ (SELECT 1 FROM orders WHERE user_id = u.id);", "EXISTS", "Existence operator.", "6 letters.", "EXISTS checks subquery presence."),
        create_fill_q("Reverse membership condition.", "SELECT * FROM items WHERE id NOT _______ (SELECT item_id FROM sales);", "IN", "Negated membership keyword.", "2 letters.", "NOT IN filters non-members.")
    ]

    sql["Fill in the Blanks"]["Intermediate"]["3"] = [
        create_fill_q("Match end of string with LIKE.", "SELECT * FROM emails WHERE address LIKE '%@_______';", "com", "Domain extension in pattern.", "3 letters.", "%@com matches domain ending in com."),
        create_fill_q("Initiate conditional CASE expression.", "SELECT name, _______ WHEN score >= 60 THEN 'Pass' ELSE 'Fail' END FROM students;", "CASE", "Conditional expression start.", "4 letters.", "CASE begins conditional block."),
        create_fill_q("Provide default branch in CASE statement.", "SELECT CASE WHEN x = 1 THEN 'A' _______ 'B' END;", "ELSE", "Fallback conditional keyword.", "4 letters.", "ELSE provides default."),
        create_fill_q("Close conditional CASE expression.", "SELECT CASE WHEN active = 1 THEN 'Yes' ELSE 'No' _______ AS status FROM users;", "END", "Closing keyword for CASE.", "3 letters.", "END terminates CASE expression."),
        create_fill_q("Combine two query results removing duplicates.", "SELECT city FROM clients _______ SELECT city FROM suppliers;", "UNION", "Set union operator.", "5 letters.", "UNION merges distinct rows.")
    ]

    sql["Fill in the Blanks"]["Intermediate"]["4"] = [
        create_fill_q("Combine queries preserving duplicate rows.", "SELECT id FROM t1 UNION _______ SELECT id FROM t2;", "ALL", "Keyword modifying UNION.", "3 letters.", "UNION ALL preserves duplicates."),
        create_fill_q("Create a virtual table view.", "CREATE _______ active_users AS SELECT * FROM users WHERE active = 1;", "VIEW", "Virtual table keyword.", "4 letters.", "CREATE VIEW defines stored query."),
        create_fill_q("Filter rows where column is not null.", "SELECT * FROM contacts WHERE phone IS NOT _______;", "NULL", "Keyword for null value.", "4 letters.", "IS NOT NULL checks present values."),
        create_fill_q("Count non-null occurrences of a column.", "SELECT COUNT(_______) FROM users;", "id", "Primary key column name.", "2 letters.", "COUNT(id) counts non-null IDs."),
        create_fill_q("Check secondary condition in CASE statement.", "CASE WHEN x = 1 THEN 'One' _______ x = 2 THEN 'Two' ELSE 'Other' END", "WHEN", "Subsequent branch keyword.", "4 letters.", "WHEN tests each case branch.")
    ]

    # Advanced
    sql["Fill in the Blanks"]["Advanced"]["1"] = [
        create_fill_q("Define window execution specification.", "SELECT val, ROW_NUMBER() _______ (ORDER BY val) FROM t;", "OVER", "Window function clause keyword.", "4 letters.", "OVER specifies window framing."),
        create_fill_q("Divide window calculation into partitions.", "SELECT dept, salary, RANK() OVER (_______ BY dept ORDER BY salary DESC) FROM emp;", "PARTITION", "Keyword before BY in window function.", "9 letters.", "PARTITION BY groups window frames."),
        create_fill_q("Access value from preceding row.", "SELECT day, rev, _______(rev, 1) OVER (ORDER BY day) FROM sales;", "LAG", "Function accessing previous row.", "3 letters.", "LAG() retrieves earlier row values."),
        create_fill_q("Access value from subsequent row.", "SELECT day, rev, _______(rev, 1) OVER (ORDER BY day) FROM sales;", "LEAD", "Function accessing following row.", "4 letters.", "LEAD() retrieves next row values."),
        create_fill_q("Assign contiguous rank without gaps.", "SELECT salary, ________RANK() OVER (ORDER BY salary DESC) FROM emp;", "DENSE", "Prefix for gapless rank.", "5 letters.", "DENSE_RANK() leaves no gaps.")
    ]

    sql["Fill in the Blanks"]["Advanced"]["2"] = [
        create_fill_q("Declare Common Table Expression.", "_______ UserTotals AS (SELECT user_id, sum(amt) FROM orders GROUP BY user_id) SELECT * FROM UserTotals;", "WITH", "CTE initiating keyword.", "4 letters.", "WITH introduces CTE."),
        create_fill_q("Enable recursive self-referencing in CTE.", "WITH _______ TreeCTE AS (SELECT id, parent_id FROM nodes) SELECT * FROM TreeCTE;", "RECURSIVE", "Modifier for recursive CTE.", "9 letters.", "WITH RECURSIVE enables recursion."),
        create_fill_q("Return first non-null argument.", "SELECT _______(nickname, full_name, 'Anonymous') FROM profiles;", "COALESCE", "Function returning first non-null.", "8 letters.", "COALESCE returns first non-null."),
        create_fill_q("Segment rows into N buckets.", "SELECT score, _______(4) OVER (ORDER BY score DESC) FROM students;", "NTILE", "Bucket segmentation function.", "5 letters.", "NTILE(n) divides into n buckets."),
        create_fill_q("Generate sequential integer per row in window.", "SELECT _______() OVER (ORDER BY created_at) FROM logs;", "ROW_NUMBER", "Sequential row numbering function.", "10 letters with underscore.", "ROW_NUMBER() numbers rows 1, 2, 3...")
    ]

    sql["Fill in the Blanks"]["Advanced"]["3"] = [
        create_fill_q("Start database transaction.", "_______ TRANSACTION;", "BEGIN", "Keyword starting transaction.", "5 letters.", "BEGIN TRANSACTION starts transaction."),
        create_fill_q("Commit transaction permanently.", "_______;", "COMMIT", "Keyword persisting transaction.", "6 letters.", "COMMIT writes changes permanently."),
        create_fill_q("Revert changes in uncommitted transaction.", "_______;", "ROLLBACK", "Keyword undoing transaction.", "8 letters.", "ROLLBACK reverts modifications."),
        create_fill_q("Create unique index on column.", "CREATE _______ INDEX idx_email ON users(email);", "UNIQUE", "Keyword enforcing unique constraint.", "6 letters.", "CREATE UNIQUE INDEX enforces uniqueness."),
        create_fill_q("Cascade deletion to child records.", "FOREIGN KEY (dept_id) REFERENCES departments(id) ON DELETE _______;", "CASCADE", "Keyword cascading deletion.", "7 letters.", "ON DELETE CASCADE removes children.")
    ]

    sql["Fill in the Blanks"]["Advanced"]["4"] = [
        create_fill_q("Inspect query execution plan in SQLite/Postgres.", "_______ QUERY PLAN SELECT * FROM users WHERE id = 1;", "EXPLAIN", "Keyword analyzing execution plan.", "7 letters.", "EXPLAIN displays query execution plan."),
        create_fill_q("Add check constraint to table.", "ALTER TABLE products ADD CONSTRAINT chk_qty _______ (stock >= 0);", "CHECK", "Integrity constraint keyword.", "5 letters.", "CHECK enforces validation rules."),
        create_fill_q("Accumulate running total up to current row.", "SUM(amt) OVER (ORDER BY dt ROWS BETWEEN UNBOUNDED _______ AND CURRENT ROW)", "PRECEDING", "Frame start boundary keyword.", "9 letters.", "UNBOUNDED PRECEDING starts from partition head."),
        create_fill_q("Define primary key constraint inline.", "CREATE TABLE t (id INT PRIMARY _______, name TEXT);", "KEY", "Keyword completing PRIMARY KEY.", "3 letters.", "PRIMARY KEY defines uniqueness and index."),
        create_fill_q("Drop index from database.", "_______ INDEX idx_old_perf;", "DROP", "Keyword removing index.", "4 letters.", "DROP INDEX deletes an index.")
    ]

    # =========================================================================
    # 4. DEBUG THE CODE (debug)
    # =========================================================================
    # Beginner
    sql["Debug the Code"]["Beginner"]["1"] = [
        create_debug_q("Fix the comparison operator checking for equality in SQL.",
                       "SELECT * FROM users WHERE status == 'active';",
                       "=", "SQL does not use double equals for equality.", "Single equal sign.", "Use single '=' for equality in SQL."),
        create_debug_q("Fix the clause name used to specify the source table.",
                       "SELECT name IN employees;",
                       "FROM", "Which keyword specifies the table being queried?", "Starts with F.", "FROM specifies the table to query."),
        create_debug_q("Fix the quote style: SQL strings must use single quotes.",
                       "SELECT * FROM items WHERE category = \"books\";",
                       "'books'", "Standard SQL strings use single quotes, not double quotes.", "Enclose in single quotes.", "String literals in standard SQL are enclosed in single quotes."),
        create_debug_q("Fix the keyword used to retrieve columns.",
                       "GET first_name, email FROM contacts;",
                       "SELECT", "SQL uses SELECT, not GET.", "Starts with S.", "SELECT is the SQL statement for data retrieval."),
        create_debug_q("Fix the wildcard used to select all columns.",
                       "SELECT ALL_COLUMNS FROM inventory;",
                       "*", "Use the standard asterisk wildcard.", "Single symbol *.", "* selects all columns from the table.")
    ]

    sql["Debug the Code"]["Beginner"]["2"] = [
        create_debug_q("Fix the ordering keyword to sort from highest to lowest.",
                       "SELECT * FROM products ORDER BY price DOWN;",
                       "DESC", "What is the keyword for descending order?", "4 letters starting with D.", "DESC specifies descending sort order."),
        create_debug_q("Fix the clause used to sort query results.",
                       "SELECT * FROM users SORT BY username ASC;",
                       "ORDER BY", "SQL uses ORDER BY, not SORT BY.", "Two words: ORDER BY.", "ORDER BY is the correct SQL syntax for sorting."),
        create_debug_q("Fix the logical operator: both conditions must be true.",
                       "SELECT * FROM orders WHERE paid = 1 && shipped = 1;",
                       "AND", "SQL uses the word AND, not C-style &&.", "3 letters.", "AND is the SQL logical conjunction operator."),
        create_debug_q("Fix the keyword limiting rows returned in SQLite.",
                       "SELECT * FROM logs ORDER BY id DESC TOP 10;",
                       "LIMIT", "SQLite uses LIMIT at the end, not TOP.", "5 letters starting with L.", "LIMIT 10 restricts row count in SQLite/Postgres/MySQL."),
        create_debug_q("Fix the inequality operator typo.",
                       "SELECT * FROM scores WHERE points !- 0;",
                       "!=", "Inequality operator is != or <>.", "Exclamation with equal.", "!= or <> represents inequality in SQL.")
    ]

    sql["Debug the Code"]["Beginner"]["3"] = [
        create_debug_q("Fix the incorrect NULL comparison operator.",
                       "SELECT * FROM users WHERE email = NULL;",
                       "IS NULL", "NULL cannot be checked with '='.", "Use IS NULL.", "NULL comparisons must use IS NULL, not = NULL."),
        create_debug_q("Fix the statement keyword used to add a new record.",
                       "ADD INTO users (name) VALUES ('Bob');",
                       "INSERT INTO", "SQL uses INSERT INTO, not ADD INTO.", "INSERT INTO.", "INSERT INTO is the standard command to add rows."),
        create_debug_q("Fix the keyword used to assign values in UPDATE.",
                       "UPDATE products WITH price = 19.99 WHERE id = 4;",
                       "SET", "UPDATE uses SET, not WITH.", "3 letters.", "SET specifies column assignments in UPDATE."),
        create_debug_q("Fix the keyword introducing values in an INSERT statement.",
                       "INSERT INTO tags (name) DATA ('sql');",
                       "VALUES", "Values are introduced by VALUES, not DATA.", "6 letters.", "VALUES introduces the list of row values."),
        create_debug_q("Fix the check for present non-null values.",
                       "SELECT * FROM orders WHERE delivery_date IS NOTEMPTY;",
                       "IS NOT NULL", "Standard check is IS NOT NULL.", "Three words: IS NOT NULL.", "IS NOT NULL filters for present, non-missing values.")
    ]

    sql["Debug the Code"]["Beginner"]["4"] = [
        create_debug_q("Fix the aggregate function name for finding average.",
                       "SELECT AVERAGE(score) FROM tests;",
                       "AVG", "SQL abbreviates average as AVG.", "3 letters.", "AVG() is the standard aggregate function for mean."),
        create_debug_q("Fix the aggregate function name for counting records.",
                       "SELECT TOTAL_ROWS(*) FROM orders;",
                       "COUNT", "Counting function is COUNT.", "5 letters.", "COUNT(*) counts rows in SQL."),
        create_debug_q("Fix the summation function name.",
                       "SELECT SUMMATION(revenue) FROM sales;",
                       "SUM", "SQL uses SUM(), not SUMMATION().", "3 letters.", "SUM() is the standard SQL sum function."),
        create_debug_q("Fix the alias keyword used to rename column output.",
                       "SELECT count(*) NAME total_items FROM items;",
                       "AS", "Use AS to specify an alias.", "2 letters.", "AS specifies column aliases in SQL."),
        create_debug_q("Fix the function name for finding the maximum value.",
                       "SELECT MAXIMUM(salary) FROM employees;",
                       "MAX", "SQL uses MAX(), not MAXIMUM().", "3 letters.", "MAX() finds the highest value in a column.")
    ]

    # Intermediate
    sql["Debug the Code"]["Intermediate"]["1"] = [
        create_debug_q("Fix the misplaced filter: aggregate filter placed in WHERE clause.",
                       "SELECT dept, COUNT(*) FROM emp WHERE COUNT(*) > 5 GROUP BY dept;",
                       "HAVING COUNT(*) > 5", "Filter on COUNT(*) must be in HAVING after GROUP BY.", "Use HAVING.", "Aggregates cannot appear in WHERE; use HAVING after GROUP BY."),
        create_debug_q("Fix the keyword used to group rows together.",
                       "SELECT category, AVG(price) FROM products CLUSTER BY category;",
                       "GROUP BY", "SQL uses GROUP BY for aggregation, not CLUSTER BY.", "GROUP BY.", "GROUP BY groups rows for aggregate functions."),
        create_debug_q("Fix the set membership operator checking a list of values.",
                       "SELECT * FROM items WHERE id INSIDE (1, 2, 3);",
                       "IN", "SQL uses IN, not INSIDE.", "2 letters.", "IN checks membership in a list or subquery."),
        create_debug_q("Fix the range operator syntax.",
                       "SELECT * FROM sales WHERE amount BETWEEN 50 TO 100;",
                       "BETWEEN 50 AND 100", "BETWEEN uses 'AND', not 'TO'.", "Use AND between the limits.", "BETWEEN a AND b connects boundaries with AND."),
        create_debug_q("Fix the wildcard operator used for pattern matching.",
                       "SELECT * FROM users WHERE name MATCHES 'John%';",
                       "LIKE", "SQL standard string pattern matching uses LIKE.", "4 letters.", "LIKE is the pattern matching operator in SQL.")
    ]

    sql["Debug the Code"]["Intermediate"]["2"] = [
        create_debug_q("Fix the join condition keyword.",
                       "SELECT * FROM orders o JOIN customers c WHERE o.c_id = c.id;",
                       "ON o.c_id = c.id", "JOIN condition uses ON, not WHERE.", "Replace WHERE with ON for the join.", "ON specifies join conditions in explicit JOIN syntax."),
        create_debug_q("Fix the keyword for left outer join.",
                       "SELECT * FROM emp e OUTER_LEFT JOIN dept d ON e.d_id = d.id;",
                       "LEFT JOIN", "Standard syntax is LEFT JOIN or LEFT OUTER JOIN.", "LEFT JOIN.", "LEFT JOIN is the standard syntax for left outer joins."),
        create_debug_q("Fix the subquery existence operator.",
                       "SELECT * FROM users u WHERE IS_EXIST (SELECT 1 FROM orders WHERE user_id = u.id);",
                       "EXISTS", "SQL operator is EXISTS.", "6 letters.", "EXISTS returns true if the subquery returns any rows."),
        create_debug_q("Fix the operator combining two queries while removing duplicate rows.",
                       "SELECT city FROM customers COMBINE SELECT city FROM suppliers;",
                       "UNION", "Use UNION to merge two queries.", "5 letters.", "UNION combines results of two queries and eliminates duplicates."),
        create_debug_q("Fix the closing keyword for a CASE expression.",
                       "SELECT CASE WHEN score >= 50 THEN 'Pass' ELSE 'Fail' STOP FROM exams;",
                       "END", "CASE expressions terminate with END, not STOP.", "3 letters.", "END terminates a CASE WHEN expression.")
    ]

    sql["Debug the Code"]["Intermediate"]["3"] = [
        create_debug_q("Fix the keyword preserving duplicates when combining sets.",
                       "SELECT id FROM a UNION DUPLICATES SELECT id FROM b;",
                       "UNION ALL", "SQL uses UNION ALL to keep duplicates.", "UNION ALL.", "UNION ALL retains all rows including duplicates."),
        create_debug_q("Fix the table creation keyword for virtual tables.",
                       "CREATE VIRTUAL_TABLE active_users AS SELECT * FROM users;",
                       "CREATE VIEW", "Virtual queries are created with CREATE VIEW.", "CREATE VIEW.", "CREATE VIEW defines stored virtual query tables."),
        create_debug_q("Fix the single-character wildcard in SQL LIKE.",
                       "SELECT * FROM codes WHERE code LIKE 'A*C';",
                       "A_C", "Single character wildcard in SQL is underscore '_', not '*'.", "Use underscore.", "'_' matches exactly one single character in SQL LIKE."),
        create_debug_q("Fix the NOT IN condition with misplaced negation.",
                       "SELECT * FROM items WHERE id IN NOT (SELECT item_id FROM sales);",
                       "NOT IN", "Negation precedes IN: NOT IN.", "NOT IN.", "NOT IN is the correct syntax for negated set membership."),
        create_debug_q("Fix the default fallback keyword in a CASE statement.",
                       "SELECT CASE WHEN val = 1 THEN 'A' DEFAULT 'B' END;",
                       "ELSE 'B'", "SQL CASE uses ELSE, not DEFAULT.", "ELSE.", "ELSE specifies default fallback in a CASE statement.")
    ]

    sql["Debug the Code"]["Intermediate"]["4"] = [
        create_debug_q("Fix the position of ORDER BY in a grouped query.",
                       "SELECT dept, COUNT(*) FROM emp ORDER BY dept GROUP BY dept;",
                       "GROUP BY dept ORDER BY dept", "GROUP BY must come before ORDER BY.", "GROUP BY precedes ORDER BY.", "GROUP BY aggregates rows before ORDER BY sorts the final output."),
        create_debug_q("Fix the string concatenation operator in standard SQL / SQLite.",
                       "SELECT first_name + ' ' + last_name FROM users;",
                       "first_name || ' ' || last_name", "In SQLite and Postgres, string concatenation uses '||'.", "Use double pipe '||'.", "|| is the standard string concatenation operator in SQLite/Postgres."),
        create_debug_q("Fix the aggregate filter: cannot use alias in HAVING in standard SQL.",
                       "SELECT dept, count(*) as cnt FROM emp GROUP BY dept HAVING cnt > 3;",
                       "HAVING count(*) > 3", "Standard SQL requires aggregate expression in HAVING, not column alias.", "HAVING count(*) > 3.", "Standard SQL requires HAVING count(*) > 3 rather than referring to aliases."),
        create_debug_q("Fix the syntax for removing duplicate values inside COUNT.",
                       "SELECT COUNT(UNIQUE email) FROM signups;",
                       "COUNT(DISTINCT email)", "SQL uses DISTINCT inside aggregate functions, not UNIQUE.", "DISTINCT.", "COUNT(DISTINCT col) counts unique non-null values."),
        create_debug_q("Fix the date comparison format in standard ISO-8601.",
                       "SELECT * FROM logs WHERE log_date = '12/31/2023';",
                       "'2023-12-31'", "Standard SQL dates follow YYYY-MM-DD format.", "YYYY-MM-DD.", "Standard SQL date format is 'YYYY-MM-DD'.")
    ]

    # Advanced
    sql["Debug the Code"]["Advanced"]["1"] = [
        create_debug_q("Fix the window function syntax missing OVER keyword.",
                       "SELECT emp_id, ROW_NUMBER(ORDER BY hire_date) FROM employees;",
                       "ROW_NUMBER() OVER (ORDER BY hire_date)", "Window specifications require the OVER keyword.", "Use OVER ().", "Window functions require the OVER (...) clause."),
        create_debug_q("Fix the window partitioning keyword.",
                       "SELECT salary, RANK() OVER (GROUP BY dept_id ORDER BY salary) FROM emp;",
                       "PARTITION BY dept_id", "Window functions use PARTITION BY, not GROUP BY.", "PARTITION BY.", "PARTITION BY defines window partitions inside OVER()."),
        create_debug_q("Fix the function name for accessing prior row data.",
                       "SELECT day, PREVIOUS(amount) OVER (ORDER BY day) FROM sales;",
                       "LAG(amount)", "SQL function is LAG(), not PREVIOUS().", "LAG().", "LAG(col) retrieves values from preceding rows."),
        create_debug_q("Fix the CTE declaration keyword.",
                       "LET RegionalSales AS (SELECT * FROM sales) SELECT * FROM RegionalSales;",
                       "WITH RegionalSales AS", "CTEs begin with WITH, not LET.", "WITH.", "WITH begins a Common Table Expression."),
        create_debug_q("Fix the function returning first non-null argument.",
                       "SELECT FIRST_NON_NULL(email, backup_email) FROM users;",
                       "COALESCE(email, backup_email)", "SQL standard function is COALESCE.", "COALESCE.", "COALESCE() returns the first non-null argument.")
    ]

    sql["Debug the Code"]["Advanced"]["2"] = [
        create_debug_q("Fix recursive CTE declaration missing RECURSIVE keyword.",
                       "WITH Hierarchy(id, parent_id) AS (SELECT id, parent_id FROM nodes) SELECT * FROM Hierarchy;",
                       "WITH RECURSIVE Hierarchy", "Recursive CTEs must specify RECURSIVE.", "WITH RECURSIVE.", "WITH RECURSIVE is required for self-referential CTEs."),
        create_debug_q("Fix the window framing keyword for starting from partition head.",
                       "SUM(amt) OVER (ORDER BY dt ROWS BETWEEN START AND CURRENT ROW)",
                       "UNBOUNDED PRECEDING", "Window boundary keyword is UNBOUNDED PRECEDING.", "UNBOUNDED PRECEDING.", "UNBOUNDED PRECEDING defines the frame starting from the first row of the partition."),
        create_debug_q("Fix the transaction rollback command.",
                       "REVERT TRANSACTION;",
                       "ROLLBACK;", "SQL uses ROLLBACK, not REVERT.", "ROLLBACK.", "ROLLBACK cancels uncommitted changes within a transaction."),
        create_debug_q("Fix the command checking execution plan in SQLite.",
                       "SHOW PLAN SELECT * FROM users;",
                       "EXPLAIN QUERY PLAN", "SQLite uses EXPLAIN QUERY PLAN.", "EXPLAIN QUERY PLAN.", "EXPLAIN QUERY PLAN displays index and table scan details."),
        create_debug_q("Fix the function segmenting rows into percentiles/quartiles.",
                       "SELECT BUCKET(4) OVER (ORDER BY score) FROM tests;",
                       "NTILE(4)", "SQL function is NTILE(n).", "NTILE.", "NTILE(n) divides the partition into n ranked buckets.")
    ]

    sql["Debug the Code"]["Advanced"]["3"] = [
        create_debug_q("Fix the constraint name keyword in ALTER TABLE.",
                       "ALTER TABLE users ADD RULE chk_age CHECK (age >= 18);",
                       "ADD CONSTRAINT chk_age", "Use ADD CONSTRAINT, not ADD RULE.", "ADD CONSTRAINT.", "ADD CONSTRAINT specifies named database constraints."),
        create_debug_q("Fix foreign key deletion cascade syntax.",
                       "FOREIGN KEY (user_id) REFERENCES users(id) ON REMOVE CASCADE;",
                       "ON DELETE CASCADE", "SQL uses ON DELETE CASCADE, not ON REMOVE.", "ON DELETE CASCADE.", "ON DELETE CASCADE removes dependent child rows."),
        create_debug_q("Fix transaction initiation syntax.",
                       "START_TRANSACTION;",
                       "BEGIN TRANSACTION;", "Standard SQL starts transactions with BEGIN TRANSACTION.", "BEGIN TRANSACTION.", "BEGIN TRANSACTION initiates an atomic transaction block."),
        create_debug_q("Fix index creation on multiple columns.",
                       "CREATE INDEX idx_user ON orders (user_id AND order_date);",
                       "(user_id, order_date)", "Multiple index columns are separated by commas, not AND.", "Comma-separated columns.", "Composite indexes use comma-separated column lists: (col1, col2)."),
        create_debug_q("Fix unique index creation command.",
                       "CREATE DISTINCT INDEX idx_email ON users(email);",
                       "CREATE UNIQUE INDEX", "SQL uses CREATE UNIQUE INDEX, not DISTINCT.", "CREATE UNIQUE INDEX.", "CREATE UNIQUE INDEX enforces column uniqueness.")
    ]

    sql["Debug the Code"]["Advanced"]["4"] = [
        create_debug_q("Fix window ranking function typo.",
                       "SELECT DENSE_RANKING() OVER (ORDER BY points DESC) FROM players;",
                       "DENSE_RANK()", "Function is DENSE_RANK(), not DENSE_RANKING().", "DENSE_RANK().", "DENSE_RANK() assigns contiguous ranks."),
        create_debug_q("Fix subquery alias requirement in FROM clause.",
                       "SELECT total FROM (SELECT sum(amt) as total FROM orders);",
                       "(SELECT sum(amt) as total FROM orders) AS sub", "Subqueries in FROM clause require an alias in standard SQL.", "Provide alias AS sub.", "Derived tables in FROM must have an alias in standard SQL."),
        create_debug_q("Fix gapless cumulative window framing.",
                       "AVG(rev) OVER (ORDER BY dt ROWS 6 PRECEDING)",
                       "ROWS BETWEEN 6 PRECEDING AND CURRENT ROW", "Frame specification requires BETWEEN ... AND ...", "BETWEEN 6 PRECEDING AND CURRENT ROW.", "ROWS BETWEEN 6 PRECEDING AND CURRENT ROW frames the rolling 7-day window."),
        create_debug_q("Fix drop constraint syntax.",
                       "ALTER TABLE products DELETE CONSTRAINT chk_price;",
                       "DROP CONSTRAINT chk_price", "SQL uses DROP CONSTRAINT, not DELETE.", "DROP CONSTRAINT.", "DROP CONSTRAINT removes constraints in ALTER TABLE."),
        create_debug_q("Fix transaction savepoint release command.",
                       "COMMIT SAVEPOINT sp1;",
                       "RELEASE SAVEPOINT sp1;", "Savepoints are discarded/persisted with RELEASE SAVEPOINT.", "RELEASE SAVEPOINT.", "RELEASE SAVEPOINT sp1 releases the specified savepoint.")
    ]

    # =========================================================================
    # 5. PREDICT THE OUTPUT (predict)
    # =========================================================================
    # Beginner
    sql["Predict the Output"]["Beginner"]["1"] = [
        create_predict_q("Given table 'users' with 4 rows where ages are (15, 20, 25, 30), predict the output count:",
                         "SELECT COUNT(*) FROM users WHERE age >= 20;",
                         "3", "Count rows where age is 20 or higher.", "20, 25, and 30 qualify.", "3 rows meet the age >= 20 condition."),
        create_predict_q("Given table 'items' with prices (10, 20, 30), predict the output:",
                         "SELECT SUM(price) FROM items;",
                         "60", "Add 10 + 20 + 30.", "Total arithmetic sum.", "10 + 20 + 30 = 60."),
        create_predict_q("Given table 'products' with values ('Apple', 'Banana', 'Apple'), predict distinct count:",
                         "SELECT COUNT(DISTINCT name) FROM products;",
                         "2", "Deduplicate 'Apple'.", "Only Apple and Banana remain.", "There are 2 distinct product names: Apple and Banana."),
        create_predict_q("Given scores (80, 90, 100), predict the average:",
                         "SELECT AVG(score) FROM tests;",
                         "90", "(80 + 90 + 100) / 3.", "Mean score.", "Average is 270 / 3 = 90."),
        create_predict_q("Given numbers (5, 12, 3, 19, 7), predict MIN(num):",
                         "SELECT MIN(num) FROM data;",
                         "3", "Lowest number in the list.", "Single digit.", "3 is the smallest number.")
    ]

    sql["Predict the Output"]["Beginner"]["2"] = [
        create_predict_q("Given numbers (10, 25, 5, 40), predict MAX(val):",
                         "SELECT MAX(val) FROM numbers;",
                         "40", "Highest number in the list.", "Two digits.", "40 is the greatest value."),
        create_predict_q("Given rows with status ('active', 'pending', 'active', 'active'), predict count of active:",
                         "SELECT COUNT(*) FROM accounts WHERE status = 'active';",
                         "3", "Count matching 'active'.", "3 out of 4 rows.", "3 rows have status = 'active'."),
        create_predict_q("Given 10 rows in table 'logs', predict the number of rows returned by:",
                         "SELECT * FROM logs LIMIT 4;",
                         "4", "LIMIT restricts the output row count.", "Specified limit number.", "LIMIT 4 caps the returned rows at 4."),
        create_predict_q("Given prices (15, 25, 35), predict the result of:",
                         "SELECT COUNT(*) FROM products WHERE price BETWEEN 20 AND 30;",
                         "1", "Only 25 falls between 20 and 30 inclusive.", "Single row.", "Only 25 is within [20, 30]."),
        create_predict_q("Predict output for evaluating boolean comparison in SQL:",
                         "SELECT 10 > 5;",
                         "1", "In SQLite, TRUE is represented as 1.", "Single digit 1.", "10 > 5 evaluates to boolean TRUE (1).")
    ]

    sql["Predict the Output"]["Beginner"]["3"] = [
        create_predict_q("Given values (NULL, 10, 20), predict the output of COUNT(val):",
                         "SELECT COUNT(val) FROM t;",
                         "2", "COUNT(col) ignores NULL values.", "Counts only non-nulls.", "COUNT(val) skips the NULL value and counts 2."),
        create_predict_q("Given values (NULL, 10, 20), predict the output of COUNT(*):",
                         "SELECT COUNT(*) FROM t;",
                         "3", "COUNT(*) counts all rows regardless of NULLs.", "3 total rows.", "COUNT(*) counts total rows including rows with NULLs."),
        create_predict_q("Given table with 0 rows, predict the output of COUNT(*):",
                         "SELECT COUNT(*) FROM empty_table;",
                         "0", "No rows exist.", "Zero.", "COUNT(*) on an empty table returns 0."),
        create_predict_q("Given values (5, 5, 5), predict SUM(val):",
                         "SELECT SUM(val) FROM items;",
                         "15", "5 + 5 + 5.", "Sum of three fives.", "5 + 5 + 5 = 15."),
        create_predict_q("Predict the result of integer division: 15 / 4 in standard SQLite integer mode:",
                         "SELECT 15 / 4;",
                         "3", "Integer division truncates decimals in SQLite.", "15 // 4 = 3.", "15 / 4 evaluates to integer 3.")
    ]

    sql["Predict the Output"]["Beginner"]["4"] = [
        create_predict_q("Given names ('Alice', 'Bob', 'Charlie'), predict output of:",
                         "SELECT COUNT(*) FROM users WHERE name LIKE 'A%';",
                         "1", "Only Alice starts with 'A'.", "Single match.", "Only 'Alice' matches 'A%'."),
        create_predict_q("Predict output of length function: LENGTH('CodeQuest')",
                         "SELECT LENGTH('CodeQuest');",
                         "9", "Count characters in 'CodeQuest'.", "9 letters.", "'CodeQuest' has 9 characters."),
        create_predict_q("Predict output of LOWER('SQL'):",
                         "SELECT LOWER('SQL');",
                         "sql", "Converts to lowercase.", "Lowercase letters.", "LOWER('SQL') returns 'sql'."),
        create_predict_q("Predict output of UPPER('data'):",
                         "SELECT UPPER('data');",
                         "DATA", "Converts to uppercase.", "Capital letters.", "UPPER('data') returns 'DATA'."),
        create_predict_q("Given ages (16, 18, 22), predict COUNT(*) WHERE age >= 18 AND age < 22:",
                         "SELECT COUNT(*) FROM users WHERE age >= 18 AND age < 22;",
                         "1", "Only 18 satisfies both conditions (22 is excluded by <).", "Single row.", "Only age 18 qualifies.")
    ]

    # Intermediate
    sql["Predict the Output"]["Intermediate"]["1"] = [
        create_predict_q("Given employees in Dept 1: (salary 10, 20) and Dept 2: (salary 30), predict count of depts with SUM(salary) >= 30:",
                         "SELECT dept, SUM(salary) FROM emp GROUP BY dept HAVING SUM(salary) >= 30;",
                         "2", "Dept 1 sum is 30; Dept 2 sum is 30. Both qualify.", "Both departments meet threshold.", "Both departments have sum >= 30, so 2 rows are returned."),
        create_predict_q("Given table A with IDs (1, 2) and table B with IDs (2, 3), how many rows returned by INNER JOIN ON A.id = B.id?",
                         "SELECT * FROM A INNER JOIN B ON A.id = B.id;",
                         "1", "Only ID 2 matches in both tables.", "Single matching ID.", "Only ID 2 matches, producing 1 row."),
        create_predict_q("Given table A with IDs (1, 2) and table B with ID (2), how many rows returned by A LEFT JOIN B ON A.id = B.id?",
                         "SELECT * FROM A LEFT JOIN B ON A.id = B.id;",
                         "2", "LEFT JOIN returns all rows from table A.", "Table A has 2 rows.", "LEFT JOIN preserves both rows of A, yielding 2 rows."),
        create_predict_q("Predict output of COALESCE(NULL, NULL, 'Found', 'Extra'):",
                         "SELECT COALESCE(NULL, NULL, 'Found', 'Extra');",
                         "Found", "First non-null value.", "Returns 'Found'.", "COALESCE returns the first non-null argument 'Found'."),
        create_predict_q("Predict output of CASE expression:",
                         "SELECT CASE WHEN 10 > 20 THEN 'No' WHEN 5 = 5 THEN 'Yes' ELSE 'Maybe' END;",
                         "Yes", "Second branch evaluates to TRUE.", "Returns 'Yes'.", "5 = 5 is TRUE, so 'Yes' is returned.")
    ]

    sql["Predict the Output"]["Intermediate"]["2"] = [
        create_predict_q("Given table with 3 rows, predict row count of UNION ALL between table and itself:",
                         "SELECT id FROM t UNION ALL SELECT id FROM t;",
                         "6", "3 rows + 3 rows without deduplication.", "3 + 3 = 6.", "UNION ALL preserves all duplicates: 3 + 3 = 6 rows."),
        create_predict_q("Given table with IDs (1, 2, 2, 3), predict row count of: SELECT DISTINCT id FROM t UNION SELECT id FROM t;",
                         "SELECT id FROM t UNION SELECT id FROM t;",
                         "3", "UNION deduplicates to unique IDs: 1, 2, 3.", "Unique count.", "UNION eliminates duplicates, leaving 3 distinct rows."),
        create_predict_q("Given string 'Database', predict output of SUBSTR('Database', 1, 4):",
                         "SELECT SUBSTR('Database', 1, 4);",
                         "Data", "First 4 characters starting at position 1.", "4 letters.", "SUBSTR('Database', 1, 4) returns 'Data'."),
        create_predict_q("Given table with 5 rows and table B with 4 rows, how many rows does CROSS JOIN produce?",
                         "SELECT * FROM A CROSS JOIN B;",
                         "20", "Cartesian product: 5 * 4.", "5 multiplied by 4.", "5 * 4 = 20 rows."),
        create_predict_q("Given values (10, 20, 30), predict the output of: SELECT COUNT(*) FROM t WHERE id IN (SELECT id FROM t WHERE id > 15);",
                         "SELECT COUNT(*) FROM t WHERE id IN (SELECT id FROM t WHERE id > 15);",
                         "2", "Subquery returns 20 and 30.", "2 matching rows.", "IDs 20 and 30 match, resulting in 2 rows.")
    ]

    sql["Predict the Output"]["Intermediate"]["3"] = [
        create_predict_q("Predict output of TRIM('   SQL   '):",
                         "SELECT TRIM('   SQL   ');",
                         "SQL", "Strips whitespace padding.", "3 capital letters.", "TRIM removes leading and trailing spaces."),
        create_predict_q("Given scores (50, 70, 90), predict count of: WHERE score NOT BETWEEN 60 AND 80;",
                         "SELECT COUNT(*) FROM tests WHERE score NOT BETWEEN 60 AND 80;",
                         "2", "50 and 90 fall outside [60, 80].", "Two scores qualify.", "50 and 90 are not between 60 and 80, so 2 rows match."),
        create_predict_q("Predict output of: SELECT COALESCE(NULL, 42);",
                         "SELECT COALESCE(NULL, 42);",
                         "42", "First non-null is 42.", "Number 42.", "COALESCE returns 42."),
        create_predict_q("Given departments with employee counts (1, 4, 7), how many rows returned by: GROUP BY dept HAVING count(*) > 2?",
                         "SELECT dept FROM emp GROUP BY dept HAVING count(*) > 2;",
                         "2", "Departments with 4 and 7 employees qualify.", "Two departments.", "4 and 7 are > 2, so 2 groups are returned."),
        create_predict_q("Predict boolean result in SQLite: SELECT 1 IS NULL;",
                         "SELECT 1 IS NULL;",
                         "0", "1 is not NULL, so IS NULL evaluates to FALSE (0).", "Zero.", "1 IS NULL evaluates to 0 (FALSE).")
    ]

    sql["Predict the Output"]["Intermediate"]["4"] = [
        create_predict_q("Given table with 2 active and 3 inactive rows, predict output of: SELECT SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) FROM t;",
                         "SELECT SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) FROM t;",
                         "2", "Each active row adds 1; inactive adds 0.", "Total is 2.", "Sum of active indicators equals 2."),
        create_predict_q("Predict output of ABS(-99):",
                         "SELECT ABS(-99);",
                         "99", "Absolute value removes sign.", "Positive 99.", "ABS(-99) returns 99."),
        create_predict_q("Predict output of ROUND(3.14159, 2):",
                         "SELECT ROUND(3.14159, 2);",
                         "3.14", "Rounds to two decimal places.", "3.14.", "ROUND(3.14159, 2) returns 3.14."),
        create_predict_q("Given orders with amounts (50, 150, 250), predict count of: WHERE amount > 100 OR id = 1 (where order 1 amount is 50):",
                         "SELECT COUNT(*) FROM orders WHERE amount > 100 OR id = 1;",
                         "3", "All three orders qualify.", "3 rows.", "All 3 rows satisfy the OR condition."),
        create_predict_q("Predict result of: SELECT INSTR('CodeQuest', 'Quest');",
                         "SELECT INSTR('CodeQuest', 'Quest');",
                         "5", "1-based index where 'Quest' begins.", "Starts at position 5.", "In SQLite, INSTR is 1-indexed, starting at 5.")
    ]

    # Advanced
    sql["Predict the Output"]["Advanced"]["1"] = [
        create_predict_q("Given salaries (100, 200, 300), predict the highest ROW_NUMBER() assigned by: ROW_NUMBER() OVER (ORDER BY salary)",
                         "SELECT MAX(rn) FROM (SELECT ROW_NUMBER() OVER (ORDER BY salary) as rn FROM emp);",
                         "3", "Total of 3 sequential rows.", "3.", "Row numbers are 1, 2, 3; maximum is 3."),
        create_predict_q("Given values (10, 20, 20, 30), what is DENSE_RANK() for value 30 ordered ascending?",
                         "SELECT DENSE_RANK() OVER (ORDER BY val ASC) FROM t WHERE val = 30;",
                         "3", "Ranks are 10 -> 1, 20 -> 2, 30 -> 3 (no gaps).", "Rank 3.", "DENSE_RANK leaves no gaps: 10(1), 20(2), 20(2), 30(3)."),
        create_predict_q("Given values (10, 20, 20, 30), what is RANK() for value 30 ordered ascending?",
                         "SELECT RANK() OVER (ORDER BY val ASC) FROM t WHERE val = 30;",
                         "4", "Ranks are 10 -> 1, 20 -> 2, 20 -> 2, 30 -> 4 (skips 3).", "Rank 4.", "RANK skips rank 3 after tie: 10(1), 20(2), 20(2), 30(4)."),
        create_predict_q("Given revenue on days 1, 2, 3 as (10, 20, 30), predict running total on day 3:",
                         "SELECT SUM(rev) OVER (ORDER BY day) FROM sales WHERE day = 3;",
                         "60", "10 + 20 + 30 = 60.", "Cumulative sum.", "Running sum on day 3 is 10 + 20 + 30 = 60."),
        create_predict_q("Given daily values (100, 200), predict LAG(val, 1) for the first row (day 1):",
                         "SELECT LAG(val, 1) OVER (ORDER BY day) FROM sales LIMIT 1;",
                         "NULL", "There is no preceding row for the first entry.", "Returns NULL.", "The first row has no preceding record, yielding NULL.")
    ]

    sql["Predict the Output"]["Advanced"]["2"] = [
        create_predict_q("Given CTE generating numbers 1 to 3, predict SUM(n):",
                         "WITH RECURSIVE nums(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM nums WHERE n < 3) SELECT SUM(n) FROM nums;",
                         "6", "1 + 2 + 3 = 6.", "Sum of numbers.", "1 + 2 + 3 = 6."),
        create_predict_q("Given 8 rows, into how many buckets does NTILE(4) partition the rows?",
                         "SELECT COUNT(DISTINCT bucket) FROM (SELECT NTILE(4) OVER (ORDER BY id) as bucket FROM t);",
                         "4", "NTILE(4) creates 4 buckets.", "4 quartiles.", "NTILE(4) creates 4 distinct bucket numbers (1, 2, 3, 4)."),
        create_predict_q("Given CTE returning 5 rows, how many rows returned by outer query: SELECT * FROM MyCTE WHERE id > 2?",
                         "WITH MyCTE AS (SELECT id FROM items WHERE id <= 5) SELECT COUNT(*) FROM MyCTE WHERE id > 2;",
                         "3", "IDs 3, 4, 5 qualify.", "3 rows.", "3 rows (3, 4, 5) satisfy the condition."),
        create_predict_q("Predict output of COALESCE(NULL, COALESCE(NULL, 100)):",
                         "SELECT COALESCE(NULL, COALESCE(NULL, 100));",
                         "100", "Innermost returns 100; outer returns 100.", "100.", "Nested COALESCE evaluates to 100."),
        create_predict_q("Given table with 4 rows where all rows have identical score 50, predict DENSE_RANK() for all rows:",
                         "SELECT DISTINCT DENSE_RANK() OVER (ORDER BY score) FROM t;",
                         "1", "All tied at rank 1.", "Rank 1.", "All identical values receive rank 1.")
    ]

    sql["Predict the Output"]["Advanced"]["3"] = [
        create_predict_q("Predict row count after executing: BEGIN; INSERT INTO t VALUES (1); ROLLBACK; SELECT COUNT(*) FROM t (initially empty):",
                         "SELECT COUNT(*) FROM t;",
                         "0", "ROLLBACK cancels the inserted row.", "0 rows.", "ROLLBACK reverts the insert, leaving 0 rows."),
        create_predict_q("Predict row count after executing: BEGIN; INSERT INTO t VALUES (1); COMMIT; SELECT COUNT(*) FROM t (initially empty):",
                         "SELECT COUNT(*) FROM t;",
                         "1", "COMMIT persists the inserted row.", "1 row.", "COMMIT permanently saves the row, so count is 1."),
        create_predict_q("Given CTE counting active users (say 5), predict output of: WITH A AS (SELECT 5 as c) SELECT c * 2 FROM A;",
                         "WITH A AS (SELECT 5 as c) SELECT c * 2 FROM A;",
                         "10", "5 * 2 = 10.", "10.", "5 * 2 evaluates to 10."),
        create_predict_q("Predict output of: SELECT CASE WHEN EXISTS (SELECT 1 WHERE 1=0) THEN 'Yes' ELSE 'No' END;",
                         "SELECT CASE WHEN EXISTS (SELECT 1 WHERE 1=0) THEN 'Yes' ELSE 'No' END;",
                         "No", "Subquery returns no rows, so EXISTS is FALSE.", "Returns 'No'.", "EXISTS on empty set is FALSE, selecting 'No'."),
        create_predict_q("Predict output of: SELECT CASE WHEN NOT EXISTS (SELECT 1 WHERE 1=0) THEN 'Pass' ELSE 'Fail' END;",
                         "SELECT CASE WHEN NOT EXISTS (SELECT 1 WHERE 1=0) THEN 'Pass' ELSE 'Fail' END;",
                         "Pass", "NOT EXISTS on empty set is TRUE.", "Returns 'Pass'.", "NOT EXISTS evaluates to TRUE, selecting 'Pass'.")
    ]

    sql["Predict the Output"]["Advanced"]["4"] = [
        create_predict_q("Given sequence (10, 20, 30), predict LEAD(val, 1) for the last row:",
                         "SELECT LEAD(val, 1) OVER (ORDER BY val) FROM t ORDER BY val DESC LIMIT 1;",
                         "NULL", "The last row has no following record.", "Returns NULL.", "The last row has no following value, so LEAD returns NULL."),
        create_predict_q("Predict output of: SELECT COALESCE(NULL, NULL, NULL, 0);",
                         "SELECT COALESCE(NULL, NULL, NULL, 0);",
                         "0", "0 is non-null.", "Zero.", "0 is non-null, so COALESCE returns 0."),
        create_predict_q("Given 3 rows with values (1, 2, 3), predict the average rank: (1 + 2 + 3) / 3:",
                         "SELECT AVG(r) FROM (SELECT ROW_NUMBER() OVER (ORDER BY id) as r FROM t);",
                         "2", "(1 + 2 + 3) / 3 = 2.", "Mean rank is 2.", "Average of 1, 2, 3 is 2."),
        create_predict_q("Predict output of string concatenation: SELECT 'SQL' || '_' || '2024';",
                         "SELECT 'SQL' || '_' || '2024';",
                         "SQL_2024", "Concatenates strings with double pipe.", "SQL_2024.", "'SQL' || '_' || '2024' produces 'SQL_2024'."),
        create_predict_q("Predict output of modular arithmetic: SELECT 20 % 6;",
                         "SELECT 20 % 6;",
                         "2", "Remainder of 20 divided by 6 (6*3 = 18, rem 2).", "Remainder 2.", "20 % 6 = 2.")
    ]

    return sql
