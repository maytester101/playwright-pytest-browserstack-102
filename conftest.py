# conftest.py
# BrowserStack Playwright pytest configuration

import pytest
import os
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """
    Configure browser context options for Playwright.
    BrowserStack capabilities are handled automatically by browserstack-sdk
    when running tests via 'browserstack-sdk pytest'.
    
    For local testing, you can customize browser context here.
    """
    # BrowserStack SDK automatically handles BrowserStack-specific configuration
    # when running via 'browserstack-sdk pytest'
    
    # For local testing, you can add custom context options here
    # Example: viewport size, locale, timezone, etc.
    return {
        **browser_context_args,
        # Add any custom Playwright browser context options here
        # Example:
        # "viewport": {"width": 1920, "height": 1080},
        # "locale": "en-US",
    }


@pytest.fixture(scope="function")
def page_with_metadata(page: Page, request):
    """
    Enhanced page fixture with BrowserStack test metadata.
    Use this fixture instead of 'page' to get BrowserStack-specific features.
    
    Note: BrowserStack SDK automatically captures test metadata.
    This fixture is optional and can be used for additional customizations.
    """
    # Set test name for BrowserStack reporting (optional)
    test_name = request.node.name
    
    # BrowserStack SDK automatically handles test naming and metadata
    # This is just for any additional custom headers if needed
    
    yield page
    
    # Cleanup: BrowserStack SDK handles test completion automatically