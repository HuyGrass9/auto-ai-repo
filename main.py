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
            -- Example: Tool 1 combo
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1"))
            -- task.wait(0.5)
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2"))
        elseif tool == 2 then
            -- Tool 2 combo
            -- Example: Tool 2 combo
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2"))
            -- task.wait(0.5)
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
        elseif tool == 3 then
            -- Tool 3 combo
            -- Example: Tool 3 combo
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
            -- task.wait(0.5)
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
        elseif tool == 4 then
            -- Tool 4 combo
            -- Example: Tool 4 combo
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
        end
    end
    local function isStunned()
        return game.Players.LocalPlayer.Character.HumanoidState:GetState() == Enum.HumanoidStateType.Dizzy
    end
    local function checkBusy()
        return game.Players.LocalPlayer.Character.HumanoidState:GetState() == Enum.HumanoidStateType.Jumping or
               game.Players.LocalPlayer.Character.HumanoidState:GetState() == Enum.HumanoidStateType.Landed or
               game.Players.LocalPlayer.Character.HumanoidState:GetState() == Enum.HumanoidStateType.Falling
    end
    local function combo()
        while true do
            if not isStunned() and not checkBusy() then
                executeCombo()
            end
            task.wait(cfg.comboDelay or 0.5)
        end
    end
    task.spawn(combo)
end

--- Silent Aim Section ---
local function silentAim()
    local function getNearestEnemy()
        local nearestEnemy = nil
        local minDistance = math.huge
        for _, player in pairs(game.Players:GetPlayers()) do
            if player ~= game.Players.LocalPlayer and player.Character then
                local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
                if distance < minDistance then
                    minDistance = distance
                    nearestEnemy = player
                end
            end
        end
        return nearestEnemy
    end
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" and args[1] == "Attack" then
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                local direction = (nearestEnemy.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
                args[2] = direction * 100
                return namecall(unpack(args))
            end
        end
        return namecall(unpack(args))
    end
    local function overrideVector3(namecall)
        local args = {...}
        if namecall == "Vector3" then
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return nearestEnemy.Character.HumanoidRootPart.Position
            end
        end
        return namecall(unpack(args))
    end
    local function overrideCFrame(namecall)
        local args = {...}
        if namecall == "CFrame" then
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return nearestEnemy.Character.HumanoidRootPart.CFrame
            end
        end
        return namecall(unpack(args))
    end
    local function silentAimLoop()
        while true do
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                local direction = (nearestEnemy.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
                local fireArgs = {Attack = direction * 100}
                fireServer("FireServer", unpack(fireArgs))
            end
            task.wait(cfg.silentAimDelay or 0.5)
        end
    end
    local function hook()
        local oldFireServer = game.ReplicatedStorage.RemoteEvent.FireServer.__index.FireServer
        game.ReplicatedStorage.RemoteEvent.FireServer.__index.FireServer = fireServer
        local oldVector3 = Vector3.__index.Vector3
        Vector3.__index.Vector3 = overrideVector3
        local oldCFrame = CFrame.__index.CFrame
        CFrame.__index.CFrame = overrideCFrame
    end
    hook()
    task.spawn(silentAimLoop)
end

--- Visuals Section ---
local function visuals()
    local function billboardGui()
        local billboard = Instance.new("BillboardGui")
        billboard.Parent = game.Players.LocalPlayer.Character
        billboard.Adornee = game.Players.LocalPlayer.Character.HumanoidRootPart
        billboard.StudsOffset = Vector3.new(0, 2, 0)
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboard
        textLabel.BackgroundTransparency = 1
        textLabel.Text = ""
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.FontSize = Enum.FontSize.Size24
        local function updateTextLabel()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - nearestEnemy.Character.HumanoidRootPart.Position).Magnitude
                local name = nearestEnemy.Name
                local health = nearestEnemy.Character.Humanoid.Health
                local level = nearestEnemy.Character.Humanoid.MaxHealth
                local weapon = nearestEnemy.Character:FindFirstChild("Tool")
                if weapon then
                    textLabel.Text = name .. " (" .. health .. "/" .. level .. ") - " .. weapon.Name
                else
                    textLabel.Text = name .. " (" .. health .. "/" .. level .. ")"
                end
            else
                textLabel.Text = ""
            end
        end
        updateTextLabel()
        task.spawn(function()
            while true do
                updateTextLabel()
                task.wait(cfg.visualsDelay or 0.5)
            end
        end)
    end
    local function tracers()
        local tracer = Instance.new("Part")
        tracer.Parent = game.Players.LocalPlayer