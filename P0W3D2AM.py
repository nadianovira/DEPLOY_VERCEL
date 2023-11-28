from fastapi import FastAPI, HTTPException, Request
import pandas as pd
key = 'secret123'

#panggil class FastAPI
app = FastAPI()

#load data csv
data = pd.read_csv('data.csv')

#define url/endpoint
@app.get('/')
def handler():
    return {'message' : 'hello'}

@app.get('/secret')
def handler(request: Request):
    #retrieve header content from request
    headers = request.headers

    #retrieve User-Agent key in headers
    agent = headers.get ('User-Agent')

    token = headers.get('Token')

    if token == None: #jika key token tidak ada dalam headers
        raise HTTPException(status_code=500, detail='belum login')
    else: # jika ada key token
        if token != key: #
            raise HTTPException(status_code=500, detail='key tidak sesuai')
        else:
            return {
                "message" : "halaman utama",
                "agent": agent #display value agent
                }

@app.get('/data')
def handler ():
    return data.to_dict(orient='records')


@app.get('/home/{user}')
def handler(user):
    if user == 'nadia':
        return {
        "message" : "hallo home",
        "user" : user
    }
    else:
        #handle error, supaya tidak mati errornya 
        raise HTTPException(status_code=400, detail='not found')
    
