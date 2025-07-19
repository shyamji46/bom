from playwright.sync_api import sync_playwright
import time

def trigger_sms_loop(phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to run in background
        page = browser.new_page(viewport={"width": 360, "height": 640})
        page.goto("https://taskshare.live/#/pages/gs/invite?id=p5g57n", timeout=60000)

        # Scroll to find the phone input field
        phone_input_selector = 'input[placeholder*="phone"], input[type="tel"]'
        get_sms_selector = 'text=Get SMS'

        found = False
        for _ in range(10):
            if page.locator(phone_input_selector).count() > 0:
                found = True
                break
            page.mouse.wheel(0, 300)
            time.sleep(0.5)

        if not found:
            print("❌ Phone input field not found.")
            browser.close()
            return

        # Fill the phone number
        page.fill(phone_input_selector, phone)
        print(f"✅ Phone number filled: {phone}")

        # Click on "Get SMS"
        try:
            page.click(get_sms_selector)
            print("📩 Clicked 'Get SMS'")
        except Exception as e:
            print("❌ Failed to click 'Get SMS':", e)
            browser.close()
            return

        # Loop: click "Get SMS" every 62 seconds
        while True:
            time.sleep(62)
            try:
                page.click(get_sms_selector)
                print("🔁 Clicked 'Get SMS' again")
            except Exception as e:
                print("❌ Failed to click 'Get SMS' again:", e)

# Example usage
trigger_sms_loop("7309369669")
