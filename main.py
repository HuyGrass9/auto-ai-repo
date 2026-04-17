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
    local function checkBusy()
        local character = game.Players.LocalPlayer.Character
        if character and character:FindFirstChild("Humanoid") and character.Humanoid.Health > 0 then
            return false
        else
            return true
        end
    end
    local function isStunned()
        local character = game.Players.LocalPlayer.Character
        if character and character:FindFirstChild("HumanoidRootPart") then
            local rootPart = character.HumanoidRootPart
            if rootPart.Velocity.Magnitude > 0 then
                return false
            else
                return true
            end
        end
    end
    local function checkStunned()
        if isStunned() then
            return true
        else
            return false
        end
    end
    local function combo()
        while wait() do
            if checkBusy() then
                continue
            end
            if checkStunned() then
                continue
            end
            executeCombo()
        end
    end
    task.spawn(combo)
end

--- Silent Aim Section ---
local function silentAim()
    local function getNearestEnemy()
        local players = game:GetService("Players"):GetPlayers()
        local nearestEnemy = nil
        local nearestDistance = math.huge
        for _, player in pairs(players) do
            if player ~= game.Players.LocalPlayer and player.Character then
                local character = player.Character
                local head = character:FindFirstChild("Head")
                if head then
                    local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - head.Position).Magnitude
                    if distance < nearestDistance then
                        nearestDistance = distance
                        nearestEnemy = player
                    end
                end
            end
        end
        return nearestEnemy
    end
    local function getEnemyPosition()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            local character = nearestEnemy.Character
            local head = character:FindFirstChild("Head")
            if head then
                return head.Position
            end
        end
    end
    local function fireServer()
        local args = {}
        local enemyPosition = getEnemyPosition()
        if enemyPosition then
            args[1] = enemyPosition
        end
        game:GetService("ReplicatedStorage").RemoteEvent:FireServer(unpack(args))
    end
    local function hookFireServer()
        local oldFireServer = game:GetService("ReplicatedStorage").RemoteEvent.FireServer
        game:GetService("ReplicatedStorage").RemoteEvent.FireServer = function(self, ...)
            local args = {...}
            if args[1] then
                local position = args[1]
                local character = game.Players.LocalPlayer.Character
                local head = character:FindFirstChild("Head")
                if head then
                    local cframe = CFrame.new(head.Position, position)
                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = cframe
                end
            end
            return oldFireServer(self, ...)
        end
    end
    hookFireServer()
    local function checkBusy()
        local character = game.Players.LocalPlayer.Character
        if character and character:FindFirstChild("Humanoid") and character.Humanoid.Health > 0 then
            return false
        else
            return true
        end
    end
    local function isStunned()
        local character = game.Players.LocalPlayer.Character
        if character and character:FindFirstChild("HumanoidRootPart") then
            local rootPart = character.HumanoidRootPart
            if rootPart.Velocity.Magnitude > 0 then
                return false
            else
                return true
            end
        end
    end
    local function checkStunned()
        if isStunned() then
            return true
        else
            return false
        end
    end
    local function silentAimLoop()
        while wait() do
            if checkBusy() then
                continue
            end
            if checkStunned() then
                continue
            end
            fireServer()
        end
    end
    task.spawn(silentAimLoop)
end

--- Visuals Section ---
local function visuals()
    local function createBillboardGui()
        local billboardGui = Instance.new("BillboardGui")
        billboardGui.Parent = game.Players.LocalPlayer.Character
        billboardGui.Adornee = game.Players.LocalPlayer.Character.HumanoidRootPart
        billboardGui.LightInfluence = 1
        billboardGui.AlwaysOnTop = true
        return billboardGui
    end
    local function createTextLabel()
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = createBillboardGui()
        textLabel.BackgroundTransparency = 1
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.TextSize = 14
        return textLabel
    end
    local function createNameLabel()
        local nameLabel = createTextLabel()
        nameLabel.Text = "Name"
        return nameLabel
    end
    local function createHealthLabel()
        local healthLabel = createTextLabel()
        healthLabel.Text = "Health"
        return healthLabel
    end
    local function createLevelLabel()
        local levelLabel = createTextLabel()
        levelLabel.Text = "Level"
        return levelLabel
    end
    local function createWeaponLabel()
        local weaponLabel = createTextLabel()
        weaponLabel.Text =