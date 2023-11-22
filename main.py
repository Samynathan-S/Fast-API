# main.py
from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from app.resolvers.resolver import Query, Mutation 

readSchema = strawberry.Schema( query=Query )

writeSchema = strawberry.Schema( query=Mutation , mutation=Mutation )

app = FastAPI( debug=True )

origins = ["http://localhost:3000/", "http://0.0.0.0:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app .get("/")
def index():
    return { "message" : "Welcome to the GraphQL API"}

app.add_route("/read", GraphQL(readSchema, debug=True))

app.add_route("/write", GraphQL(writeSchema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


