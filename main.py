-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character
local Humanoid = Character:WaitForChild("Humanoid")
local Mouse = LocalPlayer:GetMouse()

-- SilentAim Variables
local SilentAimEnabled = true
local SilentAimFOV = 50
local SilentAimSpeed = 10

-- CombatEngine Variables
local CombatEngineEnabled = true
local CombatEngineRange = 100
local CombatEngineSpeed = 5

-- Prediction Math
local function predict_position(target, speed)
    local direction = (target.Position - Character.HumanoidRootPart.Position).Unit
    local distance = (target.Position - Character.HumanoidRootPart.Position).Magnitude
    local travel_time = distance / speed
    local predicted_position = target.Position + (target.Velocity * travel_time)
    return predicted_position
end

-- SilentAim Function
local function silent_aim(target)
    if SilentAimEnabled then
        local predicted_position = predict_position(target, SilentAimSpeed)
        local direction = (predicted_position - Character.HumanoidRootPart.Position).Unit
        local rotation = math.atan2(-direction.Z, direction.X)
        Mouse.Rotate = Vector2.new(rotation, 0)
    end
end

-- CombatEngine Function
local function combat_engine(target)
    if CombatEngineEnabled then
        local predicted_position = predict_position(target, CombatEngineSpeed)
        local distance = (predicted_position - Character.HumanoidRootPart.Position).Magnitude
        if distance <= CombatEngineRange then
            -- Attack target
            local attack = Instance.new("RemoteEvent")
            attack.Name = "Attack"
            attack.Parent = Character
            attack:FireServer(target)
        end
    end
end

-- Main Loop
game:GetService("RunService").RenderStepped:Connect(function()
    -- Get nearest target
    local nearest_target = nil
    local nearest_distance = math.huge
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local distance = (player.Character.HumanoidRootPart.Position - Character.HumanoidRootPart.Position).Magnitude
            if distance < nearest_distance then
                nearest_distance = distance
                nearest_target = player.Character
            end
        end
    end

    -- SilentAim
    if nearest_target then
        silent_aim(nearest_target.HumanoidRootPart)
    end

    -- CombatEngine
    if nearest_target then
        combat_engine(nearest_target.HumanoidRootPart)
    end
end)

-- Update prediction math
local function update_prediction_math()
    -- Update SilentAim speed
    SilentAimSpeed = 15

    -- Update CombatEngine speed
    CombatEngineSpeed = 10
end

-- Update script
update_prediction_math()