**INSTALLATION INSTRUCTIONS**

# Create a virtual env (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install with pip
pip install -r requirements.txt

# For M1/M2 Macs ONLY: Replace tensorflow with:
pip uninstall tensorflow -y
pip install tensorflow-macos
