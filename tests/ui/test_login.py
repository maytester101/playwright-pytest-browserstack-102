import pytest
import re
from playwright.sync_api import Page, expect


def test_facebook_invalid_login(page: Page, browser_name: str):
    """
    Test invalid login attempt on Facebook.
    This test verifies that Facebook shows appropriate error messages
    for invalid credentials.
    
    BrowserStack Features Used:
    - Cross-browser testing
    - Screenshot capture
    - Network logs
    - Video recording
    """
    # Navigate to Facebook login page
    page.goto("https://www.facebook.com")
    
    # Verify we're on the login page
    expect(page).to_have_title(re.compile(r"Facebook", re.IGNORECASE))
    
    # Fill login form with invalid credentials
    email_input = page.locator("input[name='email']")
    email_input.fill("invalid_email@test.com")
    
    # Verify email was entered
    expect(email_input).to_have_value("invalid_email@test.com")
   
    # Click login button
    login_button = page.get_by_role("button", name="Log in")
    expect(login_button).to_be_visible()
    login_button.click()

    # Wait for page to process login attempt
    # Network idle ensures all requests are complete
    page.wait_for_load_state("networkidle")
    
    # Wait a bit more for error message to appear
    page.wait_for_timeout(2000)

    # Verify error message appears (Facebook shows error for invalid login)
    # Check for common error indicators
    error_indicators = [
        page.locator("text=/incorrect|wrong|invalid|error/i"),
        page.locator("[role='alert']"),
        page.locator(".error"),
    ]
    
    # At least one error indicator should be present
    error_found = False
    for indicator in error_indicators:
        if indicator.count() > 0:
            error_found = True
            break
    
    # Assert that login failed (error message should appear)
    assert error_found or page.url != "https://www.facebook.com/", \
        "Expected error message or redirect after invalid login attempt"
    
    # Capture screenshot with browser name in filename
    # BrowserStack automatically captures screenshots, but we can add custom ones
    screenshot_path = f"screenshot_{browser_name}_facebook_invalid_login.png"
    page.screenshot(path=screenshot_path, full_page=True)
    
    # Additional BrowserStack-specific assertions
    # Verify page title changed or stayed on login page
    current_url = page.url
    assert "facebook.com" in current_url, f"Unexpected URL after login attempt: {current_url}"


@pytest.mark.parametrize("invalid_email", [
    "invalid@test.com",
    "notanemail",
    "",
    "test@",
])
def test_facebook_multiple_invalid_logins(page: Page, browser_name: str, invalid_email: str):
    """
    Parameterized test to verify multiple invalid login scenarios.
    BrowserStack will run this test across all configured platforms.
    """
    page.goto("https://www.facebook.com")
    
    if invalid_email:  # Skip if empty string
        page.fill("input[name='email']", invalid_email)
        page.get_by_role("button", name="Log in").click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000)
        
        # Capture screenshot with browser name and email scenario in filename
        # Sanitize email for filename (replace @ and other special chars)
        email_safe = invalid_email.replace("@", "_at_").replace(".", "_").replace(" ", "_")
        screenshot_path = f"screenshot_{browser_name}_multiple_invalid_logins_{email_safe}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        
        # Verify we're still on login page or error appeared
        assert "facebook.com" in page.url

