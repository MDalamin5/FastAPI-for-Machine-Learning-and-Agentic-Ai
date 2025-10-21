from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


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