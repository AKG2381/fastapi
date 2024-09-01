from fastapi import Header, HTTPException

async def get_token_header(x_token : str = Header(...)):
    if x_token != 'fake_super_token':
        raise HTTPException(status_code=400, detail='X-Token Header Invalid')

async def get_query_token(token : str = 'Jessica'):
    if token != 'Jessica':
        raise HTTPException(status_code=400, detail='No Jessica Token provided')
    

