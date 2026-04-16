-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character or LocalPlayer.CharacterAdded:Wait()
local Humanoid = Character:WaitForChild("Humanoid")
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

-- SilentAim Variables
local SilentAimEnabled = true
local SilentAimFOV = 360
local SilentAimSpeed = 10

-- CombatEngine Variables
local CombatEngineEnabled = true
local CombatEngineRange = 10
local CombatEngineSpeed = 0.1

-- Prediction Math
local function predict_position(target)
    local velocity = target.Velocity
    local position = target.Position
    local time = (position - HumanoidRootPart.Position).Magnitude / CombatEngineSpeed
    local predicted_position = position + velocity * time
    return predicted_position
end

-- SilentAim Function
local function silent_aim(target)
    if SilentAimEnabled then
        local direction = (target.Position - HumanoidRootPart.Position).Unit
        local rotation = math.atan2(-direction.Z, direction.X)
        local yaw = math.deg(rotation)
        local pitch = math.deg(math.asin(direction.Y))
        HumanoidRootPart.CFrame = CFrame.new(HumanoidRootPart.Position, Vector3.new(math.cos(math.rad(yaw)), math.sin(math.rad(pitch)), -math.sin(math.rad(yaw))))
    end
end

-- CombatEngine Function
local function combat_engine(target)
    if CombatEngineEnabled then
        local predicted_position = predict_position(target)
        local distance = (predicted_position - HumanoidRootPart.Position).Magnitude
        if distance <= CombatEngineRange then
            silent_aim(target)
            -- Attack logic here
        end
    end
end

-- Loop
while true do
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local target = player.Character:FindFirstChild("HumanoidRootPart")
            if target then
                combat_engine(target)
            end
        end
    end
    RunService.RenderStepped:Wait()
end