from playwright.sync_api import sync_playwright
import time

def trigger_playrummy_otp_loop(phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page(viewport={'width': 360, 'height': 640})
        page.goto("https://www.playrummy.com/", timeout=60000)

        # Step 1: Wait for and click Login
        try:
            page.wait_for_selector('text=Login', timeout=15000)
            page.click('text=Login')
            print("✅ Clicked Login")
        except Exception as e:
            print("❌ Login button not found:", e)
            return

        # Step 2: Wait for login popup
        page.wait_for_selector('input[placeholder="Enter Email/Mobile No.*"]', timeout=10000)
        page.fill('input[placeholder="Enter Email/Mobile No.*"]', phone)
        print(f"📱 Entered phone number: {phone}")

        # Step 3: Click Login/Register
        page.click("text=Login/Register")
        print("✅ Clicked Login/Register")

        # Step 4: Wait for OTP field
        page.wait_for_selector('input[placeholder="Enter OTP*"]', timeout=10000)
        print("⏳ Waiting 35 seconds before first OTP resend...")
        time.sleep(35)

        # Step 5: Loop resend OTP
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
