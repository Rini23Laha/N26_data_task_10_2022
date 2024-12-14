CREATE TABLE transactions (
transaction_id UUID,
date DATE,
user_id UUID,
is_blocked BOOL,
transaction_amount INTEGER,
transaction_category_id INTEGER
);


CREATE TABLE users (
user_id UUID,
is_active BOOLEAN
);