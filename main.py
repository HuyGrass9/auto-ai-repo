```lua
-- Services
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")
local HttpService = game:GetService("HttpService")
local ServerScriptService = game:GetService("ServerScriptService")

-- Config
local Config = {
    AutoCombo = true,
    SwitchTool = true,
    FastSkill = true,
    StunBusyDetection = true,
    SilentAim = true,
    ESP = true,
    Tracer = true,
    FakeLag = true,
    UI = true,
    LagFixer = true,
    FakeLagDelay = 0.5,
    SilentAimFOV = 90,
    SilentAimRange = 100,
    ESPSize = 10,
    ESPColor = Color3.new(1, 0, 0),
    TracerColor = Color3.new(1, 1, 0),
    FakeLagSpeed = 10,
    LagFixerSpeed = 10,
}

-- State
local State = {
    isRunning = false,
    isSilentAiming = false,
    isAutoCombining = false,
    isSwitchingTool = false,
    isFastSkilling = false,
    isStunned = false,
    isBusy = false,
    isFakeLagging = false,
    isLagFixing = false,
}

-- Cache
local Cache = {
    players = {},
    tools = {},
    skills = {},
    targets = {},
}

-- Utils
local function getHUI()
    local HUI = Instance.new("ScreenGui")
    HUI.Name = "MayChemXeoCanV2"
    HUI.Parent = Players.LocalPlayer.PlayerGui
    return HUI
end

local function getTool()
    local tool = Players.LocalPlayer.Character:FindFirstChild("Tool")
    if tool then
        return tool
    end
    return nil
end

local function getSkill()
    local skill = Players.LocalPlayer.Character:FindFirstChild("Skill")
    if skill then
        return skill
    end
    return nil
end

local function getTarget()
    local target = Cache.targets[Players.LocalPlayer.UserId]
    if target then
        return target
    end
    return nil
end

local function setTarget(target)
    Cache.targets[Players.LocalPlayer.UserId] = target
end

local function getPlayers()
    return Players:GetPlayers()
end

local function getDistance(player)
    local character = player.Character
    local distance = (Players.LocalPlayer.Character.HumanoidRootPart.Position - character.HumanoidRootPart.Position).Magnitude
    return distance
end

local function isStunned(player)
    local character = player.Character
    local stun = character:FindFirstChild("Stun")
    if stun and stun.Value then
        return true
    end
    return false
end

local function isBusy(player)
    local character = player.Character
    local busy = character:FindFirstChild("Busy")
    if busy and busy.Value then
        return true
    end
    return false
end

local function getToolType(tool)
    if tool.Name == "Wand" then
        return "Wand"
    elseif tool.Name == "Sword" then
        return "Sword"
    elseif tool.Name == "Bow" then
        return "Bow"
    end
    return nil
end

local function getSkillType(skill)
    if skill.Name == "Fireball" then
        return "Fireball"
    elseif skill.Name == "Iceball" then
        return "Iceball"
    elseif skill.Name == "Lightning" then
        return "Lightning"
    end
    return nil
end

-- CombatEngine
local function autoCombo()
    if State.isAutoCombining then
        local tool = getTool()
        local skill = getSkill()
        if tool and skill then
            local toolType = getToolType(tool)
            local skillType = getSkillType(skill)
            if toolType == "Wand" and skillType == "Fireball" then
                skill:FireServer()
            elseif toolType == "Sword" and skillType == "Iceball" then
                skill:FireServer()
            elseif toolType == "Bow" and skillType == "Lightning" then
                skill:FireServer()
            end
        end
    end
end

local function switchTool()
    if State.isSwitchingTool then
        local tool = getTool()
        if tool then
            tool:Destroy()
        end
    end
end

local function fastSkill()
    if State.isFastSkilling then
        local skill = getSkill()
        if skill then
            skill:FireServer()
        end
    end
end

local function stunDetection()
    if State.isStunned then
        local players = getPlayers()
        for _, player in pairs(players) do
            if player ~= Players.LocalPlayer and isStunned(player) then
                print(player.Name .. " is stunned!")
            end
        end
    end
end

local function busyDetection()
    if State.isBusy then
        local players = getPlayers()
        for _, player in pairs(players) do
            if player ~= Players.LocalPlayer and isBusy(player) then
                print(player.Name .. " is busy!")
            end
        end
    end
end

-- SilentAim
local function silentAim()
    if State.isSilentAiming then
        local target = getTarget()
        if target then
            local distance = getDistance(target)
            if distance <= Config.SilentAimRange then
                local aimPart = target.Character:FindFirstChild("Head")
                if aimPart then
                    local aimPosition = aimPart.Position
                    local playerPosition = Players.LocalPlayer.Character.HumanoidRootPart.Position
                    local aimDirection = (aimPosition - playerPosition).Unit
                    Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.lookAt(playerPosition, aimPosition + aimDirection * Config.SilentAimFOV)
                end
            end
        end
    end
end

-- Visuals
local function esp()
    if State.isRunning then
        local target = getTarget()
        if target then
            local distance = getDistance(target)
            if distance <= Config.ESPSize then
                local espGui = Instance.new("BillboardGui")
                espGui.Name = "ESP"
                espGui.Parent = target.Character
                local espText = Instance.new("TextLabel")
                espText.Name = "ESPText"
                espText.Parent = espGui
                espText.Text = Players.LocalPlayer.Name
                espText.Size = UDim2.new(0, 100, 0, 20)
                espText.Position = UDim2.new(0, 0, 0, 0)
                espText.BackgroundTransparency = 1
                espText.TextColor3 = Config.ESPColor
            end
        end
    end
end

local function tracer()
    if State.isRunning then
        local target = getTarget()
        if target then
            local distance = getDistance(target)
            if distance <= Config.TracerSize then
                local tracer = Instance.new("Beam")
                tracer.Name = "Tracer"
                tracer.Parent = target.Character
                tracer.Color = Config.TracerColor
                tracer.Width0 = 0
                tracer.Width1 = 10
                tracer.Texture = "rbxassetid://"
                tracer.LightInfluence = 0
                tracer.Lifetime = 0.5
                tracer.Rotation = 0
            end
        end
    end
end

-- FakeLag
local function fakeLag()
    if State.isFakeLagging then
        local delay = Config.FakeLagDelay
        while delay > 0 do
            delay = delay - 0.1
            RunService.RenderStepped:Wait()
        end
    end
end

-- LagFixer
local function lagFixer()
    if State.isLagFixing then
        local speed = Config.LagFixerSpeed
        while speed > 0 do
            speed = speed - 0.1
            RunService.RenderStepped:Wait()
        end
    end
end

-- MaruUI
local function maruUI()
    local HUI = getHUI()
    local dragFrame = Instance.new("Frame")
    dragFrame.Name = "DragFrame"
    dragFrame.Parent = HUI
    dragFrame.Size = UDim2.new(0, 200, 0, 100)
    dragFrame.Position = UDim2.new(0, 0, 0, 0)
    dragFrame.BackgroundTransparency = 1
    local dragText = Instance.new("TextLabel")
    dragText.Name = "DragText"
    dragText.Parent = dragFrame
    dragText.Text = "MayChemXeoCanV2"
    dragText.Size = UDim2.new(0, 200, 0, 20)
    dragText.Position = UDim2.new(0, 0, 0, 0)
    dragText.BackgroundTransparency = 1
    dragText.TextColor3 = Color3.new(1, 1, 1)
    local dragInput = Instance.new("TextButton")
    dragInput.Name = "DragInput"
    dragInput.Parent = HUI
    dragInput.Size = UDim2.new(0, 200, 0, 20)
    dragInput.Position = UDim2.new(0, 0, 0, 20)
    dragInput.BackgroundTransparency = 1
    dragInput.Text = "Drag"
    dragInput.TextColor3 = Color3.new(1, 1, 1)
    dragInput.MouseButton1Down:Connect(function()
        dragFrame:TweenPosition(UDim2.new(0, 0, 0, 0), Enum.EasingStyle.Linear, Enum.EasingDirection.InOut, 0.5, true)
    end)
end

-- Hooks
local function __namecall(func, ...)
    local args = {...}
    if State.isRunning then
        if func.Name == "FireServer" then
            if State.isAutoCombining then
                autoCombo()
            elseif State.isFastSkilling then
                fastSkill()
            end
        elseif func.Name == "FireClient" then
            if State.isSilentAiming then
                silentAim()
            end
        end
    end
    return func(args)
end

local function onPlayerAdded(player)
    Cache.players[player.UserId] = player
end

local function onPlayerRemoved(player)
    Cache.players[player.UserId] = nil
end

local function onToolEquipped(tool)
    if State.isSwitchingTool then
        switchTool()
    end
end

local function onSkillEquipped(skill)
    if State.isFastSkilling then
        fastSkill()
    end
end

local function onStunChanged(stun)
    if State.isStunned then
        stunDetection()
    end
end

local function onBusyChanged(busy)
    if State.isBusy then
        busyDetection()
    end
end

-- Main
local function main()
    State.isRunning = true
    maruUI()
    local hook = hookfunction(game:GetService("ReplicatedStorage").RemoteEvent, __namecall)
    Players.PlayerAdded:Connect(onPlayerAdded)
    Players.PlayerRemoved:Connect(onPlayerRemoved)
    Players.LocalPlayer.CharacterAdded:Connect(onToolEquipped)
    Players.LocalPlayer.CharacterAdded:Connect(onSkillEquipped)
    Players.LocalPlayer.Character:WaitForChild("Stun").Changed:Connect(onStunChanged)
    Players.LocalPlayer.Character:WaitForChild("Busy").Changed:Connect(onBusyChanged)
    while true do
        if State.isRunning then
            silentAim()
            esp()
            tracer()
            fakeLag()
            lagFixer()
        end
        RunService.RenderStepped:Wait()
    end
end

main()
```

Lưu ý rằng code này được viết để chạy trên Roblox, và cần có các module và dịch vụ Roblox để hoạt động đúng.