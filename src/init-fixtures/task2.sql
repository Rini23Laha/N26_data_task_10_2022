CREATE TABLE transactions (
transaction_id UUID,
date DATE,
user_id UUID,
is_blocked BOOL,
transaction_amount INTEGER,
transaction_category_id INTEGER
);

INSERT INTO transactions VALUES 
('ef05-4247','becf-457e',2020-01-01,0),
('c8d1-40ca','becf-457e',2020-01-05 1)
;


CREATE TABLE users (
user_id UUID,
is_active BOOLEAN
);