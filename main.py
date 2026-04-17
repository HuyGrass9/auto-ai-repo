-- Services
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local HttpService = game:GetService("HttpService")
local GameSettings = game:GetService("GameSettings")

-- Config
local Config = {}
Config.SilentAim = true
Config.Visuals = true
Config.LagFixer = true
Config.FakeLag = true
Config.MaruiUI = true
Config.CombatEngine = true

-- State
local State = {}
State.CurrentTool = nil
State.Target = nil
State.IsSilentAiming = false
State.IsLagFixing = false
State.IsFakingLag = false

-- Cache
local Cache = {}
Cache.Players = {}
Cache.Characters = {}

-- Utils
local function getHui()
    local Player = game.Players.LocalPlayer
    local ScreenGui = Player:WaitForChild("ScreenGui")
    local Hui = ScreenGui:WaitForChild("Hui")
    return Hui
end

local function getCharacter()
    local Player = game.Players.LocalPlayer
    local Character = Player.Character
    return Character
end

local function getTarget()
    local Player = game.Players.LocalPlayer
    local Character = getCharacter()
    local Target = Character:FindFirstChild("HumanoidRootPart")
    if Target then
        Target = Target.Parent
        while not Target:IsA("Model") do
            Target = Target.Parent
        end
    end
    return Target
end

local function isPlayerOnline(PlayerName)
    for _, Player in pairs(Players:GetPlayers()) do
        if Player.Name == PlayerName then
            return true
        end
    end
    return false
end

-- CombatEngine
local function combatEngine()
    local Player = game.Players.LocalPlayer
    local Character = getCharacter()
    local CurrentTool = State.CurrentTool
    if CurrentTool then
        if CurrentTool.Name == "Wand" then
            -- Auto Combo
            local autoCombo = true
            if autoCombo then
                local Target = getTarget()
                if Target then
                    local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                    if Distance <= 10 then
                        local CurrentTool = State.CurrentTool
                        if CurrentTool then
                            CurrentTool:FireServer("Attack")
                        end
                    end
                end
            end
        elseif CurrentTool.Name == "Sword" then
            -- Auto Combo
            local autoCombo = true
            if autoCombo then
                local Target = getTarget()
                if Target then
                    local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                    if Distance <= 10 then
                        local CurrentTool = State.CurrentTool
                        if CurrentTool then
                            CurrentTool:FireServer("Attack")
                        end
                    end
                end
            end
        end
    end
end

-- SilentAim
local SilentAim = {}
SilentAim.__index = SilentAim

function SilentAim.new()
    local instance = setmetatable({}, SilentAim)
    instance.Target = nil
    instance.IsSilentAiming = false
    return instance
end

function SilentAim:__newindex(key, value)
    if self.IsSilentAiming then
        if key == "Target" then
            self.Target = value
        end
    end
end

function SilentAim:__index(key)
    if self.IsSilentAiming then
        if key == "Target" then
            return self.Target
        end
    end
end

function SilentAim:getNamecallHook()
    local function hookFunc(func, ...)
        if self.IsSilentAiming then
            local Target = self.Target
            if Target then
                local Distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                if Distance <= 10 then
                    return func(...)
                else
                    return nil
                end
            else
                return nil
            end
        else
            return func(...)
        end
    end
    return hookFunc
end

function SilentAim:getTarget()
    local Player = game.Players.LocalPlayer
    local Character = getCharacter()
    local Target = Character:FindFirstChild("HumanoidRootPart")
    if Target then
        Target = Target.Parent
        while not Target:IsA("Model") do
            Target = Target.Parent
        end
    end
    return Target
end

function SilentAim:silentAim()
    local function silentAimFunc()
        local Target = self:getTarget()
        if Target then
            local Distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
            if Distance <= 10 then
                self.IsSilentAiming = true
                self.Target = Target
                return Target
            else
                self.IsSilentAiming = false
                self.Target = nil
                return nil
            end
        else
            self.IsSilentAiming = false
            self.Target = nil
            return nil
        end
    end
    return silentAimFunc
end

function SilentAim:velocityPrediction()
    local function velocityPredictionFunc()
        local Target = self:getTarget()
        if Target then
            local Distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
            local Velocity = (Target.HumanoidRootPart.Velocity - game.Players.LocalPlayer.Character.HumanoidRootPart.Velocity).Magnitude
            if Distance <= 10 then
                return Target
            else
                return nil
            end
        else
            return nil
        end
    end
    return velocityPredictionFunc
end

-- Visuals
local function visuals()
    local Player = game.Players.LocalPlayer
    local Character = getCharacter()
    local Target = getTarget()
    if Target then
        local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
        if Distance <= 10 then
            local Visuals = game.ReplicatedStorage:WaitForChild("Visuals")
            local ESP = Visuals:WaitForChild("ESP")
            local AllyColor = ESP:WaitForChild("AllyColor")
            local TargetColor = ESP:WaitForChild("TargetColor")
            local BountyColor = ESP:WaitForChild("BountyColor")
            local VisualsInstance = ESP:Clone()
            VisualsInstance.Parent = game.Workspace
            VisualsInstance.AllyColor = AllyColor
            VisualsInstance.TargetColor = TargetColor
            VisualsInstance.BountyColor = BountyColor
        end
    end
end

-- LagFixer
local LagFixer = {}
LagFixer.__index = LagFixer

function LagFixer.new()
    local instance = setmetatable({}, LagFixer)
    instance.IsLagFixing = false
    return instance
end

function LagFixer:__newindex(key, value)
    if self.IsLagFixing then
        if key == "Beams" then
            local Beams = value
            for _, Beam in pairs(Beams:GetDescendants()) do
                if Beam:IsA("BasePart") then
                    Beam.CanCollide = false
                end
            end
        elseif key == "Trails" then
            local Trails = value
            for _, Trail in pairs(Trails:GetDescendants()) do
                if Trail:IsA("BasePart") then
                    Trail.CanCollide = false
                end
            end
        elseif key == "LocalPlayerEffects" then
            local LocalPlayerEffects = value
            for _, Effect in pairs(LocalPlayerEffects:GetDescendants()) do
                if Effect:IsA("BasePart") then
                    Effect.CanCollide = false
                end
            end
        end
    end
end

function LagFixer:__index(key)
    if self.IsLagFixing then
        if key == "Beams" then
            return game.Workspace:GetDescendants()
        elseif key == "Trails" then
            return game.Workspace:GetDescendants()
        elseif key == "LocalPlayerEffects" then
            return game.Players.LocalPlayer.Character:GetDescendants()
        end
    end
end

function LagFixer:fakeLag()
    local function fakeLagFunc()
        local LagFixerInstance = LagFixer.new()
        LagFixerInstance.IsLagFixing = true
        return LagFixerInstance
    end
    return fakeLagFunc
end

-- FakeLag
local function fakeLag()
    local function fakeLagFunc()
        local Player = game.Players.LocalPlayer
        local Character = getCharacter()
        local Target = getTarget()
        if Target then
            local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
            if Distance <= 10 then
                local FakeLag = game.ReplicatedStorage:WaitForChild("FakeLag")
                local SetNetworkOwner = FakeLag:WaitForChild("SetNetworkOwner")
                SetNetworkOwner:FireServer(Target)
            end
        end
    end
    return fakeLagFunc
end

-- MaruUI
local function maruUI()
    local function maruUIFunc()
        local Player = game.Players.LocalPlayer
        local Character = getCharacter()
        local Target = getTarget()
        if Target then
            local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
            if Distance <= 10 then
                local MaruUI = game.ReplicatedStorage:WaitForChild("MaruUI")
                local Hui = MaruUI:WaitForChild("Hui")
                Hui.Parent = game.Players.LocalPlayer.PlayerGui
            end
        end
    end
    return maruUIFunc
end

-- Main
local function main()
    local Player = game.Players.LocalPlayer
    local Character = getCharacter()
    local CurrentTool = State.CurrentTool
    if CurrentTool then
        if CurrentTool.Name == "Wand" then
            -- Auto Combo
            local autoCombo = true
            if autoCombo then
                local Target = getTarget()
                if Target then
                    local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                    if Distance <= 10 then
                        local CurrentTool = State.CurrentTool
                        if CurrentTool then
                            CurrentTool:FireServer("Attack")
                        end
                    end
                end
            end
        elseif CurrentTool.Name == "Sword" then
            -- Auto Combo
            local autoCombo = true
            if autoCombo then
                local Target = getTarget()
                if Target then
                    local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                    if Distance <= 10 then
                        local CurrentTool = State.CurrentTool
                        if CurrentTool then
                            CurrentTool:FireServer("Attack")
                        end
                    end
                end
            end
        end
    end
end

-- Hooks
local function onCharacterAdded(Character)
    State.Characters[Character.Name] = Character
end

local function onCharacterRemoved(Character)
    State.Characters[Character.Name] = nil
end

local function onPlayerAdded(Player)
    State.Players[Player.Name] = Player
end

local function onPlayerRemoved(Player)
    State.Players[Player.Name] = nil
end

local function onStun(Character)
    local Target = getTarget()
    if Target then
        local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
        if Distance <= 10 then
            local CurrentTool = State.CurrentTool
            if CurrentTool then
                CurrentTool:FireServer("Attack")
            end
        end
    end
end

local function onUnstun(Character)
    local Target = getTarget()
    if Target then
        local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
        if Distance <= 10 then
            local CurrentTool = State.CurrentTool
            if CurrentTool then
                CurrentTool:FireServer("Attack")
            end
        end
    end
end

-- Events
game.Players.LocalPlayer.CharacterAdded:Connect(onCharacterAdded)
game.Players.LocalPlayer.CharacterRemoved:Connect(onCharacterRemoved)
game.Players.PlayerAdded:Connect(onPlayerAdded)
game.Players.PlayerRemoved:Connect(onPlayerRemoved)
game.Players.LocalPlayer.Character.Stuck:Connect(onStun)
game.Players.LocalPlayer.Character.Unstuck:Connect(onUnstun)

-- Task
task.spawn(function()
    while true do
        -- SilentAim
        local SilentAimInstance = SilentAim.new()
        SilentAimInstance:getNamecallHook()
        SilentAimInstance:silentAim()
        SilentAimInstance:velocityPrediction()

        -- CombatEngine
        combatEngine()

        -- Visuals
        visuals()

        -- LagFixer
        local LagFixerInstance = LagFixer.new()
        LagFixerInstance:fakeLag()

        -- FakeLag
        fakeLag()

        -- MaruUI
        maruUI()

        -- Main
        main()

        -- Wait
        wait(0.1)
    end
end)

-- Error Handling
pcall(function()
    -- Services
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RunService = game:GetService("RunService")
    local Players = game:GetService("Players")
    local UserInputService = game:GetService("UserInputService")
    local HttpService = game:GetService("HttpService")
    local GameSettings = game:GetService("GameSettings")

    -- Config
    local Config = {}
    Config.SilentAim = true
    Config.Visuals = true
    Config.LagFixer = true
    Config.FakeLag = true
    Config.MaruiUI = true
    Config.CombatEngine = true

    -- State
    local State = {}
    State.CurrentTool = nil
    State.Target = nil
    State.IsSilentAiming = false
    State.IsLagFixing = false
    State.IsFakingLag = false

    -- Cache
    local Cache = {}
    Cache.Players = {}
    Cache.Characters = {}

    -- Utils
    local function getHui()
        local Player = game.Players.LocalPlayer
        local ScreenGui = Player:WaitForChild("ScreenGui")
        local Hui = ScreenGui:WaitForChild("Hui")
        return Hui
    end

    local function getCharacter()
        local Player = game.Players.LocalPlayer
        local Character = Player.Character
        return Character
    end

    local function getTarget()
        local Player = game.Players.LocalPlayer
        local Character = getCharacter()
        local Target = Character:FindFirstChild("HumanoidRootPart")
        if Target then
            Target = Target.Parent
            while not Target:IsA("Model") do
                Target = Target.Parent
            end
        end
        return Target
    end

    local function isPlayerOnline(PlayerName)
        for _, Player in pairs(Players:GetPlayers()) do
            if Player.Name == PlayerName then
                return true
            end
        end
        return false
    end

    -- CombatEngine
    local function combatEngine()
        local Player = game.Players.LocalPlayer
        local Character = getCharacter()
        local CurrentTool = State.CurrentTool
        if CurrentTool then
            if CurrentTool.Name == "Wand" then
                -- Auto Combo
                local autoCombo = true
                if autoCombo then
                    local Target = getTarget()
                    if Target then
                        local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                        if Distance <= 10 then
                            local CurrentTool = State.CurrentTool
                            if CurrentTool then
                                CurrentTool:FireServer("Attack")
                            end
                        end
                    end
                end
            elseif CurrentTool.Name == "Sword" then
                -- Auto Combo
                local autoCombo = true
                if autoCombo then
                    local Target = getTarget()
                    if Target then
                        local Distance = (Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                        if Distance <= 10 then
                            local CurrentTool = State.CurrentTool
                            if CurrentTool then
                                CurrentTool:FireServer("Attack")
                            end
                        end
                    end
                end
            end
        end
    end

    -- SilentAim
    local SilentAim = {}
    SilentAim.__index = SilentAim

    function SilentAim.new()
        local instance = setmetatable({}, SilentAim)
        instance.Target = nil
        instance.IsSilentAiming = false
        return instance
    end

    function SilentAim:__newindex(key, value)
        if self.IsSilentAiming then
            if key == "Target" then
                self.Target = value
            end
        end
    end

    function SilentAim:__index(key)
        if self.IsSilentAiming then
            if key == "Target" then
                return self.Target
            end
        end
    end

    function SilentAim:getNamecallHook()
        local function hookFunc(func, ...)
            if self.IsSilentAiming then
                local Target = self.Target
                if Target then
                    local Distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                    if Distance <= 10 then
                        return func(...)
                    else
                        return nil
                    end
                else
                    return nil
                end
            else
                return func(...)
            end
        end
        return hookFunc
    end

    function SilentAim:getTarget()
        local Player = game.Players.LocalPlayer
        local Character = getCharacter()
        local Target = Character:FindFirstChild("HumanoidRootPart")
        if Target then
            Target = Target.Parent
            while not Target:IsA("Model") do
                Target = Target.Parent
            end
        end
        return Target
    end

    function SilentAim:silentAim()
        local function silentAimFunc()
            local Target = self:getTarget()
            if Target then
                local Distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - Target.HumanoidRootPart.Position).Magnitude
                if Distance <= 10 then
                    self.IsSilentAiming = true
                    self.Target = Target
                    return Target
                else
                    self.IsSilentAiming = false
                    self.Target = nil
                    return nil
                end
            else
                self.IsSilentAiming = false
                self.Target = nil
                return nil
            end
        end