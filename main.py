-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character
local Humanoid = Character:WaitForChild("Humanoid")
local Mouse = LocalPlayer:GetMouse()

-- Silent Aim
local SilentAimSettings = {
    Prediction = 0.15,
    FOV = 50,
    Smoothness = 5,
}

-- Combat Engine
local CombatEngineSettings = {
    AttackSpeed = 0.1,
    AttackRange = 10,
    Damage = 100,
}

-- Functions
local function GetClosestEnemy()
    local closestEnemy = nil
    local closestDistance = math.huge

    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local distance = (Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
            if distance < closestDistance then
                closestEnemy = player
                closestDistance = distance
            end
        end
    end

    return closestEnemy
end

local function GetPrediction(enemy)
    local prediction = SilentAimSettings.Prediction
    local velocity = enemy.Character.HumanoidRootPart.Velocity
    local direction = (enemy.Character.HumanoidRootPart.Position - Character.HumanoidRootPart.Position).Unit
    local predictedPosition = enemy.Character.HumanoidRootPart.Position + velocity * prediction

    return predictedPosition
end

local function IsInFOV(position)
    local fov = SilentAimSettings.FOV
    local direction = (position - Character.HumanoidRootPart.Position).Unit
    local angle = math.acos(direction:Dot(Mouse.Unit))

    return angle <= math.rad(fov / 2)
end

-- Main Loop
RunService.RenderStepped:Connect(function()
    local closestEnemy = GetClosestEnemy()
    if closestEnemy and closestEnemy.Character then
        local predictedPosition = GetPrediction(closestEnemy)
        if IsInFOV(predictedPosition) then
            -- Aim at predicted position
            Mouse.Target = predictedPosition

            -- Attack if in range
            if (Character.HumanoidRootPart.Position - predictedPosition).Magnitude <= CombatEngineSettings.AttackRange then
                -- Attack logic here
            end
        end
    end
end)

-- Optimization
local function OptimizePrediction()
    local prediction = SilentAimSettings.Prediction
    local velocity = Character.HumanoidRootPart.Velocity
    local direction = (Character.HumanoidRootPart.Position - Mouse.Target).Unit
    local optimizedPrediction = prediction + (velocity.Magnitude / 100) * (direction:Dot(velocity.Unit))

    return optimizedPrediction
end

-- Update prediction math
SilentAimSettings.Prediction = OptimizePrediction()