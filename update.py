# update.py
import requests
import os
from jinja2 import Environment, FileSystemLoader
from config import API_ID, AFF_ID, SERVICE, FLOOR, HITS, SORT

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# APIエンドポイント
API_URL = "https://api.dmm.com/affiliate/v3/ItemList"

# DMM APIから商品データを取得
def fetch_items():
    params = {
        "api_id": API_ID,
        "affiliate_id": AFF_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "100",
        "sort": "rank"
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    print("API レスポンス:", data)  # ここでレスポンス確認
    if "result" not in data or "items" not in data["result"]:
        return []
    return data["result"]["items"]

# Jinja2テンプレートの読み込み
def load_template(template_name):
    env = Environment(loader=FileSystemLoader("templates"))
    return env.get_template(template_name)

os.makedirs("output/items", exist_ok=True)
print("output/items フォルダ作成済み")

# HTML生成
def generate_html():
    items = fetch_items()  # APIから取得

    # テンプレート読み込み
    index_template = load_template("index.html")
    item_template = load_template("item.html")

    # 出力先フォルダ作成
    os.makedirs("output/items", exist_ok=True)

    # index.html生成
    with open("output/index.html", "w", encoding="utf-8") as f:
    f.write(index_template.render(items=items))
    print("index.html 生成完了")

for item in items:
    content_id = item.get("content_id", "unknown")
    file_path = f"output/items/{content_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(item_template.render(item=item))
    print(f"{file_path} 生成完了")

    # 個別ページ生成
    for item in items:
        content_id = item.get("content_id", "unknown")
        file_path = f"output/items/{content_id}.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(item_template.render(item=item))

# メイン実行
if __name__ == "__main__":
    generate_html()

    print("サイト更新完了！")


