# Test Repo for ZeroQL Issue

## Run the Server
The server is written in Python. Make sure you first have the following installed:
```bash
pip install ariadne uvicorn
```

Then navigate to the directory with `server.py` and run:
```bash
uvicorn server:app
```

You can now navigate to: [http://localhost:8000/graphql/](http://localhost:8000/graphql/) in your browser to see the server and explore.

### Working Query
Here is a working query. Feel free to put it in your graphql explorer:
```
query {
  GetByUsername(username: "john") {
    id,
    name,
    loginAttempts(first: 1) {
      time,
      success
    }
  }
}
```

## The Client
There are 3 sections of code that you want to have just 1 commented out at a time (this was a sample project after all). One works (without any reference to `LastLoginAttempt`), while the other two that do reference it throw exceptions.

See [the issue on Github](https://github.com/byme8/ZeroQL/issues/91) for more info!