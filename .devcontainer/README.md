# GitHub Codespace Configuration - ga2-10b7c2

This devcontainer configuration sets up a GitHub Codespace environment for TDS project development.

## Configuration Details

- **Name**: ga2-10b7c2
- **Python**: 3.11 via ghcr.io/devcontainers/features/python:1
- **Extensions**:
  - astral-sh.uv (UV package manager)
  - ms-python.python (Python language support)
- **Post-create**: Installs FastAPI via `uv pip install fastapi`

## Features

- ✅ Python 3.11 environment
- ✅ UV package manager for fast dependency installation
- ✅ FastAPI pre-installed for API development
- ✅ Port forwarding configured for ports 8000 and 7018
- ✅ Volume mount for UV cache persistence

## Usage

1. Launch Codespace from GitHub repository
2. Wait for post-create command to complete
3. Run `python codespace_test.py` to test the environment
4. Access applications via forwarded ports

## Environment Variables

The Codespace automatically provides:
- `GITHUB_REPOSITORY` - Repository slug (owner/repo)
- `GITHUB_TOKEN` - Authentication token for API access
- `CODESPACE_NAME` - Name of the current codespace

## Testing

Run the following command in the Codespace terminal:
```bash
echo $GITHUB_REPOSITORY $GITHUB_TOKEN
```

This will output the repository slug and authentication token as required.