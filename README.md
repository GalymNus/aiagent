<h1>Boot.dev/AIassistant </h1>

<h3>To run:</h3>
Create venv

```bash
    uv venv
```

activate venv
```bash
    source .venv/bin/activate
```
Install dependencies (once)
```bash
    uv add google-genai==1.12.1
    uv add python-dotenv==1.1.0
```
Make request
```bash
    uv run main.py <aibot-prompt>
```


Dependencies:
- Python  `3.10+`
- UV
- google-genai==`1.12.1`
- python-dotenv==`1.1.0`