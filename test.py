import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# This path should include 'week1' -- that proves you're in the right env
assert "week1" in sys.executable.lower() or "agentic-week1" in sys.executable.lower(), \
    "WARNING: Not running in week1 environment!"

print("\n Setup verified.")