
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}



WITH customer_product AS (
    SELECT
        o.name_id,
        i.item_name
    FROM
        {{ source('my_source', 'orders') }} as o
    JOIN
        {{ source('my_source', 'items') }} as i 
    ON 
        o.item_id = i.id
    ORDER BY
        o.name_id ASC
)

SELECT * FROM customer_product


/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
