# GitHub Actionsで設定したSecretsから読み込む
API_ID = os.environ["DMM_API_ID"]
AFF_ID = os.environ["DMM_AFF_ID"]

# 取得するカテゴリ例（アダルト動画）
SERVICE = "digital"
FLOOR = "videoa"
HITS = 30
SORT = "rank"