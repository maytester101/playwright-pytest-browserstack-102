# Playwright Test Project

A Playwright test automation project using pytest for UI testing.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/ui/test_login.py
```

### Run with verbose output:
```bash
pytest -v
```

### Run with browser visible (headed mode):
Add `--headed` flag:
```bash
pytest --headed
```

### Run tests in parallel:
```bash
pytest -n auto
```

## Project Structure

```
playwright-project/
├── tests/
│   ├── ui/
│   │   └── test_login.py
│   └── api/
├── conftest.py          # Pytest configuration
├── pytest.ini          # Pytest settings
├── requirements.txt     # Python dependencies
└── browserstack.yml     # BrowserStack configuration
```

## Using AI to Run Tests

You can use Cursor AI (or similar AI assistants) to:

1. **Run tests for you:** Simply ask "Run the tests" or "Execute pytest"
2. **Debug failing tests:** Share error messages and ask for help
3. **Modify tests:** Request changes and have AI update the code
4. **Add new tests:** Describe what you want to test and AI can write the code

### Example AI Commands:
- "Run all tests"
- "Run the login test"
- "Run tests with browser visible"
- "Fix any failing tests"
- "Add a test for user registration"

## BrowserStack Integration

This project is configured to run tests on BrowserStack cloud infrastructure, enabling cross-browser and cross-platform testing.

### BrowserStack Features Enabled

✅ **Multi-platform testing**: Tests run on Windows, macOS, Safari, Chrome, Edge  
✅ **Video recording**: All test executions are recorded  
✅ **Network logs**: HTTP requests/responses are captured  
✅ **Console logs**: Browser console output is captured  
✅ **Screenshots**: Automatic and custom screenshots  
✅ **Test observability**: Enhanced reporting and analytics  
✅ **Parallel execution**: Run multiple tests simultaneously  

### Running Tests on BrowserStack

#### Method 1: Using BrowserStack SDK (Recommended)
```bash
# Run all tests on BrowserStack
browserstack-sdk pytest

# Run specific test file
browserstack-sdk pytest tests/ui/test_login.py

# Run with verbose output
browserstack-sdk pytest -v
```

#### Method 2: Using pytest-playwright directly
```bash
# Set environment variables (optional, credentials are in browserstack.yml)
export BROWSERSTACK_USERNAME="your_username"
export BROWSERSTACK_ACCESS_KEY="your_access_key"

# Run tests
pytest
```

### BrowserStack Configuration

The `browserstack.yml` file configures:
- **Platforms**: Windows 11 (Chrome, Edge), macOS Ventura (Safari, Chrome)
- **Parallel execution**: 2 tests per platform
- **Build information**: Project and build names for dashboard organization
- **Features**: Video, network logs, console logs, test observability

### Viewing Test Results

After running tests, view results at:
- **BrowserStack Dashboard**: https://automate.browserstack.com/
- **Test Reports**: Check the `log/` directory for detailed logs
- **Screenshots**: Saved locally as `screenshot.png`

### Environment Variables (Optional)

Create a `.env` file (see `.env.example`) to override credentials:
```bash
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
BROWSERSTACK_LOCAL=false  # Set to true for localhost testing
```

### Test Improvements Made

1. **Enhanced Test Assertions**: Added proper expect() assertions for better test reliability
2. **Parameterized Tests**: Added multiple test scenarios using pytest.mark.parametrize
3. **Better Error Handling**: Improved error detection and reporting
4. **Test Metadata**: Added docstrings and test naming for BrowserStack reporting
5. **Multiple Platforms**: Configured tests to run on 4 different browser/OS combinations
6. **Parallel Execution**: Enabled parallel test execution for faster results

## Configuration

- **pytest.ini**: Configures pytest to look in `tests/` directory
- **conftest.py**: Configures BrowserStack connection and capabilities
- **browserstack.yml**: BrowserStack cloud testing configuration with multiple platforms
- **.env.example**: Template for environment variables (create `.env` from this)
"# playwright-pytest-browserstack-102" 
