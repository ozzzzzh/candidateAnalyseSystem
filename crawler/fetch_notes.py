import os
import json
from playwright.sync_api import sync_playwright

AUTH_FILE = "config/auth.json"

def fetch_single_note(note_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 开发阶段可观察
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()

        note_data = {}

        # 🔥 捕获接口返回
        def handle_response(response):
            if f"/api/sns/web/v1/note/{note_id}" in response.url:  # 小红书真实笔记详情 API
                try:
                    data = response.json()
                    note = data.get("data", {})
                    interact_info = note.get("interact_info", {})
                    note_data.update({
                        "id": note.get("note_id"),
                        "title": note.get("display_title"),
                        "likes": int(interact_info.get("liked_count", 0)),
                        "collects": int(interact_info.get("collects", 0)),
                        "comments": int(interact_info.get("comments", 0))
                    })
                except:
                    pass
        
        page.on("response", handle_response)

        # 打开笔记页面
        url = f"https://www.xiaohongshu.com/explore/{note_id}"
        print("访问笔记：", url)
        page.goto(url, timeout=60000)

        page.wait_for_timeout(5000)  # 留时间让接口触发加载

        browser.close()

    return note_data

class NoteCrawler:
    FEED_API = "/api/sns/web/v1/feed"

    def __init__(self, context):
        self.page = context.new_page()
        self.result = None
        self.page.on("response", self.capture_feed)

    def capture_feed(self, response):
        if self.FEED_API in response.url:
            try:
                payload = response.json()
                items = payload.get("data", {}).get("items", [])
                if not items:
                    return
                note = items[0].get("note_card", {})
                self.result = {
                    "id": note.get("note_id"),
                    "title": note.get("title"),
                    "tags": [tag.get("name") for tag in note.get("tag_list", [])],
                    "desc": note.get("desc"),
                    "cover": note.get("image_list", [])[0].get("url_pre") if note.get("image_list") else None,
                    "likes": int(note.get("interact_info", {}).get("liked_count", 0)),
                    "collects": int(note.get("interact_info", {}).get("collected_count", 0)),
                    "comments": int(note.get("interact_info", {}).get("comment_count", 0)),
                    "time": note.get("time")
                }
            except:
                pass

    def fetch(self, note_id):
        url = f"https://www.xiaohongshu.com/explore/{note_id}"
        self.page.goto(url)
        self.page.wait_for_timeout(3000)
        return self.result

def fetchNotes(noteId, context):
    crawler = NoteCrawler(context)
    return crawler.fetch(noteId)

def fetch_notes(author_id, limit=10):
    result_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 开发阶段可观察
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()

        # 🔥 捕获接口返回
        def handle_response(response):
            if "/api/sns/web/v1/user_posted" in response.url:  # 小红书真实笔记列表 API
                try:
                    data = response.json()
                    for note in data.get("data", {}).get("notes", []):
                        interact_info = note.get("interact_info", {})
                        noteData = fetchNotes(note.get("note_id"), context)
                        result_data.append({
                            "id": note.get("note_id"),
                            "body": noteData,
                            "title": note.get("display_title"),
                            "likes": int(interact_info.get("liked_count", 0)),
                            "collects": int(interact_info.get("collects", 0)),
                            "comments": int(interact_info.get("comments", 0))
                        })
                        
                except:
                    pass
        
        page.on("response", handle_response)

        # 打开博主主页
        url = f"https://www.xiaohongshu.com/user/profile/{author_id}"
        print("访问主页：", url)
        page.goto(url, timeout=60000)

        # Removed click — rely on scrolling to trigger loading

        for _ in range(2):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(500)

        page.wait_for_timeout(80000)

        # page.wait_for_timeout(5000)  # 留时间让接口触发加载

        browser.close()

    # 截取最近 limit 条
    return result_data[:limit]


if __name__ == "__main__":
    # testUserId = 6246cc94000000001000d74b
    # testNoteLink = https://www.xiaohongshu.com/explore/68f1e55d0000000007001e14?xsec_token=ABGxQZ3dmrl8zE-77xmJCB_perW36IoK0VY13Nd0B_AME=&xsec_source=pc_user
    author = input("请输入小红书博主 ID： ")
    notes = fetch_notes(author)

    save_dir = "tempData/fetchData"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{author}.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
    print(f"数据已保存到: {save_path}")

    print("📌 获取结果：")
    print(json.dumps(notes, ensure_ascii=False, indent=2))