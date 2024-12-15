WITH transaction_features AS (
    SELECT 
        t1.transaction_id,
        t1.user_id,
        t1.date,
        COUNT(t2.transaction_id) AS transactions_within_7_days
    FROM 
        transactions t1
    LEFT JOIN 
        transactions t2
        ON t1.user_id = t2.user_id 
        AND t2.date < t1.date
        AND t2.date >= t1.date - INTERVAL '7 days'
    GROUP BY 
        t1.transaction_id, t1.user_id, t1.date
)
SELECT * FROM transaction_features
ORDER BY user_id, date;



