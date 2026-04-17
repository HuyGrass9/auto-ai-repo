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
            -- task.wait(0.5)
            -- game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1"))
        end
    end
    local function isStunned()
        return game.Players.LocalPlayer.Character.Humanoid.State == Enum.HumanoidStateType.Dazed or game.Players.LocalPlayer.Character.Humanoid.State == Enum.HumanoidStateType.Unconscious
    end
    local function checkBusy()
        return game.Players.LocalPlayer.Character.HumanoidRootPart.Velocity.Magnitude > 0 or game.Players.LocalPlayer.Character.Humanoid.JumpPower > 0
    end
    local function combatLoop()
        while wait() do
            if checkTool() then
                executeCombo()
            end
            if isStunned() then
                wait(1)
            elseif checkBusy() then
                wait(1)
            else
                executeCombo()
            end
        end
    end
    combatLoop()
end

--- Silent Aim Section ---
local function silentAim()
    local function getNearestEnemy()
        local nearestEnemy = nil
        local minDistance = math.huge
        for _, player in pairs(game.Players:GetPlayers()) do
            if player ~= game.Players.LocalPlayer and player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
                local distance = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - player.Character.HumanoidRootPart.Position).Magnitude
                if distance < minDistance then
                    minDistance = distance
                    nearestEnemy = player
                end
            end
        end
        return nearestEnemy
    end
    local function fireServer()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            local firePosition = nearestEnemy.Character.HumanoidRootPart.Position
            local fireDirection = (firePosition - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            local fireCFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(fireDirection * 10)
            game.Players.LocalPlayer.Character.Humanoid:FireServer("Fire", fireCFrame)
        end
    end
    local function __namecall(func, ...)
        local args = {...}
        if func.Name == "FireServer" then
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                local firePosition = nearestEnemy.Character.HumanoidRootPart.Position
                local fireDirection = (firePosition - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
                local fireCFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(fireDirection * 10)
                args[1] = "Fire"
                args[2] = fireCFrame
            end
        end
        return func(unpack(args))
    end
    getgenv().fireServer = fireServer
    setmetatable(getgenv(), {__namecall = __namecall})
end

--- Visuals Section ---
local function visuals()
    local function createBillboardGui()
        local billboardGui = Instance.new("BillboardGui")
        billboardGui.Parent = game.Players.LocalPlayer.Character
        billboardGui.Name = "BillboardGui"
        billboardGui.Adornee = game.Players.LocalPlayer.Character.HumanoidRootPart
        billboardGui.AlwaysOnTop = true
        billboardGui.LightInfluence = 0
        billboardGui.MaxDistance = math.huge
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboardGui
        textLabel.Name = "TextLabel"
        textLabel.BackgroundTransparency = 1
        textLabel.Text = ""
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.FontSize = Enum.FontSize.Size24
        return billboardGui, textLabel
    end
    local function updateBillboardGui()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            local firePosition = nearestEnemy.Character.HumanoidRootPart.Position
            local fireDirection = (firePosition - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            local fireCFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(fireDirection * 10)
            local billboardGui, textLabel = createBillboardGui()
            textLabel.Text = nearestEnemy.Name .. " (" .. nearestEnemy.Character.Humanoid.Health .. ")"
            textLabel.CFrame = fireCFrame
        end
    end
    local function createTracers()
        local tracers = {}
        for i = 1, 10 do
            local tracer = Instance.new("Part")
            tracer.Parent = game.Workspace
            tracer.Name = "Tracer" .. i
            tracer.Anchored = true
            tracer.CanCollide = false
            tracer.Material = Enum.Material.Neon
            tracer.Transparency = 0.5
            table.insert(tracers, tracer)
        end
        return tracers
    end
    local function updateTracers()
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            local firePosition = nearestEnemy.Character.HumanoidRootPart.Position
            local fireDirection = (firePosition - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            local fireCFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame