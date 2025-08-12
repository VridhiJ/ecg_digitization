import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

# Quantum computing settings
QUANTUM_BACKEND = "qasm_simulator"
MAX_QUBITS = 20

# ECG processing settings
SAMPLING_RATE = 360  # Hz
LEADS = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Model settings
BATCH_SIZE = 32
LEARNING_RATE = 0.001