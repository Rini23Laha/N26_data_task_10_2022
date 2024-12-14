CREATE TABLE transactions (
transaction_id UUID,
date DATE,
user_id UUID,
is_blocked BOOL,
transaction_amount INTEGER,
transaction_category_id INTEGER
);

--take few examples of data from transaction csv
INSERT INTO transactions (transaction_id, date, user_id, is_blocked, transaction_amount, transaction_category_id) VALUES
('022a1063-0b82-4c8f-8d5a-f05788f46b1e', '2024-09-19', 'c3cfd3f6-c170-4842-a0bc-c017f5c587bb', FALSE, 67.92, 6),
('7d6e0e20-3d83-416c-99d5-7a02387dc513', '2024-10-13', '05e252f9-cd7e-4b1c-978a-58aef7b0bdbb', TRUE, 88.77, 7),
('7f586ac6-e8a6-4403-bbbd-2a21ecf1ce03', '2024-10-06', '36fa0ed3-8e04-415c-a662-4f2cb83b2a9a', TRUE, 84.98, 3),
('d11d80d4-7017-4fd9-9994-6db02638c8af', '2024-09-26', 'bab91d75-80f7-4b4c-8f84-463196120b1d', TRUE, 94.45, 5),
('5d8c50aa-c1cc-4129-a09b-058c0176cf11', '2024-11-14', '433bee14-ebf4-4116-89f1-cfc10d0eb059', TRUE, 74.95, 3),
('4a2f40fd-b770-41a0-aace-2b0fc737fb7b', '2024-09-11', '20a57c91-55d2-46e7-be16-14b4408b3f8c', FALSE, 81.95, 4);

CREATE TABLE users (
user_id UUID,
is_active BOOLEAN
);

-- take examples of data from users

INSERT INTO users (user_id, is_active) values
('c3cfd3f6-c170-4842-a0bc-c017f5c587bb',True),
('05e252f9-cd7e-4b1c-978a-58aef7b0bdbb',True),
('36fa0ed3-8e04-415c-a662-4f2cb83b2a9a',True),
('bab91d75-80f7-4b4c-8f84-463196120b1d',True),
('433bee14-ebf4-4116-89f1-cfc10d0eb059',True),
('20a57c91-55d2-46e7-be16-14b4408b3f8c',true);


-- Query to execute--

SELECT
    t.transaction_category_id,
    SUM(t.transaction_amount) AS sum_amount,
    COUNT(DISTINCT t.user_id) AS num_users
FROM transactions t
JOIN users u USING (user_id)
WHERE t.is_blocked = FALSE
AND u.is_active = TRUE  -- Use TRUE instead of 1
GROUP BY t.transaction_category_id
ORDER BY sum_amount DESC;