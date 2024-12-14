-- Create users table
CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY,
    is_active BOOLEAN
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id UUID PRIMARY KEY,
    date DATE,
    user_id UUID REFERENCES users(user_id),
    is_blocked BOOLEAN,
    transaction_amount INTEGER,
    transaction_category_id INTEGER
);

-- Load users data into users table using \copy, and cast values
\copy users(user_id, is_active) FROM '/mnt/data/users.csv' DELIMITER ',' CSV HEADER;

-- Update the users table to convert 'True'/'False' to boolean
UPDATE users
SET is_active = CASE 
                    WHEN is_active = 'True' THEN true
                    WHEN is_active = 'False' THEN 
                    ELSE NULL
                END;

-- Load transactions data into transactions table
\copy transactions(transaction_id, date, user_id, is_blocked, transaction_amount, transaction_category_id)
FROM '/mnt/data/transactions.csv' DELIMITER ',' CSV HEADER;
