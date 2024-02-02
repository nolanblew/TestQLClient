from ariadne import QueryType, make_executable_schema, ObjectType
from ariadne.asgi import GraphQL
from fastapi import FastAPI
import uvicorn

type_defs = """
type Query {
  GetByUsername(username: String!): User
}

type User {
  id: ID!
  username: String!
  name: String!
  loginAttempts(first: Int!): [LoginAttempt!]!
}

type LoginAttempt {
  id: ID!
  time: String!
  success: Boolean!
}
"""

query = QueryType()
user_type = ObjectType("User")

# Static data to represent a list of users for demonstration
static_users = [
    {
        "id": "1",
        "username": "john",
        "name": "John Doe",
        "loginAttempts": [
            {"id": "la1", "time": "2023-01-01T12:00:00Z", "success": True},
            {"id": "la2", "time": "2023-01-02T12:00:00Z", "success": False},
        ]
    },
    {
        "id": "2",
        "username": "jane",
        "name": "Jane Doe",
        "loginAttempts": [
            {"id": "la3", "time": "2023-01-01T12:00:00Z", "success": True},
            {"id": "la4", "time": "2023-01-02T12:00:00Z", "success": True},
        ]
    }
]

@query.field("GetByUsername")
def resolve_get_by_username(_, info, username):
    # Filter the user by username; in a real app, you'd query your database
    user = next((user for user in static_users if user["username"] == username), None)
    return user

@user_type.field("loginAttempts")
def resolve_login_attempts(user, info, first):
    # Return only the first 'n' login attempts
    return user["loginAttempts"][:first]

schema = make_executable_schema(type_defs, query, user_type)
graphql_app = GraphQL(schema, debug=True)

app = FastAPI()

# Mount the GraphQL app
app.mount("/graphql", graphql_app)

# Optional: add this to run with `python server.py`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
