from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 可视模式
    page = browser.new_page()
    page.goto("https://www.xiaohongshu.com/")
    print(page.title())
    browser.close()