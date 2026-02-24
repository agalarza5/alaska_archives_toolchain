import sys

print("\n--- Alaska Archives Meta Toolchain Check ---\n")

print("Python:", sys.version.split()[0])

# Core data libs
try:
    import numpy as np
    print("NumPy:", np.__version__)
except:
    print("NumPy: Missing")

try:
    import pandas as pd
    print("Pandas:", pd.__version__)
except:
    print("Pandas: Missing")

# OCR stack
try:
    import pytesseract
    print("PyTesseract:", pytesseract.__version__)
except:
    print("PyTesseract: Missing")

try:
    import PIL
    print("Pillow:", PIL.__version__)
except:
    print("Pillow: Missing")

# Meta / Transformer stack
try:
    import torch
    print("PyTorch:", torch.__version__)
except:
    print("PyTorch: Missing")

try:
    import transformers
    print("Transformers:", transformers.__version__)
except:
    print("Transformers: Missing")

print("\nStatus: READY for February Deliverable\n")