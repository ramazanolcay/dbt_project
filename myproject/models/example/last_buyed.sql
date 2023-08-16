{{ config(materialized='table') }}



WITH customer_last_buyed AS (
    SELECT DISTINCT ON (o.name_id)
        o.name_id,
        i.item_name,
        o.order_time
    FROM
        {{ source('my_source', 'orders') }} as o
    JOIN
        {{ source('my_source', 'items') }} as i 
    ON 
        o.item_id = i.id
    
    ORDER BY
        o.name_id, o.order_time DESC
    
)

SELECT * FROM customer_last_buyed
