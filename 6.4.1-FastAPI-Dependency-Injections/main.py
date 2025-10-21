from fastapi import FastAPI, Depends
from typing import Annotated
from dataclasses import dataclass

app = FastAPI()


# -------<Dependency Functions>---------
def provide_inputs(x: int , y: int, z: str):
    if x < 0:
        raise ValueError("X is not less then 0.")
    
    if not y:
        raise ValueError("Y is not provided.")
    return {
        "x": x+2,
        "y": y,
        "zz": z
    }

# -------------<Dependency Class>-----------

@dataclass
class Input:
    x: int
    y: int

@app.get("/")
async def home(inputs: Annotated[dict, Depends(provide_inputs)]):

    total = inputs.get("x") + inputs.get("y")

    return {
        "messages": f"The total value is: {total}, and name: {inputs.get("zz")}"
    }


@app.get("/testline")
async def testline(inputs: Annotated[dict, Depends(provide_inputs)]):

    return {
        "square_x": f"{inputs.get("x") ** 2}",
        "square_y": f"{inputs.get("y") ** 2}"
    }

@app.get("/class_call")
async def class_val(inputs: Annotated[Input, Depends(Input)]):

    return {
        "square_x": f"{inputs.x ** 2}",
        "square_y": f"{inputs.y ** 2}"
    }