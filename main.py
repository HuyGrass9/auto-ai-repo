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
    local file = game:GetService("Filesystem").FileService
    local data = {}
    for k, v in pairs(cfg) do
        data[k] = v
    end
    file:SetCustomContentType("application/json")
    file:WriteText("MCXC_V2.json", json.encode(data))
end

local function loadConfig()
    local file = game:GetService("Filesystem").FileService
    local data = file:ReadText("MCXC_V2.json")
    if data then
        cfg = json.decode(data)
    end
end

loadConfig()

--- Movement Functionality Section ---
local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local stance = 1
local walkSpeed = 200
local jumpForce = 50
local position = Vector3.new(0, cfg.farmHeight, 0)
local farmSize = Vector3.new(cfg.farmSize, 100, cfg.farmSize)
local characterHit = false
local currentFarm = {x = 0, y = cfg.farmSize, size = cfg.farmSize}
local camera = game.Workspace.CurrentCamera

--- Farming Functionality Section ---
local fight = false
local fightDistance = 500
local fruitPositions = {}
local pickedFruits = {}
local farms = {}
local tool = 1

--- Local Functions Section ---
local function walkToPos(pos, callback)
    camera.CFrame = camera.CFrame * CFrame.new(0, 0, -5)
    character:MoveTo(pos, walkSpeed)
    local function checkPos()
        if character.HumanoidRootPart.Position ~= pos then
            return false
        else
            callback()
            return true
        end
    end
    while not checkPos() do
        wait()
    end
end

local function checkFight()
    for i, v in pairs(fruitPositions) do
        if (v - character.HumanoidRootPart.Position).Magnitude < fightDistance then
            return true
        end
    end
    return false
end

local function pickFruit(fruitPos)
    walkToPos(fruitPos, function()
        if character then
            game.ReplicatedStorage.Fruit:FireServer(fruitPos.Position)
        end
    end)
end

local function toolDetection()
    local tool1 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1")
    local tool2 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2")
    local tool3 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3")
    local tool4 = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4")
    if tool1 and tool2 and tool3 and tool4 then
        if tool == 1 then
            tool1.Equipped:Fire()
            tool2.Equipped:Fire()
            tool3.Equipped:Fire()
            tool4.Equipped:Fire()
        elseif tool == 2 then
            tool1.Equipped:Fire()
            tool2.Equipped:Fire()
            tool3.Equipped:Fire()
            tool4.Equipped:Fire()
        elseif tool == 3 then
            tool1.Equipped:Fire()
            tool2.Equipped:Fire()
            tool3.Equipped:Fire()
            tool4.Equipped:Fire()
        elseif tool == 4 then
            tool1.Equipped:Fire()
            tool2.Equipped:Fire()
            tool3.Equipped:Fire()
            tool4.Equipped:Fire()
        end
    end
end

local function executeCombo()
    local combo = "3XZ1CZ2ZX"
    for i = 1, #combo do
        local char = combo:sub(i, i)
        if char == "X" then
            toolDetection()
        elseif char == "Z" then
            local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("Tool" .. char)
            if tool then
                tool.Equipped:Fire()
            end
        elseif char == "1" then
            tool = 1
        elseif char == "2" then
            tool = 2
        elseif char == "3" then
            tool = 3
        elseif char == "4" then
            tool = 4
        end
        wait(0.1)
    end
end

local function isStunned()
    return character.HumanoidRootPart.Anchored or character.HumanoidRootPart.CFrame == CFrame.new(0, 0, 0)
end

local function checkBusy()
    return character.HumanoidRootPart.Anchored or character.HumanoidRootPart.CFrame == CFrame.new(0, 0, 0)
end

--- Event Script Section ---
game:GetService("RunService").RenderStepped:Connect(function()
    if cfg.farmMode then
        camera.CFrame = camera.CFrame * CFrame.new(0, 0, -5)
        
        -- Handle key presses
        if game:GetService("UserInputService"):IsKeyDown(keyBinds.one) then
            currentFarm = {x = currentFarm.x - cfg.farmSize, y = cfg.farmSize, size = cfg.farmSize}
            walkToPos(position + Vector3.new(-currentFarm.x, 0, currentFarm.y), function()
                if character then
                    for i = currentFarm.x, currentFarm.x + currentFarm.size do
                        farms[i] = true
                    end
                end
            end)
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.two) then
            currentFarm = {x = currentFarm.x + cfg.farmSize, y = cfg.farmSize, size = cfg.farmSize}
            walkToPos(position + Vector3.new(currentFarm.x, 0, currentFarm.y), function()
                if character then
                    for i = currentFarm.x, currentFarm.x + currentFarm.size do
                        farms[i] = true
                    end
                end
            end)
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.fight) then
            fight = not fight
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.tool1) then
            tool = 1
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.tool2) then
            tool = 2
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.tool3) then
            tool = 3
        elseif game:GetService("UserInputService"):IsKeyDown(keyBinds.tool4) then
            tool = 4
        end
        
        -- Handle tool detection
        if toolDetection() then
            executeCombo()
        end
        
        -- Handle silent aim
        if silentAimTab:GetValue("enabled") then
            local nearestEnemy = nil
            for i, v in pairs(game.Players:GetPlayers()) do
                if v ~= player and v.Character then
                    local distance = (v.Character.HumanoidRootPart.Position - character.HumanoidRootPart.Position).Magnitude
                    if not nearestEnemy or distance < nearestEnemy then
                        nearestEnemy = v
                    end
                end
            end
            if nearestEnemy then
                local nearestEnemyPosition = nearestEnemy.Character.HumanoidRootPart.Position
                character.HumanoidRootPart.CFrame = CFrame.new(character.HumanoidRootPart.Position, nearestEnemyPosition)
            end
        end
        
        -- Handle visuals
        if visualsTab:GetValue("enabled") then
            local billboardGui = Instance.new("BillboardGui")
            billboardGui.Parent = character.HumanoidRootPart
            billboardGui.Adornee = character.HumanoidRootPart
            billboardGui.StudsOffset = Vector3.new(0, 2, 0)
            billboardGui.Name = "BillboardGui"
            local textLabel = Instance.new("TextLabel")
            textLabel.Parent = billboardGui
            textLabel.Text = "Name: " .. player.Name .. "\nHealth: " .. character.Humanoid.Health .. "\nLevel: " .. player.Level .. "\nWeapon: " .. tool
            textLabel.Size = UDim2.new(0, 200, 0, 100)
            textLabel.BackgroundTransparency = 1