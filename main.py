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
        return game.Players.LocalPlayer.Character.HumanoidState == Enum.HumanoidStateType.Dazed
    end

    local function checkBusy()
        return game.Players.LocalPlayer.Character.HumanoidState == Enum.HumanoidStateType.Jumping or
               game.Players.LocalPlayer.Character.HumanoidState == Enum.HumanoidStateType.Freefall or
               game.Players.LocalPlayer.Character.HumanoidState == Enum.HumanoidStateType.Running or
               game.Players.LocalPlayer.Character.HumanoidState == Enum.HumanoidStateType.Swimming
    end

    local function combo()
        while wait() do
            if not isStunned() and not checkBusy() then
                executeCombo()
            end
        end
    end

    task.spawn(combo)
end

local function silentAim()
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" then
            local player = game.Players:GetPlayerFromCharacter(args[1])
            if player then
                local target = player.Character
                if target then
                    local humanoid = target:FindFirstChild("Humanoid")
                    if humanoid then
                        local head = humanoid.Head
                        if head then
                            local position = head.Position
                            local direction = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - position).Unit
                            local firePosition = position + direction * 10
                            args[1] = firePosition
                            return namecall(unpack(args))
                        end
                    end
                end
            end
        end
        return namecall(unpack(args))
    end

    local function getNearestEnemy()
        local function getDistance(player)
            local position = player.Character.HumanoidRootPart.Position
            local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - position).Magnitude
            return distance
        end

        local function getNearest()
            local nearest = nil
            local minDistance = math.huge
            for _, player in pairs(game.Players:GetPlayers()) do
                if player ~= game.Players.LocalPlayer and player.Character then
                    local distance = getDistance(player)
                    if distance < minDistance then
                        minDistance = distance
                        nearest = player
                    end
                end
            end
            return nearest
        end

        local nearest = getNearest()
        if nearest then
            local position = nearest.Character.HumanoidRootPart.Position
            local direction = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - position).Unit
            local firePosition = position + direction * 10
            return firePosition
        end
    end

    local function __namecall(func, ...)
        local args = {...}
        if func == "FireServer" then
            local firePosition = getNearestEnemy()
            if firePosition then
                args[1] = firePosition
            end
        end
        return func(unpack(args))
    end

    getgenv().fireServer = __namecall
end

--- Silent Aim Section ---
silentAim()

--- Visuals Section ---
local function visuals()
    local function billboardGui(player)
        local billboard = Instance.new("BillboardGui")
        billboard.Parent = player.Character.Head
        billboard.Adornee = player.Character.Head
        billboard.StudsOffset = Vector3.new(0, 1, 0)
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboard
        textLabel.BackgroundTransparency = 1
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.TextSize = 14
        textLabel.Text = player.Name
        local healthLabel = Instance.new("TextLabel")
        healthLabel.Parent = billboard
        healthLabel.BackgroundTransparency = 1
        healthLabel.TextColor3 = Color3.new(1, 1, 1)
        healthLabel.TextSize = 14
        healthLabel.Text = "Health: " .. player.Character.Humanoid.Health
        local levelLabel = Instance.new("TextLabel")
        levelLabel.Parent = billboard
        levelLabel.BackgroundTransparency = 1
        levelLabel.TextColor3 = Color3.new(1, 1, 1)
        levelLabel.TextSize = 14
        levelLabel.Text = "Level: " .. player.Character.Humanoid.Level
        local weaponLabel = Instance.new("TextLabel")
        weaponLabel.Parent = billboard
        weaponLabel.BackgroundTransparency = 1
        weaponLabel.TextColor3 = Color3.new(1, 1, 1)
        weaponLabel.TextSize = 14
        weaponLabel.Text = "Weapon: " .. player.Character:FindFirstChild("Tool").Name
    end

    local function tracers()
        local tracers = {}
        for _, player in pairs(game.Players:GetPlayers()) do
            if player ~= game.Players.LocalPlayer and player.Character then
                local tracer = Instance.new("Part")
                tracer.Parent = game.Workspace
                tracer.Anchored = true
                tracer.CanCollide = false
                tracer.Transparency = 0.5
                tracer.BrickColor = Color3.new(1, 1, 1)
                tracers[player] = tracer
            end
        end

        local function updateTracers()
            for player, tracer in pairs(tracers) do
                if player.Character then
                    local position = player.Character.HumanoidRootPart.Position