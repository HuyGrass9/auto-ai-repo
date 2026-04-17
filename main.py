local Services = {}
Services.Players = game:GetService("Players")
Services.ReplicatedStorage = game:GetService("ReplicatedStorage")
Services.Workspace = game:GetService("Workspace")
Services.RunService = game:GetService("RunService")
Services.HttpService = game:GetService("HttpService")
Services.StarterGui = game:GetService("StarterGui")
Services.StarterPack = game:GetService("StarterPack")
Services.UserInputService = game:GetService("UserInputService")
Services.TweenService = game:GetService("TweenService")
Services.AudioService = game:GetService("AudioService")
Services.GamepadService = game:GetService("GamepadService")
Services.VoiceService = game:GetService("VoiceService")
Services.ScreenGuiService = game:GetService("ScreenGuiService")
Services.Lighting = game:GetService("Lighting")
Services.RenderStepping = game:GetService("RenderStepping")
Services.TextService = game:GetService("TextService")
Services.InputService = game:GetService("InputService")
Services.UserSettingsService = game:GetService("UserSettingsService")
Services.PlayerGui = game:GetService("PlayerGui")
Services.CoreGui = game:GetService("CoreGui")
Services.StarterScripts = game:GetService("StarterScripts")
Services.StarterScripts.ServerScriptService = game:GetService("ServerScriptService")
Services.StarterScripts.ServerStorage = game:GetService("ServerStorage")
Services.StarterScripts.ReplicatedStorage = game:GetService("ReplicatedStorage")
Services.StarterScripts.Workspace = game:GetService("Workspace")
Services.StarterScripts.RunService = game:GetService("RunService")
Services.StarterScripts.HttpService = game:GetService("HttpService")
Services.StarterScripts.StarterGui = game:GetService("StarterGui")
Services.StarterScripts.StarterPack = game:GetService("StarterPack")
Services.StarterScripts.UserInputService = game:GetService("UserInputService")
Services.StarterScripts.TweenService = game:GetService("TweenService")
Services.StarterScripts.AudioService = game:GetService("AudioService")
Services.StarterScripts.GamepadService = game:GetService("GamepadService")
Services.StarterScripts.VoiceService = game:GetService("VoiceService")
Services.StarterScripts.ScreenGuiService = game:GetService("ScreenGuiService")
Services.StarterScripts.Lighting = game:GetService("Lighting")
Services.StarterScripts.RenderStepping = game:GetService("RenderStepping")
Services.StarterScripts.TextService = game:GetService("TextService")
Services.StarterScripts.InputService = game:GetService("InputService")
Services.StarterScripts.UserSettingsService = game:GetService("UserSettingsService")
Services.StarterScripts.PlayerGui = game:GetService("PlayerGui")
Services.StarterScripts.CoreGui = game:GetService("CoreGui")
Services.StarterScripts.ServerScriptService = game:GetService("ServerScriptService")
Services.StarterScripts.ServerStorage = game:GetService("ServerStorage")
Services.StarterScripts.ReplicatedStorage = game:GetService("ReplicatedStorage")
Services.StarterScripts.Workspace = game:GetService("Workspace")
Services.StarterScripts.RunService = game:GetService("RunService")
Services.StarterScripts.HttpService = game:GetService("HttpService")
Services.StarterScripts.StarterGui = game:GetService("StarterGui")
Services.StarterScripts.StarterPack = game:GetService("StarterPack")
Services.StarterScripts.UserInputService = game:GetService("UserInputService")
Services.StarterScripts.TweenService = game:GetService("TweenService")
Services.StarterScripts.AudioService = game:GetService("AudioService")
Services.StarterScripts.GamepadService = game:GetService("GamepadService")
Services.StarterScripts.VoiceService = game:GetService("VoiceService")
Services.StarterScripts.ScreenGuiService = game:GetService("ScreenGuiService")
Services.StarterScripts.Lighting = game:GetService("Lighting")
Services.StarterScripts.RenderStepping = game:GetService("RenderStepping")
Services.StarterScripts.TextService = game:GetService("TextService")
Services.StarterScripts.InputService = game:GetService("InputService")
Services.StarterScripts.UserSettingsService = game:GetService("UserSettingsService")
Services.StarterScripts.PlayerGui = game:GetService("PlayerGui")
Services.StarterScripts.CoreGui = game:GetService("CoreGui")
Services.StarterScripts.ServerScriptService = game:GetService("ServerScriptService")
Services.StarterScripts.ServerStorage = game:GetService("ServerStorage")

local Config = {}
Config.Color = Color3.new(1, 0, 0)
Config.Model = "rbxassetid://"
Config.Tag = "Tag"

local State = {}
State.Players = {}
State.LockedPlayers = {}
State.LockedPlayersCount = 0

local Cache = {}
Cache.Players = {}
Cache.LockedPlayers = {}
Cache.LockedPlayersCount = 0

local Utils = {}
Utils.GetPlayers = function()
    return Services.Players:GetPlayers()
end

Utils.GetPlayerFromCharacter = function(character)
    for _, player in pairs(Services.Players:GetPlayers()) do
        if player.Character and player.Character:FindFirstChild("HumanoidRootPart") and player.Character:FindFirstChild("Humanoid") then
            if player.Character:FindFirstChild("HumanoidRootPart").Parent == character then
                return player
            end
        end
    end
end

Utils.GetPlayerFromUserId = function(userId)
    for _, player in pairs(Services.Players:GetPlayers()) do
        if player.UserId == userId then
            return player
        end
    end
end

Utils.GetPlayerFromName = function(name)
    for _, player in pairs(Services.Players:GetPlayers()) do
        if player.Name == name then
            return player
        end
    end
end

local CombatEngine = {}
CombatEngine.AutoCombo = false
CombatEngine.SwitchTool = false
CombatEngine.FastSkill = false
CombatEngine.StunDetection = false
CombatEngine.BusyDetection = false
CombatEngine.AutoComboDelay = 0.5
CombatEngine.SwitchToolDelay = 0.5
CombatEngine.FastSkillDelay = 0.5
CombatEngine.StunDetectionDelay = 0.5
CombatEngine.BusyDetectionDelay = 0.5

local SilentAim = {}
SilentAim.LockedPlayer = nil
SilentAim.LockedPlayerId = nil
SilentAim.LockedPlayerName = nil
SilentAim.LockedPlayerCharacter = nil
SilentAim.LockedPlayerHumanoid = nil
SilentAim.LockedPlayerHumanoidRootPart = nil
SilentAim.LockedPlayerHumanoidRootPartPosition = Vector3.new(0, 0, 0)
SilentAim.LockedPlayerHumanoidRootPartRotation = Vector3.new(0, 0, 0)
SilentAim.LockedPlayerHumanoidRootPartVelocity = Vector3.new(0, 0, 0)
SilentAim.LockedPlayerHumanoidRootPartAngularVelocity = Vector3.new(0, 0, 0)

local Visuals = {}
Visuals.ESP = false
Visuals.Tracer = false
Visuals.ESPColor = Color3.new(1, 0, 0)
Visuals.TracerColor = Color3.new(1, 0, 0)
Visuals.ESPSize = 10
Visuals.TracerSize = 10

local LagFixer = {}
LagFixer.FakeLag = false
LagFixer.FakeLagDelay = 0.5

local FakeLag = {}
FakeLag.SetNetworkOwner = function(player, newOwner)
    if player then
        if newOwner then
            player:LoadCharacter(newOwner.Character)
        else
            player:LoadCharacter()
        end
    end
end

local MaruUI = {}
MaruUI.getHUI = function()
    local HUI = Instance.new("ScreenGui")
    HUI.Name = "HUI"
    HUI.Parent = game.Players.LocalPlayer.PlayerGui
    return HUI
end

local function getPlayersByColorTagModel(color, tag, model, ...)
    local players = {}
    for _, player in pairs(Services.Players:GetPlayers()) do
        local character = player.Character
        if character and character:FindFirstChild("HumanoidRootPart") and character:FindFirstChild("Humanoid") then
            local humanoid = character:FindFirstChild("Humanoid")
            local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
            local humanoidRootPartPosition = humanoidRootPart.Position
            local humanoidRootPartRotation = humanoidRootPart.Rotation
            local humanoidRootPartVelocity = humanoidRootPart.Velocity
            local humanoidRootPartAngularVelocity = humanoidRootPart.AngularVelocity
            local humanoidRootPartAnchored = humanoidRootPart.Anchored
            local humanoidRootPartCanCollide = humanoidRootPart.CanCollide
            local humanoidRootPartCollisionGroup = humanoidRootPart.CollisionGroup
            local humanoidRootPartParent = humanoidRootPart.Parent
            local humanoidRootPartSize = humanoidRootPart.Size
            local humanoidRootPartTransparency = humanoidRootPart.Transparency
            local humanoidRootPartMaterial = humanoidRootPart.Material
            local humanoidRootPartBrickColor = humanoidRootPart.BrickColor
            local humanoidRootPartColor = humanoidRootPart.Color
            local humanoidRootPartEmbellishments = humanoidRootPart.Embellishments
            local humanoidRootPartEmbellishmentsEnabled = humanoidRootPart.EmbellishmentsEnabled
            local humanoidRootPartEmbellishmentsMaterial = humanoidRootPart.EmbellishmentsMaterial
            local humanoidRootPartEmbellishmentsTransparency = humanoidRootPart.EmbellishmentsTransparency
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngularVelocity
            local humanoidRootPartEmbellishmentsAnchored = humanoidRootPart.EmbellishmentsAnchored
            local humanoidRootPartEmbellishmentsCanCollide = humanoidRootPart.EmbellishmentsCanCollide
            local humanoidRootPartEmbellishmentsCollisionGroup = humanoidRootPart.EmbellishmentsCollisionGroup
            local humanoidRootPartEmbellishmentsParent = humanoidRootPart.EmbellishmentsParent
            local humanoidRootPartEmbellishmentsSize = humanoidRootPart.EmbellishmentsSize
            local humanoidRootPartEmbellishmentsRotation = humanoidRootPart.EmbellishmentsRotation
            local humanoidRootPartEmbellishmentsVelocity = humanoidRootPart.EmbellishmentsVelocity
            local humanoidRootPartEmbellishmentsAngularVelocity = humanoidRootPart.EmbellishmentsAngular