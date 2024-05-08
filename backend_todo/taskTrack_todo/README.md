# full_stack_todo_app

- Front-end (Next js)
- Back-end (FastAPI,SQLModel,PostgreSQL (Neon))

Steps

1. (Creating Model) We need to create model. Hamara model create ho ga sql model sa jo ORM ha - poetry add sqlmodel - Is sa phir ham khuch cheezain import karain ga
2. pydantic => Data validation and data parsing
3. sql alchemy => data base me tables create kara ga
4. sql model => pydantic + sqlalchemy
5. we need to  create model of 2 types 1. Data Model (data ko validate karna ka lia ) 2. Table model (data base me jo table create karna ha aus ka lia )

6. Jab alchemy use hota tha to aus case me 1. Data Model alag banta tha 2. Table model alag banta tha

7.SQLModel
Need to make only one model

8. 2nd step Connecting our app with database - .env file - copy connection string and paste it in .env file

9. DATABASE_URL ko secret rakhna ka lia settings.py ke file bnata han

10. now import DATABASE_URL from setting jo hama engine create karna me madad da ga

11. as we need to setup our connection with database - fastapi -> ka andar sqlmodel-> ka andar engine - yeh engine hmara connection karwai ga db (postgres) ka sath - wo engine ai ga sqlmodel sa
    -from sqlmodel import create_engine

12 Now create engine 

13. ab hama koi asi chezz chahia jo orm ke commands ko sql me convert kar kah database ko da 

14. python hama postgresql databases ka lia ak driver provide karta ha 
        - poetry add "psycopg[binary]"