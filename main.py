import feedparser

def read_rss_feed(url):
    print(f"Đang tải RSS feed từ: {url}...\n")
    feed = feedparser.parse(url)

    # Chỉ báo lỗi khi không lấy được bài viết nào
    if not feed.entries:
        print("Lỗi: Không thể đọc feed hoặc feed không có dữ liệu.")
        if hasattr(feed, "bozo_exception"):
            print("Chi tiết lỗi:", feed.bozo_exception)
        return

    print(f"--- {feed.feed.get('title', 'Không có tiêu đề')} ---")
    print(f"Mô tả: {feed.feed.get('description', 'Không có mô tả')}")
    print(f"Link: {feed.feed.get('link', 'Không có link')}\n")
    print("-" * 40)

    # Lấy 5 bài viết mới nhất
    for entry in feed.entries[:5]:
        print(f"Tiêu đề: {entry.get('title', 'Không có tiêu đề')}")
        print(f"Link bài: {entry.get('link', 'Không có link')}")
        print(f"Ngày xuất bản: {entry.get('published', 'Không có ngày')}")
        print("-" * 40)

if __name__ == "__main__":
    # URL ví dụ từ VNExpress RSS
    rss_url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
    read_rss_feed(rss_url)