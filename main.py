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
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
        elseif tool == 3 then
            -- Tool 3 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool3"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1"))
        elseif tool == 4 then
            -- Tool 4 combo
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool4"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool1"))
            task.wait(0.5)
            game.Players.LocalPlayer.Character.Humanoid:EquipTool(game.Players.LocalPlayer.Backpack:FindFirstChild("Tool2"))
        end
    end
    local function checkBusy()
        if game.Players.LocalPlayer.Character.Humanoid.Health <= 0 then
            return true
        elseif game.Players.LocalPlayer.Character:FindFirstChild("Stunned") then
            return true
        elseif game.Players.LocalPlayer.Character:FindFirstChild("Busy") then
            return true
        end
        return false
    end
    local function isStunned()
        return game.Players.LocalPlayer.Character:FindFirstChild("Stunned")
    end
    local function combo()
        while true do
            if checkBusy() then
                task.wait(0.5)
            else
                executeCombo()
                task.wait(0.5)
            end
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
        if namecall == "FireServer" then
            if args[1] == "GetNearestEnemy" then
                local nearestEnemy = getNearestEnemy()
                if nearestEnemy then
                    return nearestEnemy.Character.HumanoidRootPart.Position
                end
            end
        end
        return namecall(args)
    end
    local function overrideVector3(vector3)
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            return nearestEnemy.Character.HumanoidRootPart.Position
        end
        return vector3
    end
    local function overrideCFrame(cframe)
        local nearestEnemy = getNearestEnemy()
        if nearestEnemy then
            return nearestEnemy.Character.HumanoidRootPart.CFrame
        end
        return cframe
    end
    local function silentAimHook()
        local oldFireServer = game.ReplicatedStorage.RemoteEvent.FireServer
        game.ReplicatedStorage.RemoteEvent.FireServer = fireServer
        local oldGetMousePosition = UserInputService.GetMousePosition
        UserInputService.GetMousePosition = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return nearestEnemy.Character.HumanoidRootPart.Position
            end
            return oldGetMousePosition()
        end
        local oldGetMouseLookVector = UserInputService.GetMouseLookVector
        UserInputService.GetMouseLookVector = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return (nearestEnemy.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            end
            return oldGetMouseLookVector()
        end
        local oldGetMousePosition2 = UserInputService.GetMousePosition2
        UserInputService.GetMousePosition2 = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return nearestEnemy.Character.HumanoidRootPart.Position
            end
            return oldGetMousePosition2()
        end
        local oldGetMouseLookVector2 = UserInputService.GetMouseLookVector2
        UserInputService.GetMouseLookVector2 = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return (nearestEnemy.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            end
            return oldGetMouseLookVector2()
        end
        local oldGetMousePosition3 = UserInputService.GetMousePosition3
        UserInputService.GetMousePosition3 = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return nearestEnemy.Character.HumanoidRootPart.Position
            end
            return oldGetMousePosition3()
        end
        local oldGetMouseLookVector3 = UserInputService.GetMouseLookVector3
        UserInputService.GetMouseLookVector3 = function()
            local nearestEnemy = getNearestEnemy()
            if nearestEnemy then
                return (nearestEnemy.Character.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Unit
            end
            return oldGetMouseLookVector3()
        end
    end
    silentAimHook()
end

--- Visuals Section ---
local function visuals()
    local function billboardGui()
        local billboardGui = Instance.new("BillboardGui")
        billboardGui.Parent = game.Players.LocalPlayer.PlayerGui
        billboardGui.Name = "BillboardGui"