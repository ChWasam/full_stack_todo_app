from fastapi import FastAPI
from sqlmodel import SQLModel,Field, create_engine
from app import settings

#  Lets make a data model yeh table create nahi kara ga 
#  table = True pass karna para ga agar ham chahta han kah yeh table bhi create kara 
#  Field() : Yeh e.g id ka name sa table me field create kara ha 
#  id is primary ke ku kah filhal ak hi table ha 
#  primary key should be unique 
#  Foreign key aus waqt chahia ho ge jab han banai ga user ka model 

#  AB id ko bnana ha primary key 
#  aur wo unique bbhi honi chahia
#  Agar user  sa  id lai to wo to asi id da sakta ha jo pehla nhi kisi na de ho 
#  Ham yeh chahta ham db yeh khud create kara  
# is ka lia ham   pehla id : int|None dana para ga . None ka matlab absence of data 
#  jab todo ko get kar kah  la kar ai ga aus case me id ho ga 
# Ku kah aus case me database na assign kia ho ga  
#  jab create kara ga to aus waqt none ho ga ku kah ham id to nahi da raha han


class Todo (SQLModel, table = True):
    id : int|None = Field(default=None, primary_key=True)
    content : str = Field(index=True, min_length=3, max_length=54)
    # Index : Is column ko data base me index kar da ge 
    # Faida yeh hota ha kha jab ham search karain ga apna task ko  
    #  to sara database ko sara table scan nahi karna para ga 

    #  data validation ka lia bhi use hota ha is lia min = 3
    is_completed = bool = Field(default=False)
    #  Matlab jab bhi create karain ga task to default value False kar dya ha 

 
connection_string:str = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")
#  ku kah me is postgrs ko psycopg ka sath use kar raha ho 
engine = create_engine(connection_string)



app : FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to TaskTrack todo app"}

@app.get("/todo")
async def read_todos():
    return {"content":"dummy_todo"}


