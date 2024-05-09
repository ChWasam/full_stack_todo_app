# full_stack_todo_app

- Front-end (Next js)
- Back-end (FastAPI,SQLModel,PostgreSQL (Neon))

Steps

1. (Creating Model) We need to create model. Hamara model create ho ga sql model sa jo ORM ha - poetry add sqlmodel - Is sa phir ham khuch cheezain import karain ga
2. pydantic => Data validation and data parsing
3. sql alchemy => data base me tables create kara ga
4. sql model => pydantic + sqlalchemy
5. we need to create model of 2 types 1. Data Model (data ko validate karna ka lia ) 2. Table model (data base me jo table create karna ha aus ka lia )

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

14. python hama postgresql databases ka lia ak driver provide karta ha - poetry add "psycopg[binary]"

15 ab jo model bnaya tha table ka isa create bhi karna ha - Jo Todo class ka data/Fields ho ga wo SQLModel ka metadata attribute ka sath automatically register ho gya (lakin aus ka lia table=True hona chahia)

16 session (Ak app me engine ak ho ga session different create ho ga)

- har function ka lia ak alag sa session create ho ga
  -e.g login har user ka lia ak alag sa session create hota ha - Jab user logout hta ha to wo session close hota ha - jab ak todo bana ge to wo session ka through ho ga - pehla session create karain ga phir session ko close bhi karna para ga - ak engine me mukhtalif session ho ga jo aus engine ka use kar kah jo bhi task ho ga wo perform karwai ga

17 Create todos in database
-session.add()
-session.commit()
-session.refresh()
-session.close()

18. Fastapi

19. ab har method(get, del, post,put) ka lia session ka sara kam karna para ga - generator function - dependency injection

20. Jab hamari app start hoti ha to wo khuch cheezo pa depend kar rahi hoti ha

- tables pa depend karti ha
- Jab user endpoint pa ata ha aur wo todo pass karta ha to todo database me create hona sa pehla khuch kam hona chahia 1. connections ready hona chahia 2. tables create  hona chahia
- Hama is ka lia ak context bnana para ga 

21. ak command ha select yeh ham sqlmodel sa import karain ga 
- Yeh select kara ga table ko 


