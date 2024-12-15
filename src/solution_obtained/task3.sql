CREATE TABLE dim_dep_agreement_compacted AS
WITH merged_data AS (
    -- Select from dim_dep_agreement to collapse redundant rows
    SELECT 
        agrmnt_id,
        MIN(actual_from_dt) AS actual_from_dt,
        MAX(actual_to_dt) AS actual_to_dt,
        client_id,
        product_id,
        interest_rate
    FROM (
        -- Self-join to group consecutive rows where the attributes are the same
        SELECT 
            agrmnt_id,
            actual_from_dt,
            actual_to_dt,
            client_id,
            product_id,
            interest_rate,
            ROW_NUMBER() OVER (PARTITION BY agrmnt_id ORDER BY actual_from_dt) - 
            ROW_NUMBER() OVER (PARTITION BY agrmnt_id, client_id, product_id, interest_rate ORDER BY actual_from_dt) AS grp
        FROM dim_dep_agreement
    ) AS temp
    GROUP BY agrmnt_id, client_id, product_id, interest_rate, grp
)
-- Insert the merged data into the new table
SELECT *FROM merged_data ORDER BY agrmnt_id, actual_from_dt;
