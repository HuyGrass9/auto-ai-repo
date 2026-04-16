-- MayChemXeoCan V2
-- SilentAim and CombatEngine

-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")
local Mouse = LocalPlayer:GetMouse()

-- Settings
local SilentAimEnabled = true
local CombatEngineEnabled = true
local Prediction = 0.15 -- Adjust this value based on your internet connection
local AimFOV = 50 -- Field of view for aiming
local AimSpeed = 10 -- Speed at which the aim moves
local CombatDistance = 10 -- Maximum distance for combat

-- Functions
local function GetClosestEnemy()
    local closestEnemy = nil
    local closestDistance = math.huge

    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local enemyHumanoidRootPart = player.Character:FindFirstChild("HumanoidRootPart")
            if enemyHumanoidRootPart then
                local distance = (HumanoidRootPart.Position - enemyHumanoidRootPart.Position).Magnitude
                if distance < closestDistance then
                    closestEnemy = player
                    closestDistance = distance
                end
            end
        end
    end

    return closestEnemy
end

local function GetAimDirection()
    local mousePosition = Mouse.Hit.Position
    local direction = (mousePosition - HumanoidRootPart.Position).Unit
    return direction
end

local function GetPredictedPosition(enemyHumanoidRootPart)
    local velocity = enemyHumanoidRootPart.Velocity
    local predictedPosition = enemyHumanoidRootPart.Position + velocity * Prediction
    return predictedPosition
end

-- SilentAim
local function SilentAim()
    if SilentAimEnabled then
        local closestEnemy = GetClosestEnemy()
        if closestEnemy then
            local enemyHumanoidRootPart = closestEnemy.Character:FindFirstChild("HumanoidRootPart")
            if enemyHumanoidRootPart then
                local predictedPosition = GetPredictedPosition(enemyHumanoidRootPart)
                local direction = (predictedPosition - HumanoidRootPart.Position).Unit
                local angle = math.atan2(direction.X, direction.Z)

                -- Move the aim to the predicted position
                local aimDirection = GetAimDirection()
                local aimAngle = math.atan2(aimDirection.X, aimDirection.Z)
                local angleDifference = angle - aimAngle
                if math.abs(angleDifference) > AimFOV / 2 then
                    -- Move the aim to the predicted position
                    local newAimDirection = Vector3.new(math.cos(angle), 0, math.sin(angle))
                    local newAimPosition = HumanoidRootPart.Position + newAimDirection * 1000
                    Mouse.Hit = RaycastParams.new({ Origin = HumanoidRootPart.Position, Direction = newAimDirection })
                end
            end
        end
    end
end

-- CombatEngine
local function CombatEngine()
    if CombatEngineEnabled then
        local closestEnemy = GetClosestEnemy()
        if closestEnemy then
            local enemyHumanoidRootPart = closestEnemy.Character:FindFirstChild("HumanoidRootPart")
            if enemyHumanoidRootPart then
                local distance = (HumanoidRootPart.Position - enemyHumanoidRootPart.Position).Magnitude
                if distance <= CombatDistance then
                    -- Attack the enemy
                    local tool = Character:FindFirstChild("Tool")
                    if tool then
                        local animation = tool:FindFirstChild("Animation")
                        if animation then
                            animation:Play()
                        end
                    end
                end
            end
        end
    end
end

-- Main Loop
RunService.RenderStepped:Connect(function()
    SilentAim()
    CombatEngine()
end)

-- User Input
UserInputService.InputBegan:Connect(function(input)
    if input.KeyCode == Enum.KeyCode.LeftControl then
        SilentAimEnabled = not SilentAimEnabled
    elseif input.KeyCode == Enum.KeyCode.LeftShift then
        CombatEngineEnabled = not CombatEngineEnabled
    end
end)