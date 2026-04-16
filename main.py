-- MayChemXeoCan V2
-- Auto Bounty Script

-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local VirtualInputManager = game:GetService("VirtualInputManager")

-- Variables
local LocalPlayer = Players.LocalPlayer
local Character = LocalPlayer.Character
local Humanoid = Character:WaitForChild("Humanoid")
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")
local BountyTarget = nil
local BountyTargetHRP = nil
local CurrentSkill = "Z"
local CurrentSlot = 1
local Ping = 0
local LastPing = 0
local DynamicDelay = 0

-- Functions
local function GetBountyTarget()
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
            local distance = (HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
            if distance <= 50 then
                return player
            end
        end
    end
    return nil
end

local function GetPredictedPosition(hrp, velocity, time)
    return hrp.Position + velocity * time
end

local function SmoothTween(part, targetPosition, time)
    local startPosition = part.Position
    local elapsed = 0
    while elapsed < time do
        local newPosition = startPosition + (targetPosition - startPosition) * (elapsed / time)
        part.CFrame = CFrame.new(newPosition)
        elapsed = elapsed + 0.01
        task.wait(0.01)
    end
end

local function MaintainDistance(targetHrp)
    local distance = (HumanoidRootPart.Position - targetHrp.Position).Magnitude
    if distance > 10 then
        local direction = (targetHrp.Position - HumanoidRootPart.Position).Unit
        SmoothTween(HumanoidRootPart, HumanoidRootPart.Position + direction * (distance - 10), 0.5)
    elseif distance < 5 then
        local direction = (HumanoidRootPart.Position - targetHrp.Position).Unit
        SmoothTween(HumanoidRootPart, HumanoidRootPart.Position + direction * (5 - distance), 0.5)
    end
end

local function UpdatePing()
    LastPing = Ping
    Ping = game:GetService("Stats").Network.ServerStatsItem["DataPing"]:GetValue()
    DynamicDelay = math.max(0.05, Ping / 1000)
end

local function SelfCorrection(skill, targetHrp)
    local predictedPosition = GetPredictedPosition(targetHrp, targetHrp.Velocity, DynamicDelay)
    local actualPosition = targetHrp.Position
    local distance = (predictedPosition - actualPosition).Magnitude
    if distance > 1 then
        -- Adjust prediction
        print("Self-Correction: Adjusting prediction for " .. skill)
    end
end

-- Main Loop
while task.wait(DynamicDelay) do
    -- Update Ping
    UpdatePing()

    -- Get Bounty Target
    if not BountyTarget or not BountyTarget.Character or not BountyTarget.Character:FindFirstChild("HumanoidRootPart") then
        BountyTarget = GetBountyTarget()
        if BountyTarget then
            BountyTargetHRP = BountyTarget.Character:WaitForChild("HumanoidRootPart")
        end
    end

    -- Maintain Distance
    if BountyTargetHRP then
        MaintainDistance(BountyTargetHRP)
    end

    -- Combat
    if BountyTargetHRP then
        -- Predict Target Position
        local predictedPosition = GetPredictedPosition(BountyTargetHRP, BountyTargetHRP.Velocity, DynamicDelay)

        -- Skill Cycle
        if CurrentSkill == "Z" then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Z)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Z)
            CurrentSkill = "X"
        elseif CurrentSkill == "X" then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.X)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.X)
            CurrentSkill = "C"
        elseif CurrentSkill == "C" then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.C)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.C)
            CurrentSkill = "V"
        elseif CurrentSkill == "V" then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.V)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.V)
            CurrentSkill = "Z"
        end

        -- Slot Swapping
        if CurrentSlot == 1 then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.One)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.One)
            CurrentSlot = 2
        elseif CurrentSlot == 2 then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Two)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Two)
            CurrentSlot = 3
        elseif CurrentSlot == 3 then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Three)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Three)
            CurrentSlot = 4
        elseif CurrentSlot == 4 then
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Four)
            task.wait(DynamicDelay)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Four)
            CurrentSlot = 1
        end

        -- Self-Correction
        SelfCorrection(CurrentSkill, BountyTargetHRP)
    end
end