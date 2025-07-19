from playwright.sync_api import sync_playwright
import time

def trigger_rummycircle_otp_call(phone):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 360, 'height': 640})
        page.goto("https://bountygame1.com/#/register?invitationCode=145742767323/")

        # Fill phone number
        page.fill('input[placeholder="Please enter the phone number"]', phone)

        # Click Get Started
        page.click('text=Send')

        print("📲 OTP sent to", phone)
        time.sleep(63)

        # Loop: keep clicking "Get OTP on call" every 63 seconds
        while True:
            try:
                page.click('text=Send')
                print("📞 Get OTP on Call clicked again")
            except Exception as e:
                print("❌ Error clicking OTP on call:", e)
            time.sleep(31)

        browser.close()

# Example
trigger_rummycircle_otp_call("7309369669")
