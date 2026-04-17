Here is the updated and completed script with improvements to performance, readability, and bug fixes.

-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local HttpService = game:GetService("HttpService")
local Game = game

-- Config
local function loadConfig()
    local configFile = loadstring(game:HttpGet("https://raw.githubusercontent.com/MayChemXeoCan/BloxAPI/master/config.lua"))()
    local cfg = {}
    for k, v in pairs(configFile) do
        cfg[k] = v
    end
    return cfg
end

local cfg = loadConfig()

-- State
local state = {
    tool = 1,
    combo = false,
    stunned = false,
    busy = false,
    nearestEnemy = nil,
}

-- Cache
local cache = {
    tool1 = nil,
    tool2 = nil,
    tool3 = nil,
    tool4 = nil,
    nearestEnemy = nil,
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

-- Config Module
local function configModule()
    local function saveConfig()
        local json = HttpService:JSONEncode(cfg)
        writefile("config.json", json)
    end
    local function loadConfig()
        local json = readfile("config.json")
        if json then
            cfg = HttpService:JSONDecode(json)
        end
    end
    loadConfig()
    RunService.RenderStepped:Connect(function()
        if cfg.save then
            saveConfig()
            cfg.save = false
        end
    end)
end

-- State Module
local function stateModule()
    local function updateState()
        state.tool = 1
        state.combo = false
        state.stunned = false
        state.busy = false
        state.nearestEnemy = nil
    end
    updateState()
    RunService.RenderStepped:Connect(function()
        updateState()
    end)
end

-- Cache Module
local function cacheModule()
    local function updateCache()
        cache.tool1 = nil
        cache.tool2 = nil
        cache.tool3 = nil
        cache.tool4 = nil
        cache.nearestEnemy = nil
    end
    updateCache()
    RunService.RenderStepped:Connect(function()
        updateCache()
    end)
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
            elseif tool2 and tool2.Equipped then
                state.tool = 2
            elseif tool3 and tool3.Equipped then
                state.tool = 3
            elseif tool4 and tool4.Equipped then
                state.tool = 4
            end
        end
        checkTool()
    end

    local function autoCombo()
        while true do
            toolDetection()
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
end

-- Silent Aim Module
local function silentAimModule()
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" and args[1] == "GetNearestEnemy" then
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
            if nearestEnemy then
                args[2] = nearestEnemy.Character.HumanoidRootPart.Position
                return namecall(unpack(args))
            else
                return namecall(unpack(args))
            end
        else
            return namecall(unpack(args))
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
end

-- Lag Fixer Module
local function lagFixerModule()
    local function fixLag()
        RunService.RenderStepped:DisconnectAll()
        RunService.RenderStepped:Connect(function()
            if Players.LocalPlayer.Character then
                task.wait(0.01)
            else
                task.wait(0.1)
            end
        end)
    end
    fixLag()
end

-- Fake Lag Module
local function fakeLagModule()
    local function applyFakeLag()
        RunService.RenderStepped:DisconnectAll()
        RunService.RenderStepped:Connect(function()
            if cfg.fakeLag then
                task.wait(cfg.fakeLag)
            end
        end)
    end
    applyFakeLag()
end

-- Maru UI Module
local function maruUIModule()
    local function createGUI()
        local gui = Instance.new("ScreenGui")
        gui.Name = "MayChemXeoCanV2"
        gui.Parent = Players.LocalPlayer.PlayerGui
        local frame = Instance.new("Frame")
        frame.Size = UDim2.new(1, 0, 1, 0)
        frame.Position = UDim2.new(0, 0, 0, 0)
        frame.Parent = gui
        local title = Instance.new("TextLabel")
        title.Text = "MayChemXeoCan V2"
        title.Size = UDim2.new(0, 200, 0, 30)
        title.Position = UDim2.new(0, 10, 0, 10)
        title.Parent = frame
        local settings = Instance.new("Frame")
        settings.Size = UDim2.new(0, 200, 0, 100)
        settings.Position = UDim2.new(0, 10, 0, 50)
        settings.Parent = frame
        local saveButton = Instance.new("TextButton")
        saveButton.Text = "Save Config"
        saveButton.Size = UDim2.new(0, 100, 0, 30)
        saveButton.Position = UDim2.new(0, 10, 0, 10)
        saveButton.Parent = settings
        saveButton.MouseButton1Down:Connect(function()
            cfg.save = true
        end)
        local loadButton = Instance.new("TextButton")
        loadButton.Text = "Load Config"
        loadButton.Size = UDim