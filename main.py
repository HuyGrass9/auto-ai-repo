Here's the complete and optimized script:

-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local HttpService = game:GetService("HttpService")
local Game = game

-- Config
local cfg = {
    save = false,
    fakeLag = 0,
    autoCombo = false,
    silentAim = false,
    visuals = false,
    hold_1 = 0,
    hold_2 = 0,
    hold_3 = 0,
    hold_4 = 0,
    silentAimDirectionalSkills = {"1", "2", "3", "4"},
}

local function loadConfig()
    local configFile = loadstring(game:HttpGet("https://raw.githubusercontent.com/MayChemXeoCan/BloxAPI/master/config.lua"))()
    for k, v in pairs(configFile) do
        cfg[k] = v
    end
end

local function saveConfig()
    local json = HttpService:JSONEncode(cfg)
    writefile("config.json", json)
end

loadConfig()

-- State
local state = {
    tool = 1,
    combo = false,
    stunned = false,
    busy = false,
    nearestEnemy = nil,
    lockedTarget = false,
}

-- Cache
local cache = {
    toolTypes = {},
    tool1 = nil,
    tool2 = nil,
    tool3 = nil,
    tool4 = nil,
    nearestEnemy = nil,
    silentAimTarget = nil,
}

-- Utils
local function tween(value, time, easing)
    local startTime = tick()
    local function update()
        local t = (tick() - startTime) / time
        if t > 1 then
            t = 1
        end
        if easing then
            t = easing(t)
        end
        return value * t
    end
    return update
end

local function makeDraggable(gui)
    gui.InputBegan:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.MouseButton1 then
            gui.InputBegan:Disable()
            gui.InputEnded:Disable()
            gui:TweenPosition(gui.AbsolutePosition, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut, 0.5, true)
        end
    end)
end

local function getPing()
    return Players.LocalPlayer.NetworkStats.RoundTripTime
end

local function distSq(pos1, pos2)
    return (pos1 - pos2).Magnitude ^ 2
end

local function isAlly(player)
    for _, character in pairs(player.Character:GetChildren()) do
        if character:IsA("Model") then
            for _, humanoid in pairs(character:GetChildren()) do
                if humanoid:IsA("Humanoid") and humanoid.Parent == Players.LocalPlayer.Character then
                    return true
                end
            end
        end
    end
    return false
end

-- Combat Engine Module
local function combatEngineModule()
    local function toolDetection()
        local tool1 = Players.LocalPlayer.Backpack:FindFirstChild("Tool1")
        local tool2 = Players.LocalPlayer.Backpack:FindFirstChild("Tool2")
        local tool3 = Players.LocalPlayer.Backpack:FindFirstChild("Tool3")
        local tool4 = Players.LocalPlayer.Backpack:FindFirstChild("Tool4")
        local function checkTool()
            if tool1 and tool1.Equipped then
                state.tool = 1
                cache.toolTypes[1] = "1"
            elseif tool2 and tool2.Equipped then
                state.tool = 2
                cache.toolTypes[2] = "2"
            elseif tool3 and tool3.Equipped then
                state.tool = 3
                cache.toolTypes[3] = "3"
            elseif tool4 and tool4.Equipped then
                state.tool = 4
                cache.toolTypes[4] = "4"
            end
        end
        checkTool()
    end

    local function autoCombo()
        while true do
            toolDetection()
            if cfg.autoCombo then
                state.combo = true
            else
                state.combo = false
            end
            task.wait(0.5)
        end
    end

    local function fastSkill()
        local function checkBusy()
            return state.busy
        end
        local function executeSkill()
            if not checkBusy() then
                state.busy = true
                task.wait(0.5)
                state.busy = false
            end
        end
        executeSkill()
    end

    local function isStunned()
        return state.stunned
    end

    local function checkBusy()
        return state.busy
    end

    local function updateState()
        state.tool = 1
        state.combo = false
        state.stunned = false
        state.busy = false
        state.nearestEnemy = nil
    end

    updateState()
    RunService.RenderStepped:Connect(updateState)
    RunService.RenderStepped:Connect(toolDetection)
    RunService.RenderStepped:Connect(autoCombo)
    RunService.RenderStepped:Connect(fastSkill)
end

-- Silent Aim Module
local function silentAimModule()
    local function __namecall(namecall, ...)
        if namecall == "FireServer" and table.find(cfg.silentAimDirectionalSkills, ...) then
            local args = {...}
            local target = nil
            for _, player in pairs(Players:GetPlayers()) do
                if player ~= Players.LocalPlayer and player.Character and player.Character:FindFirstChild("Humanoid") then
                    local distance = (Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
                    if distance < 500 then
                        target = player
                        break
                    end
                end
            end
            if target then
                args[2] = (target.Character.HumanoidRootPart.Position - Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
                return namecall(unpack(args))
            else
                return namecall(unpack(args))
            end
        elseif namecall == "FireServer" and (table.find({"1", "2", "3", "4"}, ...) or table.find({"shoot", "fire", "cast", "skill"}, ...)) then
            local args = {...}
            local target = nil
            for _, player in pairs(Players:GetPlayers()) do
                if player ~= Players.LocalPlayer and player.Character and player.Character:FindFirstChild("Humanoid") then
                    local distance = (Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
                    if distance < 500 then
                        target = player
                        break
                    end
                end
            end
            if target then
                args[2] = target.Character.HumanoidRootPart.Position
                return namecall(unpack(args))
            else
                return namecall(unpack(args))
            end
        else
            return namecall(...)
        end
    end

    local function getNearestEnemy()
        local nearestEnemy = nil
        local minDistance = math.huge
        for _, player in pairs(Players:GetPlayers()) do
            if player ~= Players.LocalPlayer and player.Character and player.Character:FindFirstChild("Humanoid") then
                local distance = (Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
                if distance < minDistance then
                    minDistance = distance
                    nearestEnemy = player
                end
            end
        end
        return nearestEnemy
    end

    local function getEnemyCFrame()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            return nearestEnemy.Character.HumanoidRootPart.CFrame
        else
            return nil
        end
    end

    local function getSilentAimTarget()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            return nearestEnemy.Character.HumanoidRootPart.Position
        else
            return nil
        end
    end
end

-- Visuals Module
local function visualsModule()
    local function drawAim(part)
        local function updateAim()
            local aimPos = part.Position + part.CFrame.LookVector * 10
            local line = Instance.new("Part")
            line.Anchored = true
            line.Position = aimPos
            line.Size = Vector3.new(1, 0.1, 1)
            line.BrickColor = BrickColor.new("Bright blue")
            line.Parent = game.Workspace
            task.wait(0.1)
            line:Destroy()
        end
        updateAim()
        RunService.RenderStepped:Connect(updateAim)
    end

    local function drawEsp(part)
        local function updateEsp()
            local name = part.Name
            local health = part.Health
            local level = part.Level
            local distance = (part.Position - Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude
            local heldWeapon = part:GetChildren()[4].Name
            local gui = Instance.new("BillboardGui")
            gui.Parent = part
            gui.ResetOnSpawn = false
            gui.Name = "EspGui"
            local label = Instance.new("TextLabel")
            label.Text = name
            label.Size = UDim2.new(0, 50, 0, 20)
            label.Position = UDim2.new(0, 0, 0, 0)
            label.Parent = gui
            local healthBar = Instance.new("Frame")
            healthBar.Size =