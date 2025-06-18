# ============================================================
# Program untuk mempersiapkan dataset PKLotSegmented
# ============================================================
# Kelompok 5
# Anggota:
# - 140810230008 | Robby Azwan Saputra 
# - 140810230014 | Muhammad Zahran Muntazar
# - 140810230022 | Dafa Ghani Abdul Rabbani
# ============================================================

import os
import shutil
from tqdm import tqdm

# ======== CONFIGURABLE PARAMETERS ========
source_root = 'PKLotSegmented'            # Folder asli dataset
target_dir = 'parking_data_5000'          # Output folder (ganti ke 'parking_data' untuk full dataset)
limit_debug = 5000                        # Set ke None untuk full dataset (hilangkan debug)

# ======== PERSIAPAN FOLDER TARGET ========
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

for split in ['train', 'valid']:
    for label in ['empty', 'occupied']:
        os.makedirs(os.path.join(target_dir, split, label), exist_ok=True)

# ======== MENGUMPULKAN FILE GAMBAR ========
empty_images = []
occupied_images = []

print("🔍 Mencari gambar...")
for root, dirs, files in os.walk(source_root):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            full_path = os.path.join(root, file)
            if 'empty' in root.lower():
                empty_images.append(full_path)
            elif 'occupied' in root.lower():
                occupied_images.append(full_path)

# ======== DEBUG MODE: AMBIL N FILE PERTAMA SAJA ========
if limit_debug:
    empty_images = sorted(empty_images)[:limit_debug]
    occupied_images = sorted(occupied_images)[:limit_debug]

# ======== SPLIT TRAIN/VALID ========
split_ratio = 0.8
split_empty = int(len(empty_images) * split_ratio)
split_occupied = int(len(occupied_images) * split_ratio)

# ======== COPY FILE ========
print(f"📦 Menyalin {len(empty_images)} gambar empty...")
for i, file in tqdm(enumerate(empty_images), total=len(empty_images), desc="Copying empty"):
    split = 'train' if i < split_empty else 'valid'
    dest_path = os.path.join(target_dir, split, 'empty', os.path.basename(file))
    shutil.copy(file, dest_path)

print(f"📦 Menyalin {len(occupied_images)} gambar occupied...")
for i, file in tqdm(enumerate(occupied_images), total=len(occupied_images), desc="Copying occupied"):
    split = 'train' if i < split_occupied else 'valid'
    dest_path = os.path.join(target_dir, split, 'occupied', os.path.basename(file))
    shutil.copy(file, dest_path)

# ======== DONE ========
print("✅ Selesai! Dataset tersedia di folder:", target_dir)
print(f"   Total empty: {len(empty_images)}")
print(f"   Total occupied: {len(occupied_images)}")
