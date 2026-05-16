🪨 Rock Paper Scissors Game (Desktop GUI)A lightweight, event-driven desktop application built in Python using the tkinter framework. The game features an interactive graphical user interface, persistent real-time session score tracking, and automated audio-visual feedback compiled into a portable, standalone Windows executable (.exe).📂 Exact Repository ArchitecturePlaintext├── assets/
│   ├── rock.png                # Asset for Rock selection
│   ├── paper.png               # Asset for Paper selection
│   ├── scissors.png            # Asset for Scissors selection
│   ├── win.mp3                 # Victory audio feedback
│   ├── lose.mp3                # Defeat audio feedback
│   ├── tie.mp3                 # Draw audio feedback
│   └── game_icon.ico           # Application window icon
├── app.py                      # Main application script containing core logic & GUI
├── RockPaperScissor.exe        # Compiled standalone production executable
└── LICENSE                     # Software License agreement
⚙️ Core Implementation & Code MechanicsThe application runs purely on standard library bindings, ensuring zero external third-party overhead.1. Unified Resource Path Routing (sys._MEIPASS)To maintain asset resolution when the script is packed inside a compressed PyInstaller binary, the path resolution system dynamically switches contexts between local development files and the temporary boot directory (AppData\Local\Temp\_MEIxxxxxx):Pythonimport os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
2. Game Matrix Rules EngineThe win/loss state determination avoids bloated nested conditionals by evaluating state matches through explicit functional checks or standard lookup pairs:Player == Computer $\rightarrow$ Tie(Player == 'Rock' and Computer == 'Scissors') OR ('Paper' > 'Rock') OR ('Scissors' > 'Paper') $\rightarrow$ Player WinsOtherwise $\rightarrow$ Computer Wins🚀 Execution & Deployment InstructionsRunning the Source CodeEnsure your environment has Python 3 installed. No external package installations via pip are required for execution.Bashpython app.py
Re-Compiling the Standalone ExecutableIf you modify app.py or the items in assets/, you can recompile the exact binary distribution using the explicit build flag layout below:Bashpyinstaller --clean --onefile --windowed --icon=assets/game_icon.ico --add-data "assets;assets" app.py
📄 Licensing & Distribution AgreementsSource Code LicenseThe source code of this repository is entirely open-source and licensed under the MIT License. You are free to modify, distribute, and use it for private or commercial purposes. See the accompanying LICENSE file for full terms.Standalone Executable (.exe) End-User License AgreementThe compiled binary file RockPaperScissor.exe included in this repository is distributed under the following specific binary provisions:PlaintextTERMS OF USE FOR COMPILED BINARY (RockPaperScissor.exe)

1. Redistribution: You are permitted to redistribute the compiled .exe file 
   freely, provided that the original credit to the developer (Kunal Nayak) 
   and a link to this repository remain intact.
2. Safety & Integrity: The executable is provided clean, compiled directly 
   from the open-source code listed in app.py via PyInstaller. No modifications 
   or injections have been made to the native code.
3. No Warranty: THE EXECUTABLE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
   MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL THE 
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
   LIABILITY ARISING FROM THE RUNTIME EXECUTION OF THE BINARY.
👤 AuthorDeveloped and maintained by Kunal Nayak (@kunal2005j03).
