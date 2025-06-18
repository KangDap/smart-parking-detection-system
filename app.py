# ============================================================
# Aplikasi Streamlit untuk Deteksi Slot Parkir dari Gambar
# ============================================================
# Kelompok 5
# Anggota:
# - 140810230008 | Robby Azwan Saputra 
# - 140810230014 | Muhammad Zahran Muntazar
# - 140810230022 | Dafa Ghani Abdul Rabbani
# ============================================================

import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Set up Streamlit page
st.set_page_config(page_title="SPDS - Gambar", page_icon="🖼️", layout="wide")
st.title("SPDS - Deteksi Parkir dari Gambar")

# Load model
model = load_model("parking_cnn_best.h5")

# Koordinat slot parkir
area_list = {
    1: [(18, 656), (48, 656), (48, 700), (18, 700)],
    2: [(58, 656), (88, 656), (88, 700), (58, 700)],
    3: [(98, 656), (128, 656), (128, 700), (98, 700)],
    4: [(138, 656), (178, 656), (178, 700), (138, 700)],
    5: [(188, 656), (228, 656), (228, 700), (188, 700)],
    6: [(238, 656), (278, 656), (278, 700), (238, 700)],
    7: [(288, 656), (328, 656), (328, 700), (288, 700)],
    8: [(338, 656), (378, 656), (378, 700), (338, 700)],
    9: [(388, 656), (428, 656), (428, 700), (388, 700)],
    10: [(438, 656), (478, 656), (478, 700), (438, 700)],
    11: [(488, 656), (528, 656), (528, 700), (488, 700)],
    12: [(538, 656), (578, 656), (578, 700), (538, 700)],
    13: [(608, 646), (628, 646), (628, 690), (608, 690)],
    14: [(638, 656), (678, 656), (678, 700), (638, 700)],
    15: [(688, 656), (728, 656), (728, 700), (688, 700)],
    16: [(738, 656), (778, 656), (778, 700), (738, 700)],
    17: [(8, 506), (28, 506), (28, 550), (8, 550)],
    18: [(38, 506), (68, 506), (68, 550), (38, 550)],
    19: [(78, 506), (108, 506), (108, 550), (78, 550)],
    20: [(118, 506), (158, 506), (158, 550), (118, 550)],
    21: [(158, 506), (198, 506), (198, 550), (158, 550)],
    22: [(198, 506), (238, 506), (238, 550), (198, 550)],
    23: [(248, 506), (278, 506), (278, 550), (248, 550)],
    24: [(288, 506), (318, 506), (318, 550), (288, 550)],
    25: [(338, 506), (368, 506), (368, 550), (338, 550)],
    26: [(378, 506), (408, 506), (408, 550), (378, 550)],
    27: [(418, 506), (448, 506), (448, 550), (418, 550)],
    28: [(458, 506), (498, 506), (498, 550), (458, 550)],
    29: [(508, 506), (538, 506), (538, 550), (508, 550)],
    30: [(548, 506), (578, 506), (578, 550), (548, 550)],
    31: [(588, 506), (628, 506), (628, 550), (588, 550)],
    32: [(638, 506), (678, 506), (678, 550), (638, 550)],
    33: [(688, 506), (728, 506), (728, 550), (688, 550)],
    34: [(738, 506), (778, 506), (778, 550), (738, 550)],
    35: [(788, 506), (828, 506), (828, 550), (788, 550)],
    36: [(838, 506), (878, 506), (878, 550), (838, 550)],
    37: [(888, 496), (948, 496), (948, 540), (888, 540)],
    38: [(900, 550), (952, 550), (952, 590), (900, 590)],
    39: [(910, 590), (970, 590), (970, 630), (910, 630)],
    40: [(920, 630), (988, 630), (988, 670), (920, 670)],
    41: [(888, 440), (922, 440), (922, 485), (888, 485)],
    42: [(848, 430), (882, 430), (882, 485), (848, 485)],
    43: [(808, 430), (842, 430), (842, 485), (808, 485)],
    44: [(768, 430), (802, 430), (802, 485), (768, 485)],
    45: [(728, 430), (762, 430), (762, 485), (728, 485)],
    46: [(688, 425), (722, 425), (722, 480), (688, 480)],
    47: [(648, 425), (682, 425), (682, 480), (648, 480)],
    48: [(618, 425), (642, 425), (642, 480), (618, 480)],
    49: [(578, 425), (612, 425), (612, 480), (578, 480)],
    50: [(538, 425), (572, 425), (572, 480), (538, 480)],
    51: [(498, 425), (532, 425), (532, 480), (498, 480)],
    52: [(468, 425), (492, 425), (492, 480), (468, 480)],
    53: [(433, 420), (457, 420), (457, 470), (433, 470)],
    54: [(400, 420), (424, 420), (424, 470), (400, 470)],
    55: [(362, 420), (391, 420), (391, 470), (362, 470)],
    56: [(329, 420), (358, 420), (358, 470), (329, 470)],
    57: [(296, 420), (325, 420), (325, 470), (296, 470)],
    58: [(246, 420), (275, 420), (275, 470), (246, 470)],
    59: [(208, 420), (237, 420), (237, 470), (208, 470)],
    60: [(175, 420), (204, 420), (204, 470), (175, 470)],
    61: [(142, 420), (171, 420), (171, 470), (142, 470)],
    62: [(115, 420), (138, 420), (138, 470), (115, 470)],
    63: [(81, 420), (110, 420), (110, 470), (81, 470)],
    64: [(48, 420), (77, 420), (77, 470), (48, 470)],
    65: [(15, 420), (44, 420), (44, 470), (15, 470)],
}

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar parkiran (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    # Baca gambar
    img = Image.open(uploaded_file).convert("RGB")
    frame = np.array(img)
    frame = cv2.resize(frame, (1020, 720))

    occupied_slots = []

    # Proses setiap area parkir
    for area_num, points in area_list.items():
        x_min = min(p[0] for p in points)
        x_max = max(p[0] for p in points)
        y_min = min(p[1] for p in points)
        y_max = max(p[1] for p in points)

        crop = frame[y_min:y_max, x_min:x_max]
        if crop.shape[0] == 0 or crop.shape[1] == 0:
            continue

        crop_resized = cv2.resize(crop, (54, 32))
        crop_normalized = crop_resized.astype('float32') / 255.0
        input_tensor = np.expand_dims(crop_normalized, axis=0)

        # Prediksi model
        prediction = model.predict(input_tensor, verbose=False)
        prob_occupied = prediction[0][0] if prediction.shape[-1] == 1 else prediction[0][1]
        pred_label = 1 if prob_occupied > 0.5 else 0

        # Gambar poligon dan label
        if pred_label == 1:
            occupied_slots.append(area_num)
            color = (0, 0, 255)  # merah
        else:
            color = (0, 255, 0)  # hijau

        cv2.polylines(frame, [np.array(points, np.int32)], True, color, 2)
        cv2.putText(frame, str(area_num), points[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    all_points = [pt for pts in area_list.values() for pt in pts]
    x1 = min(p[0] for p in all_points)
    x2 = max(p[0] for p in all_points)
    y1 = min(p[1] for p in all_points)
    y2 = max(p[1] for p in all_points)

    padding = 25
    x1 = max(0, x1 - padding)
    x2 = min(frame.shape[1], x2 + padding)
    y1 = max(0, y1 - padding)
    y2 = min(frame.shape[0], y2 + padding)

    cropped_frame = frame[y1:y2, x1:x2]

    # Tampilkan
    st.image(cropped_frame, caption="Deteksi Slot Parkir (Merah: Terisi, Hijau: Kosong)", channels="BGR")
    st.success(f"Total slot: {len(area_list)} | Terisi: {len(occupied_slots)} | Kosong: {len(area_list) - len(occupied_slots)}")
