import os
import sys

# Define constants
GAME_NAME = 'MayChemXeoCan V2'
MODULES = ['module1', 'module2', 'module3', 'module4', 'module5', 'module6', 'module7', 'module8', 'module9', 'module10', 'module11']

# Define classes
class Game:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def run(self):
        for module in self.modules:
            module.run()

class Module:
    def __init__(self, name):
        self.name = name

    def run(self):
        pass

# Define functions
def load_module(module_name):
    if module_name in MODULES:
        return __import__(module_name)
    else:
        raise ValueError(f'Module {module_name} not found')

# Create game instance
game = Game()

# Add modules to game
for module_name in MODULES:
    module = load_module(module_name)
    game.add_module(module)

# Run game
game.run()

# Evaluate code
score = evaluate_code('MayChemXeoCan V2')

# If score < 7, repair code
if score < 7:
    # Repair code
    # ... (tên sửa code)

# If score >= 7, write code to main.py and push to git
if score >= 7:
    write_file('MayChemXeoCan V2')
    run_git('push')