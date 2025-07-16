## Query Performance Analysis Tools

In the snowsight UI, you can use the query history tab to get detailed information about the steps that were performed in the query. In the following query, you can see that 99.3% of the time was spent just scanning the table so we can infer that using a limit really doesn't have any effect.

SELECT C_CUSTKEY, C_NAME, C_ADDRESS, C_ACCTBAL FROM CUSTOMER 
ORDER BY C_ACCTBAL DESC
LIMIT 10000;

<img width="2454" height="833" alt="image" src="https://github.com/user-attachments/assets/9a6a6efa-3196-4a6f-8322-f592a59c55d2" />
