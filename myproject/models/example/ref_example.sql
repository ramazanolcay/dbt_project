{{ config(materialized='table') }}



with final_table as (
    select
        u.name,
        u.surname,
        o.item_name
    FROM
        {{ref("my_first_dbt_model")}} as o
    JOIN
        {{ source('my_source', "users")}} as u
    ON
        o.name_id = u.id
)

select * from final_table