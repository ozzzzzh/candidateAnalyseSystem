import os
import json
from playwright.sync_api import sync_playwright

AUTH_FILE = "config/auth.json"

def fetchNoteByClick(authorId, limit = 10):
    resultData = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 开发阶段可观察
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()

        def handleClickResponse(response):
            if "/api/sns/web/v1/feed" in response.url:
                try:
                    payload = response.json()
                    items = payload.get("data", {}).get("items", [])
                    for item in items:
                        note = item.get("note_card", {})
                        resultData.append({
                            "id": note.get("note_id"),
                            "title": note.get("title"),
                            "tags": [tag.get("name") for tag in note.get("tag_list", [])],
                            "desc": note.get("desc"),
                            "cover": note.get("image_list", [])[0].get("url_pre") if note.get("image_list") else None,
                            "likes": int(note.get("interact_info", {}).get("liked_count", 0)),
                            "collects": int(note.get("interact_info", {}).get("collected_count", 0)),
                            "comments": int(note.get("interact_info", {}).get("comment_count", 0)),
                            "time": note.get("time")
                        })
                except:
                    pass
        
        page.on("response", handleClickResponse)
        url = f"https://www.xiaohongshu.com/user/profile/{authorId}"
        print("访问主页：", url)
        page.goto(url, timeout=60000)

        page.wait_for_selector(".note-item")  #! AI
        
        cards = page.locator(".note-item")
        # for i in range(limit):
        #     page.click(cards[i])  # 点击第一个笔记预览
        #     page.wait_for_timeout(3000)  # 等待接口返回

        clicked = 0 #! AI
        for i in range(limit):
            if i >= cards.count():
                break
            # 滚动卡片可见
            cards.nth(i).scroll_into_view_if_needed()
            # 点击
            cards.nth(i).click()
            page.wait_for_timeout(1500)  # 给 feed 请求时间
            clicked += 1
            # 返回上一页 (防止卡片打开详情页覆盖主列表)
            page.go_back()
            page.wait_for_selector(".note-item")

        browser.close()
    return resultData[:clicked]

if __name__ == "__main__":
    # testUserId = 6246cc94000000001000d74b
    # testNoteLink = https://www.xiaohongshu.com/explore/68f1e55d0000000007001e14?xsec_token=ABGxQZ3dmrl8zE-77xmJCB_perW36IoK0VY13Nd0B_AME=&xsec_source=pc_user
    author = input("请输入小红书博主 ID： ")
    notes = fetchNoteByClick(author)

    save_dir = "tempData/fetchData"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{author}.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
    print(f"数据已保存到: {save_path}")

    print("📌 获取结果：")
    print(json.dumps(notes, ensure_ascii=False, indent=2))