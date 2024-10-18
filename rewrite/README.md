# Run the app

1. Install the dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app
```bash
uvicorn main:app --reload
```

3. seed the db in a new terminal
```bash
python seed.py
```