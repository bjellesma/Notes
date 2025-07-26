# Supported Function Types

## Scalar Functions

These are data generation functions like `Date()` or  `UUID_STRING()` that return one value.

## Aggregate Functions

operate on values across rows to perform mathematical calculations like `SUM()` or `MAX()`

## Window Functions

a subset of aggregate functions allowing us to aggregate one on a subset of rows this is done using the `over` syntax with the aggregate. 

```sql
select account_id, max(amount) over (partition by account_id) from account
```

will give us the max for each account id

## Table Functions

return a set of rows for each input row. The returned set can contain zero, one, or mor rows. Each row can contain one or more columns.

```sql
select randstr(5, RANDOM()), RANDOM() FROM TABLE(GENERATOR(ROWCOUNT => 3)):
```

The above query creates a table of 3 rows whereas the first col is random string of 5 chars and the second column is random data

<img width="1828" height="415" alt="image" src="https://github.com/user-attachments/assets/e38b087f-47b5-42b0-a48c-360d93d83e6e" />

## System Functions

This is a built in function that uses the $ syntax

```sql
select system$pipe_status('my_pipe`);
```

```sql
select system$explain_plan_json('SELECT * FROM FILMS_DB.FILMS_SCHEMA.FILMS')
```

<img width="1864" height="438" alt="image" src="https://github.com/user-attachments/assets/575e5925-95e1-4646-b463-5f0759e76afc" />
