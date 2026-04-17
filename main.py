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
    local function combo()
        while wait() do
            executeCombo()
        end
    end
    combo()

    local function isStunned()
        return game.Players.LocalPlayer.Character.HumanoidRootPart:FindFirstChild("Stunned")
    end

    local function checkBusy()
        return game.Players.LocalPlayer.Character.HumanoidRootPart:FindFirstChild("Busy")
    end

    local function combatEngine()
        while wait() do
            if isStunned() then
                task.wait(1)
            elseif checkBusy() then
                task.wait(1)
            else
                executeCombo()
            end
        end
    end
    combatEngine()
end

--- Silent Aim Section ---
local function silentAim()
    local function fireServer(namecall)
        local args = {...}
        if namecall == "FireServer" then
            if args[1] == "GetNearestEnemy" then
                local player = game.Players.LocalPlayer
                local character = player.Character
                local humanoidRootPart = character:WaitForChild("HumanoidRootPart")
                local lookVector = (game.Workspace:FindFirstChild("Players"):FindFirstChild(player.Name):WaitForChild("Character"):WaitForChild("HumanoidRootPart").Position - humanoidRootPart.Position).Unit
                local nearestEnemy = game.Workspace:FindFirstChild("Players"):FindFirstChild(player.Name):WaitForChild("Character"):WaitForChild("HumanoidRootPart"):GetNearestEnemy()
                if nearestEnemy then
                    local nearestEnemyPosition = nearestEnemy.Position
                    local nearestEnemyCFrame = nearestEnemy.CFrame
                    local nearestEnemyLookVector = (nearestEnemyPosition - humanoidRootPart.Position).Unit
                    local nearestEnemyRotation = nearestEnemyLookVector:ToOrientation()
                    local nearestEnemyCFrame = CFrame.lookAt(humanoidRootPart.Position, nearestEnemyPosition)
                    return nearestEnemyCFrame
                end
            end
        end
        return namecall(args)
    end
    local function __namecall(func, ...)
        return fireServer(func, ...)
    end
    getrawmetatable(game).__namecall = __namecall
end

--- Visuals Section ---
local function visuals()
    local function billboardGui()
        local billboard = Instance.new("BillboardGui")
        billboard.Parent = game.Players.LocalPlayer.PlayerGui
        billboard.Name = "Billboard"
        billboard.Adornee = game.Players.LocalPlayer.Character
        billboard.StudsOffset = Vector3.new(0, 2, 0)
        local textLabel = Instance.new("TextLabel")
        textLabel.Parent = billboard
        textLabel.Name = "TextLabel"
        textLabel.BackgroundTransparency = 1
        textLabel.Text = ""
        textLabel.TextColor3 = Color3.new(1, 1, 1)
        textLabel.Font = Enum.Font.SourceSansBold
        textLabel.FontSize = Enum.FontSize.Size24
        textLabel.TextScaled = true
        local function updateTextLabel()
            local player = game.Players.LocalPlayer
            local character = player.Character
            local humanoid = character:WaitForChild("Humanoid")
            local name = player.Name
            local health = humanoid.Health
            local level = humanoid.Level
            local weapon = character:FindFirstChild("Tool1") and character:FindFirstChild("Tool1").Name or "No Tool"
            textLabel.Text = name .. "\nHealth: " .. health .. "\nLevel: " .. level .. "\nWeapon: " .. weapon
        end
        updateTextLabel()
        local function update()
            while wait() do
                updateTextLabel()
            end
        end
        update()
    end
    local function tracers()
        local tracers = Instance.new("Folder")
        tracers.Name = "Tracers"
        tracers.Parent = game.Players.LocalPlayer.PlayerGui
        local function createTracer()
            local tracer = Instance.new("BillboardGui")
            tracer.Parent = tracers
            tracer.Name = "Tracer"
            tracer.Adornee = game.Players.LocalPlayer.Character
            tracer.StudsOffset = Vector3.new(0, 2, 0)
            local textLabel = Instance.new("TextLabel")
            textLabel.Parent = tracer
            textLabel.Name = "TextLabel"
            textLabel.BackgroundTransparency = 1
            textLabel.Text = ""
            textLabel.TextColor3 = Color3.new(1, 1, 1)
            textLabel.Font = Enum.Font.SourceSansBold
            textLabel.FontSize = Enum.FontSize.Size24
            textLabel.TextScaled = true
            local function updateTextLabel()
                local player = game.Players.LocalPlayer
                local character = player.Character
                local humanoid = character:WaitForChild("Humanoid")
                local name = player.Name
                local health = humanoid.Health
                local level = humanoid.Level
                local weapon = character:FindFirstChild("Tool1") and character:FindFirstChild("Tool1").Name or "No Tool"
                textLabel.Text = name .. "\nHealth: " .. health .. "\nLevel: " .. level .. "\nWeapon: " .. weapon
            end
            updateTextLabel()
            local function update()
                while wait() do
                    updateTextLabel()
                end
            end
            update()
        end
        createTracer()
        local function update()
            while wait() do
                createTracer()
            end
        end
        update()
    end
    local function fovChanger()
        local fov