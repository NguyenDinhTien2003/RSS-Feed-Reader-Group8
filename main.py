import feedparser

def read_rss_feed(url):
    print(f"Đang tải RSS feed từ: {url}...\n")
    feed = feedparser.parse(url)

    if feed.bozo == 1:
        print("Lỗi: Không thể đọc feed. Vui lòng kiểm tra lại URL.")
        return

    print(f"--- {feed.feed.title} ---")
    print(f"Mô tả: {feed.feed.get('description', 'Không có mô tả')}")
    print(f"Link: {feed.feed.link}\n")
    print("-" * 40)

    # Lấy 5 bài viết mới nhất
    for entry in feed.entries[:5]:
        print(f"Tiêu đề: {entry.title}")
        print(f"Link bài: {entry.link}")
        print(f"Ngày xuất bản: {entry.get('published', 'Không có ngày')}")
        print("-" * 40)

if __name__ == "__main__":
    # URL ví dụ từ VNExpress RSS
    rss_url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
    read_rss_feed(rss_url)