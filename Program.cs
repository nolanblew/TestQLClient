using TestQLClient;
using ZeroQL.Client;

var username = "john";

var httpClient = new HttpClient(new LoggingHandler(new HttpClientHandler())) { BaseAddress = new Uri("http://localhost:8000/graphql") };
var client = new ZeroQLClient(httpClient);

// // This does not work because of LastLogin
// var request = await client.Query(q => q.GetByUsername(username, user => new MyUser(
//     Id: user.Id,
//     Name: user.Name,
//     Username: user.Username,
//     LastLogin: user.LoginAttempts(first: 1, login => new MyLogin(
//         Time: login.Time,
//         Success: login.Success
//     )).FirstOrDefault()
// )));

// This works fine without the LastLoggin: Uncomment to run:
var request = await client.Query(q => q.GetByUsername(username, user => new MyUser(
    Id: user.Id,
    Name: user.Name,
    Username: user.Username
)));

// // However, this also doesn't work because we are assigning a custom value to LastLoggin: Uncomment to run:
// var request = await client.Query(q => q.GetByUsername(username, user => new MyUser(
//     Id: user.Id,
//     Name: user.Name,
//     Username: user.Username,
//     LastLogin: null
// )));

var userData = request.Data;

Console.WriteLine($"Hello, {userData.Name}! You last logged in on: {userData.LastLogin?.Time ?? "never"}");