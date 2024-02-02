namespace TestQLClient;

public record MyUser(string Id, string Name, string Username, MyLogin? LastLogin = null);

public record MyLogin(string Time, bool Success);