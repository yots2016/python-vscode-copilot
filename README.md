# Python VSCode Copilot Example

This is a simple Python web service that serves a static HTML page and provides an endpoint to simulate pressing the F14 key.

## Structure
- `app/` — application source code
  - `server.py`: main server code
- `static/` — static files (HTML, CSS, etc.)
  - `hello.html`: animated HTML page
- `tests/` — integration and unit tests
- `requirements.txt` — pip dependencies
- `pyproject.toml` — Poetry/PEP 517+ build config
- `README.md` — project documentation
- `.gitignore` — git ignore rules

## Usage

### Using Poetry (recommended)
1. Install dependencies:
   ```sh
   poetry install
   ```
2. Run the server:
   ```sh
   poetry run python app/server.py
   ```

### Using pip
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```sh
   python app/server.py
   ```

3. Open [http://localhost:8000](http://localhost:8000) in your browser.
4. To trigger F14 press, open [http://localhost:8000/f14](http://localhost:8000/f14)

## Endpoints
- `/` — returns the animated HTML page (`hello.html`)
- `/f14` — simulates F14 key press and returns plain text
- `/image` — returns a dynamically generated PNG image using Pillow

---

**Note:**
- The virtual environment (`.venv/` or `venv/`) should not be committed to version control.
- For more endpoints or features, extend `app/server.py`.
