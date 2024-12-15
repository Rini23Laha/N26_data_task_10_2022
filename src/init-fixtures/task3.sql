CREATE TABLE dim_dep_agreement (
    sk SERIAL PRIMARY KEY,
    agrmnt_id INT,
    actual_from_dt DATE,
    actual_to_dt DATE,
    client_id INT,
    product_id INT,
    interest_rate NUMERIC(5, 2)
);


INSERT INTO dim_dep_agreement (agrmnt_id, actual_from_dt, actual_to_dt, client_id, product_id, interest_rate)
VALUES
    (101, '2015-01-01', '2015-02-20', 20, 305, 3.5),
    (101, '2015-02-21', '2015-05-17', 20, 345, 4.0),
    (101, '2015-05-18', '2015-07-05', 20, 345, 4.0),
    (101, '2015-07-06', '2015-08-22', 20, 539, 6.0),
    (101, '2015-08-23', '9999-12-31', 20, 345, 4.0),
    (102, '2016-01-01', '2016-06-30', 25, 333, 3.7),
    (102, '2016-07-01', '2016-07-25', 25, 333, 3.7),
    (102, '2016-07-26', '2016-09-15', 25, 333, 3.7),
    (102, '2016-09-16', '9999-12-31', 25, 560, 5.9),
    (103, '2011-05-22', '9999-12-31', 30, 560, 2.0);