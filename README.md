# CHSH_game_tutorial

This repository contains an interactive tutorial on the CHSH game, a quantum experiment that demonstrates how entanglement allows two players to win a cooperative game beyond the limits of classical physics. You'll learn the theory behind Bell inequalities, explore classical vs. quantum strategies, and run real quantum circuits — both on a simulator and IBM Quantum hardware.

## Repository Structure
```
├── CHSH Game.ipynb     # Main tutorial notebook - start here
├── Images              # Images folder for the tutorial
├── Installation.ipynb  # Instructions for creating an IBM Quantum account
├── README.md           # This file
├── environment.yaml    # To create the environment if using conda
├── requirements.txt    # To create the environment using pip
└── util.py             # Tests to check answers to exercises in tutorial notebook
```

## Set up instructions
Using pip:
```
python3 -m venv chsh_env
source chsh_env/bin/activate
pip install -r requirements.txt
```

Using conda:
```
conda env create -f environment.yaml
conda activate chsh_env
```

Refer to the file Installation.ipynb for instructions on creating an IBM Quantum account in order to run the code on real quantum hardware.

## Run the CHSH game tutorial
Once your setup is complete, launch 
```
jupyter notebook "CHSH Game.ipynb"
```


