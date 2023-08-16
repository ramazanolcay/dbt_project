Firstly, I generated fake data using the Faker library and created an artificial database by writing the data to a PostgreSQL database using SQLAlchemy. The table structure for the database is provided below.

![image](https://github.com/ramazanolcay/dbt_project/assets/87130915/91fe3efc-cf1b-4639-8c0f-14101bdbbced)


Later on, I organized the .yml files for DBT, created my models, and utilized features like reference functions within these models. Visuals of the outputs from these models are presented below. In the subsequent stages of the project, I will also incorporate tools like Airflow.

my_first_dbt_model.sql

![image](https://github.com/ramazanolcay/dbt_project/assets/87130915/49778316-5797-48c3-8e4c-7f328da1e625)



my_second_dbt_model.sql

![image](https://github.com/ramazanolcay/dbt_project/assets/87130915/c3babe64-e427-44e5-8030-8e3426f07012)



last_buyed.sql

![image](https://github.com/ramazanolcay/dbt_project/assets/87130915/e9188d07-e2a3-49cf-86df-9d4198bf9eb5)



ref_example.sql

![image](https://github.com/ramazanolcay/dbt_project/assets/87130915/ff3f1691-f121-45a4-a606-e2505dd58ddf)
