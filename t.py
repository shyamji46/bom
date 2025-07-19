from playwright.sync_api import sync_playwright
import time

def trigger_sms_loop(phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=False for debugging
        page = browser.new_page(viewport={"width": 360, "height": 640})
        page.goto("https://taskshare.live/#/pages/gs/invite?id=p5g57n", timeout=60000)

        # Scroll to find phone input
        phone_input_selector = 'input[placeholder*="phone"]'
        found = False
        for _ in range(10):
            if page.locator(phone_input_selector).count() > 0:
                found = True
                break
            page.mouse.wheel(0, 200)
            time.sleep(0.5)

        if not found:
            print("❌ Phone input field not found.")
            return

        # Fill phone number
        page.fill(phone_input_selector, phone)
        print("✅ Phone number filled.")

        # Click Get SMS button
        get_sms_button_selector = 'text=Get SMS'
        page.click(get_sms_button_selector)
        print("📩 First Get SMS clicked.")

        # Wait and loop to click Get SMS again every 62 seconds
        while True:
            time.sleep(62)
            try:
                page.click(get_sms_button_selector)
                print("🔁 Get SMS clicked again.")
            except Exception as e:
                print("❌ Error clicking Get SMS:", e)

        # This line is unreachable, but included for completeness
        browser.close()

# Example usage
trigger_sms_loop("7309369669")
