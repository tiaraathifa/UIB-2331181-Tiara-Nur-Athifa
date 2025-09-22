print("=== Verifying your Python environment... ===\n")

try:
    import numpy
    print(f"[OK] NumPy installed, version: {numpy.__version__}")
except ImportError:
    print("[X] NumPy not installed!")

try:
    import pandas
    print(f"[OK] Pandas installed, version: {pandas.__version__}")
except ImportError:
    print("[X] Pandas not installed!")

try:
    import matplotlib
    print(f"[OK] Matplotlib installed, version: {matplotlib.__version__}")
except ImportError:
    print("[X] Matplotlib not installed!")

try:
    import seaborn
    print(f"[OK] Seaborn installed, version: {seaborn.__version__}")
except ImportError:
    print("[X] Seaborn not installed!")

try:
    import sklearn
    print(f"[OK] scikit-learn installed, version: {sklearn.__version__}")
except ImportError:
    print("[X] scikit-learn not installed!")

print("\n=== Verification finished! ===")
