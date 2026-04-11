from huggingface_hub import HfApi

api = HfApi()
repo_id = "wangkevin02/SASLM-demo-audio"  # 改成你的

# 上传整个目录
api.upload_folder(
    folder_path="./emotion",
    repo_id=repo_id,
    repo_type="dataset",
    path_in_repo="emotion"  # HF上的目录名
)

api.upload_folder(
    folder_path="./open_domain",
    repo_id=repo_id,
    repo_type="dataset",
    path_in_repo="open_domain"
)