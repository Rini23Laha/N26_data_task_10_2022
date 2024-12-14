-- Create users and transactions tables
CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY,
    is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    transaction_amount DECIMAL,
    transaction_category_id INT,
    date DATE
);

-- Load users data from CSV
COPY users(user_id, is_active)
FROM '/app/users.csv'
DELIMITER ','
CSV HEADER;

-- Load transactions data from CSV
COPY transactions(transaction_id, user_id, transaction_amount, transaction_category_id, date)
FROM '/app/transactions.csv'
DELIMITER ','
CSV HEADER;
