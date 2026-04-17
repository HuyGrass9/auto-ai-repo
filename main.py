local Services = {
    ServerStorage = game:GetService("ServerStorage"),
    ServerScriptService = game:GetService("ServerScriptService"),
    ReplicatedStorage = game:GetService("ReplicatedStorage"),
    Players = game:GetService("Players"),
    RunService = game:GetService("RunService"),
    UserInputService = game:GetService("UserInputService"),
    HttpService = game:GetService("HttpService"),
    Workspace = game:GetService("Workspace"),
    Lighting = game:GetService("Lighting"),
    SoundService = game:GetService("SoundService"),
    TeleportService = game:GetService("TeleportService"),
    GameService = game:GetService("GameService")
}

local function getService(name)
    return Services[name]
end

local Config = {
    -- Config for the script
}

local State = {
    -- State for the script
}

local Cache = {
    -- Cache for the script
}

local Utils = {
    function getMouse()
        return game.Players.LocalPlayer:GetMouse()
    end,
    function getCharacter()
        return game.Players.LocalPlayer.Character
    end,
    function getHumanoid()
        return game.Players.LocalPlayer.Character:WaitForChild("Humanoid")
    end,
    function getCamera()
        return game.Workspace.CurrentCamera
    end,
    function getPlayers()
        return game:GetService("Players"):GetPlayers()
    end,
    function getPlayersByTeam(team)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Team == team then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByRole(role)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild(role) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByTag(tag)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild(tag) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByModel(model)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild(model) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColor(color)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTag(color, tag)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorModel(color, model)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(model) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModel(color, tag, model)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColor(color, tag, model, color2)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character.Head.Color.Color == color2 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTag(color, tag, model, color2, tag2)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character.Head.Color.Color == color2 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModel(color, tag, model, color2, tag2, model2)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character.Head.Color.Color == color2 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColor(color, tag, model, color2, tag2, model2, color3)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTag(color, tag, model, color2, tag2, model2, color3, tag3)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModel(color, tag, model, color2, tag2, model2, color3, tag3, model3)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColor(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTag(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModel(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColor(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTag(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5, tag5)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character:FindFirstChild(tag5) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTagModel(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5, tag5, model5)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character:FindFirstChild(tag5) and player.Character:FindFirstChild(model5) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTagModelColor(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5, tag5, model5, color6)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character:FindFirstChild(tag5) and player.Character:FindFirstChild(model5) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 and player.Character.Head.Color.Color == color6 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTagModelColorTag(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5, tag5, model5, color6, tag6)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character:FindFirstChild(tag5) and player.Character:FindFirstChild(model5) and player.Character:FindFirstChild(tag6) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 and player.Character.Head.Color.Color == color6 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTagModelColorTagModel(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4, tag4, model4, color5, tag5, model5, color6, tag6, model6)
        local players = {}
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") and player.Character.Head:FindFirstChild("Color") and player.Character.Head.Color.Color == color and player.Character:FindFirstChild(tag) and player.Character:FindFirstChild(model) and player.Character:FindFirstChild(tag2) and player.Character:FindFirstChild(model2) and player.Character:FindFirstChild(tag3) and player.Character:FindFirstChild(model3) and player.Character:FindFirstChild(tag4) and player.Character:FindFirstChild(model4) and player.Character:FindFirstChild(tag5) and player.Character:FindFirstChild(model5) and player.Character:FindFirstChild(tag6) and player.Character:FindFirstChild(model6) and player.Character.Head.Color.Color == color2 and player.Character.Head.Color.Color == color3 and player.Character.Head.Color.Color == color4 and player.Character.Head.Color.Color == color5 and player.Character.Head.Color.Color == color6 then
                table.insert(players, player)
            end
        end
        return players
    end,
    function getPlayersByColorTagModelColorTagModelColorTagModelColorTagModelColorTagModelColorTagModelTag(color, tag, model, color2, tag2, model2, color3, tag3, model3, color4,