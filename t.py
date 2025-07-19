from playwright.sync_api import sync_playwright
import time

def trigger_playrummy_otp_loop(phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1366, 'height': 768})
        page.goto("https://www.playrummy.com/", timeout=60000)

        # Step 1: Click the Login button (top right corner)
        page.click("text=Login")
        print("✅ Clicked Login")

        # Step 2: Wait for login/register popup to appear
        page.wait_for_selector('input[placeholder="Enter Email/Mobile No.*"]')
        page.fill('input[placeholder="Enter Email/Mobile No.*"]', phone)
        print(f"📱 Entered phone number: {phone}")

        # Step 3: Click Login/Register
        page.click("text=Login/Register")
        print("✅ Clicked Login/Register")

        # Step 4: Wait for OTP field to appear
        page.wait_for_selector('input[placeholder="Enter OTP*"]')
        print("⏳ Waiting 35 seconds before first OTP resend...")
        time.sleep(35)

        # Step 5: Loop to click "Resend OTP" every 35 seconds
        while True:
            try:
                page.click("text=Resend OTP")
                print("🔁 Resend OTP clicked")
            except Exception as e:
                print("❌ Error clicking Resend OTP:", e)
            time.sleep(35)

        browser.close()

# Example usage
trigger_playrummy_otp_loop("7309369669")
