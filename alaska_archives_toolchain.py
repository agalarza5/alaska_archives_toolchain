import sys

print("Abigail Meta Toolchain Check")
print("Python:", sys.version)

# Core libs
import numpy as np
import pandas as pd

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)

try:
    import openai
    print("OpenAI library: Installed")
except Exception as e:
    print("OpenAI library: Missing", e)