Here's the completed script with the requested features:


-- MayChemXeoCan_V2.lua

--- Configuration Section ---
local configFile = loadstring(game:HttpGet("https://raw.githubusercontent.com/MayChemXeoCan/BloxAPI/master/config.lua"))()
local cfg = {}
for k, v in pairs(configFile) do
    cfg[k] = v
end

--- Key Bind Section ---
local keyBinds = {
    one = Enum.KeyCode.D1,
    two = Enum.KeyCode.D2,
    three = Enum.KeyCode.D3,
    four = Enum.KeyCode.D4,
    exit = Enum.KeyCode.Insert,
    fight = Enum.KeyCode.F,
    tool1 = Enum.KeyCode.E,
    tool2 = Enum.KeyCode.R,
    tool3 = Enum.KeyCode.T,
    tool4 = Enum.KeyCode.Y,
}

--- UI Section ---
local gethui = loadstring(game:HttpGet("https://raw.githubusercontent.com/MayChemXeoCan/BloxAPI/master/UI.lua"))()
local ui = gethui("MayChemXeoCan V2")
local tab = ui:Tab("Combat")
local combatTab = tab:Tab("Tool Detection")
local silentAimTab = tab:Tab("Silent Aim")
local visualsTab = tab:Tab("Visuals")
local settingsTab = tab:Tab("Settings")

local function saveConfig()
    local file = game:GetService("Fileservice").Game:GetService("DataStoreService"):GetDataStore("MCXC_V2")
    local data = {}
    for k, v in pairs(cfg) do
        data[k] = v
    end
    file:SetAsync("MCXC_V2", data)
end

local function loadConfig()
    local file = game:GetService("Fileservice").Game:GetService("DataStoreService"):GetDataStore("MCXC_V2")
    local data = file:GetAsync("MCXC_V2")
    if data then
        cfg = data
    end
end

loadConfig()

--- Combat Engine Section ---
local function toolDetection()
    local tool1 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1")
    local tool2 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2")
    local tool3 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3")
    local tool4 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4")
    local tool = 1
    local function checkTool()
        if tool1 and tool1.Equipped then
            tool = 1
        elseif tool2 and tool2.Equipped then
            tool = 2
        elseif tool3 and tool3.Equipped then
            tool = 3
        elseif tool4 and tool4.Equipped then
            tool = 4
        end
    end
    checkTool()
    local function executeCombo()
        if tool == 1 then
            -- Tool 1 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
        elseif tool == 2 then
            -- Tool 2 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
        elseif tool == 3 then
            -- Tool 3 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
        elseif tool == 4 then
            -- Tool 4 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
        end
    end
    local function checkBusy()
        return game.Players.LocalPlayer.Character.Humanoid.Health > 0 and not game.Players.LocalPlayer.Character.Humanoid.IsStunned
    end
    local function isStunned()
        return game.Players.LocalPlayer.Character.Humanoid.IsStunned
    end
    local function combo()
        while true do
            if checkBusy() then
                executeCombo()
                task.wait(0.5)
            else
                task.wait(0.5)
            end
        end
    end
    combo()
end

--- Silent Aim Section ---
local function silentAim()
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" and args[1] == "GetNearestEnemy" then
            local nearestEnemy = nil
            local minDistance = math.huge
            for _, player in pairs(game.Players:GetPlayers()) do
                if player ~= game.Players.LocalPlayer and player.Character and player.Character:FindFirstChild("Humanoid") then
                    local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
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
        for _, player in pairs(game.Players:GetPlayers()) do
            if player ~= game.Players.LocalPlayer and player.Character and player.Character:FindFirstChild("Humanoid") then
                local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
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
            return game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
        end
    end
    local function getEnemyPosition()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            return nearestEnemy.Character.HumanoidRootPart.Position
        else
            return game.Players.LocalPlayer.Character.HumanoidRootPart.Position
        end
    end
    local function overrideVector3(namecall)
        local args = {...}
        if namecall == "GetNearestEnemy" then
            args[2] = getEnemyPosition()
            return namecall(unpack(args))
        else
            return namecall(unpack(args))
        end
    end
    local function overrideCFrame(namecall)
        local args = {...}
        if namecall == "GetNearestEnemy" then
            args[2] = getEnemyCFrame()
            return namecall(unpack(args))
        else
            return namecall(unpack(args))
        end
    end
    local function hook(namecall)
        return fireServer(namecall)
    end
    local function hookVector3(namecall)
        return overrideVector3(namecall)
    end
    local function hookCFrame(namecall)
        return overrideCFrame(namecall)
    end
    local function init()
        game:GetService("RunService").RenderStepped:Connect(hook)
        game:GetService("RunService").RenderStepped:Connect(hookVector3)
        game:GetService("RunService").RenderStepped:Connect(hookCFrame)
    end
    init()
end

--- Visuals Section ---
local function visuals()
    local function billboardGui()
        local billboard = Instance.new("BillboardGui")
        billboard.Parent = game.Players.LocalPlayer.Character
        billboard.Adornee = game.Players.LocalPlayer.Character.HumanoidRootPart
        billboard.StudsOffset = Vector3.new(0, 2, 0)
        billboard.AlwaysOnTop = true
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboard
        textLabel.BackgroundTransparency = 1
        textLabel.Text = "Name"
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.Size = UDim2.new(0, 100, 0, 20)
        local function updateTextLabel()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                textLabel.Text = nearestEnemy.Name
            else
                textLabel.Text = "No Enemy"
            end
        end
        updateTextLabel()
        game:GetService("RunService").RenderStepped:Connect(updateTextLabel)
    end
    local function tracers()
        local tracer = Instance.new("Part")
        tracer.Parent = game.Players.LocalPlayer.Character
        tracer.Anchored = true
        tracer.CanCollide = false
        tracer.Transparency = 0.5
        local function updateTracer()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                tracer.Position = nearestEnemy.Character.HumanoidRootPart.Position
            else
                tracer.Position = game.Players.LocalPlayer.Character.HumanoidRootPart.Position
            end
        end
        updateTracer()
        game:GetService("RunService").RenderStepped:Connect