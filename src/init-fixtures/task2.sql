CREATE TABLE transactions (
    transaction_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    date DATE
);

INSERT INTO transactions (transaction_id, user_id, date) VALUES
('ef05-4247', 'becf-457e', '2020-01-01'),
('c8d1-40ca', 'becf-457e', '2020-01-05'),
('fc2b-4b36', 'becf-457e', '2020-01-07'),
('3725-48c4', 'becf-457e', '2020-01-15'),
('5f2a-47c2', 'becf-457e', '2020-01-16'),
('7541-412c', '5728-4f1c', '2020-01-01'),
('3deb-47d7', '5728-4f1c', '2020-01-12');
