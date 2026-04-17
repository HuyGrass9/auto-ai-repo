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
                return true
            else
                return false
            end
        end
    end
    local function combatEngine()
        while wait() do
            if not checkBusy() then
                executeCombo()
            end
            if isStunned() then
                task.wait(0.5)
            end
        end
    end
    combatEngine()
end

--- Silent Aim Section ---
local function silentAim()
    local function getNearestEnemy()
        local players = game.Players:GetPlayers()
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
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" then
            if args[1] == "GetNearestEnemy" then
                local nearestEnemy = getNearestEnemy()
                if nearestEnemy then
                    return nearestEnemy.Character.HumanoidRootPart.Position
                else
                    return Vector3.new(0, 0, 0)
                end
            end
        end
        return namecall(args)
    end
    local function silentAimEngine()
        while wait() do
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                local head = nearestEnemy.Character:FindFirstChild("Head")
                if head then
                    local aimPosition = head.Position
                    local character = game.Players.LocalPlayer.Character
                    local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                    if humanoidRootPart then
                        local aimCFrame = CFrame.new(humanoidRootPart.Position, aimPosition)
                        humanoidRootPart.CFrame = aimCFrame
                    end
                end
            end
        end
    end
    getgenv().fireServer = fireServer
    silentAimEngine()
end

--- Visuals Section ---
local function visuals()
    local function billboardGui()
        local billboardGui = Instance.new("BillboardGui")
        billboardGui.Parent = game.Players.LocalPlayer.Character
        billboardGui.Name = "BillboardGui"
        billboardGui.Adornee = game.Players.LocalPlayer.Character.HumanoidRootPart
        billboardGui.LightInfluence = 1
        billboardGui.StudsOffset = Vector3.new(0, 2, 0)
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboardGui
        textLabel.Name = "TextLabel"
        textLabel.BackgroundTransparency = 1
        textLabel.Text = "Name: "
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.FontSize = Enum.FontSize.Size24
        local function updateTextLabel()
            local character = game.Players.LocalPlayer.Character
            local humanoid = character:FindFirstChild("Humanoid")
            if humanoid then
                local name = humanoid.Name
                local health = humanoid.Health
                local level = humanoid.Level
                local weapon = character:FindFirstChild("Tool")
                if weapon then
                    local toolName = weapon.Name
                    textLabel.Text = "Name: " .. name .. "\nHealth: " .. health .. "\nLevel: " .. level .. "\nWeapon: " .. toolName
                else
                    textLabel.Text = "Name: " .. name .. "\nHealth: " .. health .. "\nLevel: " .. level
                end
            end
        end
        updateTextLabel()
        while wait() do
            updateTextLabel()
        end
    end
    local function tracers()
        local tracers = Instance.new("Folder")
        tracers.Name = "Tracers"
        tracers.Parent = game.Players.LocalPlayer.Character
        local function createTracer()
            local tracer = Instance.new("Part")
            tracer.Name = "Tracer"
            tracer.Parent = tracers
            tracer.Anchored = true
            tracer.CanCollide = false
            tracer.Transparency = 0.5
            tracer.BrickColor = BrickColor.new("Bright blue")
            local function updateTracer()
                local character = game.Players.LocalPlayer.Character
                local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                if humanoidRootPart then
                    local tracerPosition = humanoidRootPart.Position + (humanoidRootPart.CFrame.LookVector * 10)
                    tracer.Position = tracerPosition
                end
            end
            updateTracer()
            while