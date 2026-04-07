import random

# Pools of tables, columns, values, dates
tables = ["employees", "departments", "orders", "sales", "customers", "products", "inventory", "suppliers"]
columns = ["id", "name", "salary", "dept_id", "order_id", "customer_id", "product_id", "quantity", "order_date", "status"]
values = ["1000", "50000", "200", "300", "400", "600", "'completed'", "'pending'", "'active'"]
dates = ["2025-01-01", "2025-12-31", "2026-01-01", "2026-12-31"]

# Query templates
queries = [
    "SELECT {col} FROM {table} WHERE {col} > {val};",
    "SELECT {col1}, {col2} FROM {table1} JOIN {table2} ON {table1}.{col3} = {table2}.{col3};",
    "SELECT COUNT(*) FROM {table} WHERE {col} BETWEEN '{date1}' AND '{date2}';",
    "SELECT {col}, SUM({col2}) FROM {table} GROUP BY {col} ORDER BY SUM({col2}) DESC;",
    "SELECT {col1}, {col2} FROM {table1} LEFT JOIN {table2} ON {table1}.{col3} = {table2}.{col3};",
    "INSERT INTO {table} ({col1}, {col2}) VALUES ({val1}, {val2});",
    "UPDATE {table} SET {col} = {val} WHERE {col2} = {val2};",
    "DELETE FROM {table} WHERE {col} < {val};",
    "SELECT {col1}, AVG({col2}) FROM {table} WHERE {col3} IN (SELECT {col} FROM {table2} WHERE {col2} = {val}) GROUP BY {col1};",
    "SELECT {col1}, {col2}, ROW_NUMBER() OVER (PARTITION BY {col3} ORDER BY {col2}) FROM {table};"
]

# Rules
rules = [
    "Apply filters early to reduce intermediate results.",
    "Use EXISTS instead of IN for correlated subqueries.",
    "Avoid SELECT *; specify only required columns.",
    "Use LIMIT to restrict result size.",
    "Push down predicates into JOIN conditions.",
    "Prefer indexed columns in WHERE and JOIN clauses.",
    "Aggregate after filtering, not before.",
    "Replace nested subqueries with JOINs when possible.",
    "Use window functions instead of multiple subqueries.",
    "Cache results of expensive queries if reused frequently."
]

# Explanations
explanations = [
    "This query demonstrates selection with filtering.",
    "This query demonstrates join operations.",
    "This query demonstrates aggregation with date range filtering.",
    "This query demonstrates grouping and ordering.",
    "This query demonstrates left join operations.",
    "This query demonstrates memory-efficient existence checking.",
    "This query demonstrates computation-efficient limiting.",
    "This query demonstrates efficient subquery filtering.",
    "This query demonstrates use of window functions.",
    "This query demonstrates insert/update/delete operations."
]

def generate_entry(i):
    q = random.choice(queries).format(
        table=random.choice(tables),
        table1=random.choice(tables),
        table2=random.choice(tables),
        col=random.choice(columns),
        col1=random.choice(columns),
        col2=random.choice(columns),
        col3=random.choice(columns),
        val=random.choice(values),
        val1=random.choice(values),
        val2=random.choice(values),
        date1=random.choice(dates),
        date2=random.choice(dates)
    )
    rule = random.choice(rules)
    explanation = random.choice(explanations)
    prompt = f"Prompt {i}: Generate an SQL query for {random.choice(['filtering', 'joining', 'aggregation', 'efficient query writing'])}"
    return f"-- ENTRY {i} --\n{prompt}\nQuery: {q}\nRule: {rule}\nExplanation: {explanation}\n\n"

# Write 500k entries
with open("synthetic_sql_optimizer_dataset2.txt", "w") as f:
    for i in range(1, 500001):
        f.write(generate_entry(i))

print("Dataset generated: synthetic_sql_optimizer_dataset.txt with 500,000 entries")