# SPDS - Sistem Pendeteksi Slot Parkir

Sistem Pendeteksi Slot Parkir (SPDS) adalah sebuah aplikasi berbasis web yang dikembangkan menggunakan **Streamlit** dan **Convolutional Neural Network (CNN)** untuk mendeteksi apakah slot parkir dalam gambar terisi atau kosong. Sistem ini mendeteksi tiap slot parkir berdasarkan koordinat yang telah didefinisikan dan menampilkan hasilnya secara visual.

Dataset yang digunakan untuk melatih model berasal dari dataset [PKLot](https://www.kaggle.com/datasets/blanderbuss/parking-lot-dataset/), dimana kami mengambil data PKLotSegmented yang berisi potongan gambar tempat parkir yang diberikan label `empty` dan `occupied`.

---

## Anggota Kelompok
| NPM                    | Nama                     |
|------------------------|--------------------------|
| 140810230008           | Robby Azwan Saputra      |
| 140810230014           | Muhammad Zahran Muntazar |
| 140810230022           | Dafa Ghani Abdul Rabbani |

---

## Tujuan

Membangun sistem otomatis berbasis gambar yang mampu:
- Mendeteksi kondisi (kosong/terisi) dari slot parkir.
- Memberikan hasil deteksi dalam bentuk visualisasi interaktif.
- Mempermudah pemantauan area parkir secara efisien.

---

## Manfaat

- **Efisiensi Waktu:** Mengurangi waktu pencarian parkir secara manual.
- **Monitoring Real-Time:** Cocok untuk diintegrasikan dengan kamera CCTV.
- **Skalabilitas:** Dapat disesuaikan untuk berbagai konfigurasi area parkir.

---

## Penjelasan File

| Nama File              | Deskripsi                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `app.py`               | Script utama aplikasi Streamlit untuk deteksi slot parkir berbasis gambar. |
| `train_model.ipynb`    | Notebook Jupyter untuk training model CNN pada dataset parkir.            |
| `data_prep.py`         | Script untuk labeling dataset dan membagi data ke dalam train/test set.   |
| `parking_cnn_best.h5`  | Model CNN terbaik yang dihasilkan dari proses pelatihan.                  |

---

## Cara Menjalankan Aplikasi

1. **Pastikan dependensi sudah terinstall:**
   ```bash
   pip install -r requirements.txt

2. **Jalankan aplikasi Streamlit**
   ```bash
   streamlit run app.py
3. **Upload gambar parkiran (bisa dari folder [test_img](test_img))**