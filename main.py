from fastapi import FastAPI
from typing import Optional,List
import CBN
app = FastAPI()



@app.get("/api/v1/news/{types}")
async def cbn_news(types:str,asc:Optional[bool]=False,count:Optional[int]=None):
    if types=='us':

        return CBN.news(counter=count,queryurl='cbnnews/us')
    elif types=='world':

        return CBN.news(counter=count, queryurl='cbnnews/cwn')
    elif types=='top':

        return CBN.news(counter=count, queryurl='cbnnews')
    elif types == 'israel':
        return CBN.news(counter=count, queryurl='cbnnews/israel')
    elif types == 'national-security':
        return CBN.news(counter=count, queryurl='cbnnews/national-security')
    elif types == 'politics':
        return CBN.news(counter=count, queryurl='cbnnews/faith-nation')
    elif types == 'entertainment':
        return CBN.news(counter=count, queryurl='cbnnews/entertainment')
    elif types == 'health':
        return CBN.news(counter=count, queryurl='cbnnews/health')
    return {}


@app.get("/")
async def say_hello(name: str):
    return {}
