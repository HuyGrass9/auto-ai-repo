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
local CombatEngineRange = 50
local CombatEngineSpeed = 10

-- Prediction Math
local function predict_position(target)
    local velocity = target.HumanoidRootPart.Velocity
    local direction = (target.HumanoidRootPart.Position - HumanoidRootPart.Position).Unit
    local distance = (target.HumanoidRootPart.Position - HumanoidRootPart.Position).Magnitude
    local travel_time = distance / SilentAimSpeed
    local predicted_position = target.HumanoidRootPart.Position + velocity * travel_time
    return predicted_position
end

-- SilentAim Function
local function silent_aim(target)
    if SilentAimEnabled then
        local predicted_position = predict_position(target)
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
            silent_aim(target)
            -- Attack logic here
        end
    end
end

-- Loop
while wait() do
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer then
            local character = player.Character
            if character then
                local humanoid = character:FindFirstChild("Humanoid")
                if humanoid then
                    local humanoid_root_part = character:FindFirstChild("HumanoidRootPart")
                    if humanoid_root_part then
                        combat_engine(humanoid_root_part)
                    end
                end
            end
        end
    end
end