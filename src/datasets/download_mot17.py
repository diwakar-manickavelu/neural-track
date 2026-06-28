import kagglehub

# Download latest version
path = kagglehub.dataset_download("wenhoujinjust/mot-17")

print("Path to dataset files:", path)