Here's an optimized version of the Blox Fruits auto-farm Lua script for Delta X, utilizing keys 1-4.

```lua
-- MayChemXeoCan_V6_DeltaX.lua

--- Configuration Section ---
local configFile = loadstring(game:HttpGet("https://raw.githubusercontent.com/MayChemXeoCan/BloxAPI/master/config.lua"))()
local cfg = {}
for k, v in pairs(configFile) do
    cfg[k] = v
end

--- Key Bind Section ---
local keyBinds = {
    one = Enum.KeyCode.One,
    two = Enum.KeyCode.Two,
    three = Enum.KeyCode.Three,
    four = Enum.KeyCode.Four,
    exit = Enum.KeyCode.Escape,
    fight = Enum.KeyCode.F,
}

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

--- Local Functions Section ---
local function walkToPos(pos)
    camera.CFrame = camera.CFrame * CFrame.new(0, 0, -5)
    character:MoveTo(pos, walkSpeed)
    while character.HumanoidRootPart.Position ~= pos do
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
    while (fruitPos - character.HumanoidRootPart.Position).Magnitude > 0.1 do
        character:MoveTo(fruitPos, walkSpeed)
    end
    game.ReplicatedStorage.Fruit:FireServer(fruitPos.Position)
end

--- Event Script Section ---
game:GetService("RunService").RenderStepped:Connect(function()
    if cfg.farmMode then
        camera.CFrame = camera.CFrame * CFrame.new(0, 0, -5)
        character.HumanoidRootPart.CFrame = character.HumanoidRootPart.CFrame + (position - character.HumanoidRootPart.Position).Unit * walkSpeed * 0.001
        
        if math.abs(character.HumanoidRootPart.Position.X - position.X) > 50 then
            currentFarm.x = math.floor(character.HumanoidRootPart.Position.X / cfg.farmSize) * cfg.farmSize
        end
        
        if math.abs(character.HumanoidRootPart.Position.Z - position.Z) > 50 then
            currentFarm.size = math.floor(character.HumanoidRootPart.Position.Z / cfg.farmSize) * cfg.farmSize
        end
        
        if currentFarm.x < (position.X - farmSize.X / 2) then
            character.HumanoidRootPart.CFrame = CFrame.new(currentFarm.x, currentFarm.y, position.Z)
        elseif currentFarm.x > (position.X + farmSize.X / 2) then
            character.HumanoidRootPart.CFrame = CFrame.new(position.X - farmSize.X, currentFarm.y, position.Z)
        end
    end
    
    if cfg.farmMode then
        for i, v in pairs(fruitPositions) do
            if v:Distance(character.HumanoidRootPart.Position) < 0.5 then
                table.remove(fruitPositions, i)
            end
        end
        
        for _, v in pairs(game.Workspace.Fruits:GetChildren()) do
            local fruitPos = v:FindFirstChild("Pos")
            if fruitPos then
                if not fruitPositions[v] then
                    table.insert(fruitPositions, {v, fruitPos.Position})
                elseif v ~= fruitPositions[v][1] then
                    table.insert(fruitPositions, {v, fruitPos.Position})
                    for i = 1, #fruitPositions do
                        if fruitPositions[i][1] == v then
                            table.remove(fruitPositions, i)
                        end
                    end
                end
            end
        end
        
        while #fruitPositions > 0 and cfg.farmMode do
            if checkFight() or cfg.fight then
                local fruitPos = fruitPositions[1][2]
                pickFruit(fruitPos)
                while fruitPos:IsDescendantOf(game.Workspace) and game.ReplicatedStorage.Fruit.Value == "no fruit nearby" do
                    wait(0.1)
                    game.ReplicatedStorage.Fruit:FireServer(fruitPos.Position)
                end
            end
            
            if #fruitPositions > 0 and (fruitPositions[1][1]:FindFirstChild("Pos"):GetPosition() - character.HumanoidRootPart.Position).Magnitude > 50 then
                local fruitPos = fruitPositions[1][2]
                if not cfg.ignore then
                    pickFruit(fruitPos)
                    while fruitPos:IsDescendantOf(game.Workspace) and game.ReplicatedStorage.Fruit.Value == "no fruit nearby" do
                        wait(0.1)
                        game.ReplicatedStorage.Fruit:FireServer(fruitPos.Position)
                    end
                end
                table.remove(fruitPositions, 1)
            end
        end
    end
end)

--- UI Script Section ---
local UI = {}
UI.window = game:GetService("UserInputService"):WaitForUserConfirmation(Enum.UserInputType.MouseButton1)
local mainPage = script.Parent
function UI:CreateWindow()
    local window = Instance.new("ScreenGui")
    window.Name = "MayChemXeoCanGUI"
    window.Parent = mainPage
    return window
end

function UI:CreateMenu(title)
    local menu = Instance.new("TextButton")
    menu.Name = title
    menu.Parent = UI.window
    menu.Text = title
    menu.Size = UDim2.new(0, 200, 0, 30)
    menu.BackgroundTransparency = 1
    menu.Font = Enum.Font.SourceSansBold
    menu.FontSize = Enum.FontSize.Small
    return menu
end

function UI:CreateToggle(title, defaultValue)
    local menu = UI:CreateMenu(title)
    if defaultValue then
        menu.BackgroundColor3 = Color3.new(0.2, 0.5, 0)
    else
        menu.BackgroundColor3 = Color3.new(0.2, 0.2, 0.2)
    end
    local toggle = Instance.new("TextLabel")
    toggle.Name = "toggle"
    toggle.Parent = menu
    toggle.TextColor3 = Color3.new(1, 1, 1)
    toggle.BackgroundTransparency = 1
    local function toggleFunction()
        if menu.BackgroundColor3 == Color3.new(0.2, 0.5, 0) then
            menu.BackgroundColor3 = Color3.new(0.2, 0.2, 0.2)
            toggle.Text = "Disable"
            cfg[title] = false
        else
            menu.BackgroundColor3 = Color3.new(0.2, 0.5, 0)
            toggle.Text = "Enable"
            cfg[title] = true
        end
    end
    menu.MouseButton1Down:Connect(toggleFunction)
    return toggle
end

function UI:CreateKeybind(keybind, defaultKey)
    local menu = UI:CreateMenu("Keybind")
    local keybindValue = defaultKey
    local storedKeybind = keyBinds[keybind] or Enum.KeyCode.None
    local keybindToggle = UI:CreateToggle("Keybind", defaultKey == storedKeybind)
    local storedKeybindName = keybind .. "Name"
    if storedKeybind == Enum.KeyCode.None then
        storedKeybindName = ""
    end
    menu.StoredKeybindName = storedKeybindName
    local currentKey = Enum.KeyCode[storedKeybindName or "None"]
    local keys = {}
    keys[currentKey] = storedKeybind
    local keybindKeys = {"F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Space", "Escape", "Shift", "Ctrl", "Alt", "Enter"}
    for i = 1, #keybindKeys do
        local key = Enum.KeyCode[keybindKeys[i]]
        table.insert(keys, key)
    end
    local function changeKeybind()
        local function getKeyName()
            local textbox = Instance.new("TextBox")
            textbox.Parent = mainPage
            local function getText()
                while not textbox.Text and not textbox:FindFirstChild("TextLabel") do
                    wait()
                end
                if textbox.Text then
                    local keyName = textbox.Text
                    textbox:Destroy()
                    return keyName
                else
                    local keyLabel = textbox:FindFirstChild("TextLabel")
                    textbox:Destroy()
                    return keyLabel.Text
                end
            end
            return getText
        end
        getKeyName()
        local keyLabel = Instance.new("TextLabel")
        keyLabel.Parent = mainPage
        local function changeKeyName(value