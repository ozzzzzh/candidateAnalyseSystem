from playwright.sync_api import sync_playwright
import os
import time

AUTH_FILE = "config/auth.json"

# 目录不存在就创建
os.makedirs(os.path.dirname(AUTH_FILE), exist_ok=True)
def login_and_save_auth(login_url="https://www.xiaohongshu.com"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print(">>> Opening login page ...")
        page.goto(login_url)

        print(">>> Please login manually (scan QR / phone login etc.)")
        print(">>> After login, wait until you see homepage, then press Enter.")

        input(">>> Press Enter here after login is finished...")

        # wait extra for tokens issue
        time.sleep(2)

        # Save cookies + localStorage + sessionStorage
        context.storage_state(path=AUTH_FILE)

        print(f">>> Login saved into {AUTH_FILE}")
        browser.close()


if __name__ == "__main__":
    login_and_save_auth()