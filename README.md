*** Boot.dev/AIasistant 

to run (once):
```bash
    uv venv
    uv add google-genai==1.12.1
    uv add python-dotenv==1.1.0
```

```bash
    source .venv/bin/activate
```

```bash
    uv run main.py <aibot-prompt>
```


Dependencies:
- Python  `3.10+`
- UV
- google-genai==`1.12.1`
- python-dotenv==`1.1.0`