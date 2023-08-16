
-- Use the `ref` function to select from other models
{{ config(materialized='table') }}

WITH count_soled_items AS (
    SELECT
        i.item_name,
        COUNT(o.id) as counted
    FROM
        {{ source('my_source', "orders")}} as o
    JOIN
        {{ source('my_source', "items")}} as i
    ON
        o.item_id = i.id
    GROUP BY
        i.item_name
    ORDER BY
        counted DESC
)

select * from count_soled_items