-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character
local Humanoid = Character:WaitForChild("Humanoid")
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

-- SilentAim Variables
local SilentAimEnabled = true
local SilentAimFOV = 50
local SilentAimSpeed = 10

-- CombatEngine Variables
local CombatEngineEnabled = true
local CombatEngineRange = 20
local CombatEngineSpeed = 5

-- Prediction Math
local function predict_position(target, speed)
    local direction = (target.HumanoidRootPart.Position - HumanoidRootPart.Position).Unit
    local distance = (target.HumanoidRootPart.Position - HumanoidRootPart.Position).Magnitude
    local predicted_position = target.HumanoidRootPart.Position + direction * speed * (distance / 100)
    return predicted_position
end

-- SilentAim Function
local function silent_aim(target)
    if SilentAimEnabled then
        local predicted_position = predict_position(target, SilentAimSpeed)
        local direction = (predicted_position - HumanoidRootPart.Position).Unit
        local rotation = math.atan2(direction.X, direction.Z)
        HumanoidRootPart.CFrame = CFrame.new(HumanoidRootPart.Position, predicted_position)
    end
end

-- CombatEngine Function
local function combat_engine(target)
    if CombatEngineEnabled then
        local distance = (target.HumanoidRootPart.Position - HumanoidRootPart.Position).Magnitude
        if distance <= CombatEngineRange then
            local predicted_position = predict_position(target, CombatEngineSpeed)
            local direction = (predicted_position - HumanoidRootPart.Position).Unit
            local rotation = math.atan2(direction.X, direction.Z)
            HumanoidRootPart.CFrame = CFrame.new(HumanoidRootPart.Position, predicted_position)
            -- Attack logic here
        end
    end
end

-- Main Loop
while true do
    -- Get nearest player
    local nearest_player = nil
    local nearest_distance = math.huge
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer then
            local distance = (player.Character.HumanoidRootPart.Position - HumanoidRootPart.Position).Magnitude
            if distance < nearest_distance then
                nearest_distance = distance
                nearest_player = player
            end
        end
    end

    -- SilentAim
    if nearest_player then
        silent_aim(nearest_player.Character)
    end

    -- CombatEngine
    if nearest_player then
        combat_engine(nearest_player.Character)
    end

    -- Wait for next frame
    RunService.RenderStepped:Wait()
end