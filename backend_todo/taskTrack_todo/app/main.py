from fastapi import FastAPI
from sqlmodel import SQLModel,Field, create_engine
from app import settings

#  Lets make a data model yeh table create nahi kara ga 
#  table = True pass karna para ga agar ham chahta han kah yeh table bhi create kara 
#  Field() : Yeh e.g id ka name sa table me field create karta ha 
#  id is primary key ku kah filhal ak hi table ha 
#  primary key should be unique 
#  Foreign key aus waqt chahia ho ge jab ham banai ga user ka model 

#  Ab id ko bnana ha primary key 
#  aur wo unique bhi honi chahia
#  Agar user  sa  id lai to wo to asi id da sakta ha jo pehla nhi kisi na de ho 
#  Ham yeh chahta ham db yeh khud create kara  
# is ka lia ham   pehla id : int|None dana para ga . None ka matlab absence of data 
#  jab todo ko get kar kah  la kar ai ga aus case me id ho ga 
# Ku kah aus case me database na assign kia ho ga  
#  jab todo ko create kara ga to aus waqt none ho ga ku kah ham id to nahi da raha han


class Todo (SQLModel, table = True):
    id : int|None = Field(default=None, primary_key=True)
    content : str = Field(index=True, min_length=3, max_length=54)
    # Index : Is column ko data base me index kar da ge 
    # Faida yeh hota ha kha jab ham search karain ga apna task ko  
    #  to database ko sara table scan nahi karna para ga 

    #  data validation ka lia bhi use hota ha is lia min_length=3
    is_completed = bool = Field(default=False)
    #  Matlab jab bhi create karain ga task to default value False kar dya ha 

# *******************************************************************
#  Engine is one for whole application 

connection_string:str = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")
#  ku kah me is postgrs ko psycopg ka sath use kar raha ho is lia replace kia ha 
#  kah mera communication is sa ho ge postgresql+psycopg 

#  Ab ham chahta han jo bhi hmari communication ho database ka sath wo encrypt ho kah jai 
#  so we will add secure socket layer(ssl)
engine = create_engine(connection_string, connect_args={"sslmode":"require "},pool_recycle=300)

#   Hamara jo engine ha wo connection pool banai ga 
#  wo ak connection hmara database ka sath nahi kara ga 
#   by default sqlslchemy me  jab app start ho ge to 5 connection establish karta ha 
#  lakin ham change kar sakta han pool_size=10 is tarha sa
#  matlab wo connection ka pool bna raha ha 

#  naya connection jab database ka sath bana ga to aus ka aupar time lagta ha 
#  wo time hamara waste ho raha ha 
#  jasa waiter ai ga order lai ga kitchen me jai ga aur wapis order lana chala jai ga 
#  yani connection standby ho ga 

#  pool_recycle matlab kah 300 sec yani 5 min bad connection recycle ho jai 

# *******************************************************************





app : FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to TaskTrack todo app"}

@app.get("/todo")
async def read_todos():
    return {"content":"dummy_todo"}


