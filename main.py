from typing import Union

from fastapi import FastAPI, HTTPException, Request

from automata.fa.dfa import DFA

from automata.fa.nfa import NFA

from automata.pda.dpda import DPDA

app = FastAPI()


@app.post("/dpda")
async def dpda(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    stack_symbols = set(info.get("stack_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    initial_stack_symbol = info.get("initial_stack_symbol", "")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if len(states) == 0:
        raise HTTPException(status_code=404, detail="Status cannot be empty")
    if len(input_symbols) == 0:
        raise HTTPException(status_code=404, detail="Input symbols cannot be empty")
    if len(stack_symbols) == 0:
        raise HTTPException(status_code=404, detail="Stack symbols cannot be empty")
    if len(transitions) == 0:
        raise HTTPException(status_code=404, detail="Transitions cannot be empty")
    if initial_state == "":
        raise HTTPException(status_code=404, detail="Initial state cannot be empty")
    if initial_stack_symbol == "":
        raise HTTPException(status_code=404, detail="Initial Stack state cannot be empty")
    if len(final_states) == 0:
        raise HTTPException(status_code=404, detail="Final states cannot be empty")
    if input_w == "":
        raise HTTPException(status_code=404, detail="Input cannot be empty")

    dpda = DPDA(
        states=states,
        input_symbols=input_symbols,
        stack_symbols=stack_symbols,
        transitions=transitions,
        initial_state=initial_state,
        initial_stack_symbol=initial_stack_symbol,
        final_states=final_states,
        acceptance_mode="final_state"
    )

    if (dpda.accepts_input(input_w)):
        return {"accepted": True, "input": input_w}
    else:
        return {"accepted": False, "input": input_w}


@app.post("/nfa")
async def nfa(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if len(states) == 0:
        raise HTTPException(status_code=404, detail="States cannot be empty")
    if len(input_symbols) == 0:
        raise HTTPException(status_code=404, detail="Input symbols cannot be empty")
    if len(transitions) == 0:
        raise HTTPException(status_code=404, detail="Transitions cannot be empty")
    if initial_state == "":
        raise HTTPException(status_code=404, detail="Initial state cannot be empty")
    if len(final_states) == 0:
        raise HTTPException(status_code=404, detail="Final states cannot be empty")
    if input_w == "":
        raise HTTPException(status_code=404, detail="Input cannot be empty")

    nfa = NFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    if nfa.accepts_input(input_w):
        return {"accepted": True, "input": input_w}
    else:
        return {"accepted": False, "input": input_w}


@app.post("/dfa")
async def dfa(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if len(states) == 0:
        raise HTTPException(status_code=404, detail="Status cannot be empty")
    if len(input_symbols) == 0:
        raise HTTPException(status_code=404, detail="Input symbols cannot be empty")
    if len(transitions) == 0:
        raise HTTPException(status_code=404, detail="Transitions cannot be empty")
    if initial_state == "":
        raise HTTPException(status_code=404, detail="Initial state cannot be empty")
    if len(final_states) == 0:
        raise HTTPException(status_code=404, detail="Final states cannot be empty")
    if input_w == "":
        raise HTTPException(status_code=404, detail="Input cannot be empty")

    dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    if dfa.accepts_input(input_w):
        return {"accepted": True, "input": input_w}
    else:
        return {"accepted": False, "input": input_w}


@app.get("/vitor")
def read_vitor():
    return {"message": "Hello vitor"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
