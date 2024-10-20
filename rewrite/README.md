# Run the app


1. Create .env file
    copy .env.template to .env and fill in values for the variables

2. Install the dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app with invoke
```bash
invoke start
```

This empties the db and starts the app.