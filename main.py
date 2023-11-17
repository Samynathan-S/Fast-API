# main.py
from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from app.resolvers.resolver import Query, Mutation 

readSchema = strawberry.Schema( query=Query )

writeSchema = strawberry.Schema( query=Mutation , mutation=Mutation )

app = FastAPI()

@app .get("/")
def index():
    return { "message" : "Welcome to the GraphQL API"}

app.add_route("/read", GraphQL(readSchema, debug=True))

app.add_route("/write", GraphQL(writeSchema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


