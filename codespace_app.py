#!/usr/bin/env python3
"""
Test FastAPI application for GitHub Codespaces
Codespace Name: ga2-10b7c2
"""

import os
from fastapi import FastAPI

app = FastAPI(title="Codespace Test - ga2-10b7c2")

@app.get("/")
def root():
    return {
        "message": "GitHub Codespaces Test",
        "codespace_name": "ga2-10b7c2",
        "github_repository": os.environ.get("GITHUB_REPOSITORY", "Not available"),
        "github_token_present": bool(os.environ.get("GITHUB_TOKEN")),
        "python_version": os.sys.version.split()[0]
    }

@app.get("/env")
def environment():
    return {
        "codespace_name": os.environ.get("CODESPACE_NAME", "Not in Codespace"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY", "Not available"),
        "github_user": os.environ.get("GITHUB_USER", "Not available"),
        "github_token_available": "GITHUB_TOKEN" in os.environ
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)