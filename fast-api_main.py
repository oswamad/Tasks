#Api that accepts as input any onedimensional function y(x) = f(x) and a required range for x, 
#returns a calculate f(x)
import numpy as np
from matplotlib import pyplot as plt
from math import *
from fastapi import FastAPI, Path

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Enable CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/func-api/{l_range}/{u_range}/{function}")
def show(l_range:int = Path(description="Lower value of the range"),
    u_range:int = Path(description="Upper value of the range"), 
    function:str = Path(description="Function to perform the evaluation")):

    result = []
    t = np.arange(l_range,u_range)#Create range
    t = t.tolist()
    for x in t:
        result.append(eval(function))#Evaluate function for a given x  

    return {"interval":t,"valuesfunc":result}
