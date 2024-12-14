-- Create tables
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    is_active BOOLEAN
);

CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY,
    date DATE,
    user_id UUID REFERENCES users(user_id),
    is_blocked BOOLEAN,
    transaction_amount INTEGER,
    transaction_category_id INTEGER
);

-- Load sample data into users table (replace with CSV loading logic if needed)
COPY users(user_id, is_active)
FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;

-- Load sample data into transactions table (replace with CSV loading logic if needed)
COPY transactions(transaction_id, date, user_id, is_blocked, transaction_amount, transaction_category_id)
FROM '/docker-entrypoint-initdb.d/transactions.csv' DELIMITER ',' CSV HEADER;
