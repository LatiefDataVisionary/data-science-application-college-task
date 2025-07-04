#!/usr/bin/env python
# coding: utf-8

# Soal 1: Bitcoin Price
# Kita memiliki daftar harga Bitcoin yang dicatat setiap akhir minggu (Minggu) di 2018 dan 
# 2019. Buat visualisasi yang memungkinkan Anda menjawab pertanyaan: Tahun apa, 
# 2018 atau 2019, yang cenderung memberikan pengembalian yang lebih baik bagi 
# pemegang Bitcoin? 

# In[ ]:



prices = [14292.2, 12858.9, 11467.5, 9241.1, 8559.6, 11073.5, 9704.3, 11402.3,
 8762.0, 7874.9, 8547.4, 6938.2, 6905.7, 8004.4, 8923.1, 9352.4,
 9853.5, 8459.5, 8245.1, 7361.3, 7646.6, 7515.8, 6505.8, 6167.3, 
 6398.9, 6765.5, 6254.8, 7408.7, 8234.1, 7014.3, 6231.6, 6379.1,
 6734.8, 7189.6, 6184.3, 6519.0, 6729.6, 6603.9, 6596.3, 6321.7,
 6572.2, 6494.2, 6386.2, 6427.1, 5621.8, 3920.4, 4196.2, 3430.4,
 3228.7, 3964.4, 3706.8, 3785.4, 3597.2, 3677.8, 3570.9, 3502.5,
 3661.4, 3616.8, 4120.4, 3823.1, 3944.3, 4006.4, 4002.5, 4111.8,
 5046.2, 5051.8, 5290.2, 5265.9, 5830.9, 7190.3, 7262.6, 8027.4,
 8545.7, 7901.4, 8812.5, 10721.7, 11906.5, 11268.0, 11364.9, 10826.7,
 9492.1, 10815.7, 11314.5, 10218.1, 10131.0, 9594.4, 10461.1, 10337.3,
 9993.0, 8208.5, 8127.3, 8304.4, 7957.3, 9230.6, 9300.6, 8804.5,
 8497.3, 7324.1, 7546.6, 7510.9, 7080.8, 7156.2, 7321.5, 7376.8]


# Penjelasan No 1
# 
# Chart apa yang anda pilih untuk problem diatas dan mengapa anda memilih chart 
# tersebut? 
# 
# Tahun berapa pemegang bitcoin memiliki keuntungan yang lebih banyak? 

# 

# Soal 2: Permen 
# Kita memiliki sekantong permen. Terdapat lima jenis permen, masing-masing diberi 
# nama di bawah ini. Buat diagram yang menunjukkan persentase peluang bahwa kita akan 
# mengeluarkan permen Snickers dari kantong jika kita melakukan pengambilan acak. 
# Sebutkan peluang memilih permen Snickers. 

# In[ ]:


candy_names = ['Kit Kat', 'Snickers', 'Milky Way', 'Toblerone', 'Twi x']
candy_counts = [52, 39, 78, 13, 78]


# Penjelsan No. 2
# 
# Chart apa yang anda pilih untuk problem diatas dan mengapa anda memilih chart 
# tersebut?
# 
# Berapa persen kemungkinan Anda akan memilih Snickers saat mengeluarkan permen 
# dari tas secara acak?

# Soal 3: Makanan 
# Restoran memiliki menu makanan penutup yang terlalu besar. Mereka ingin memotong 
# beberapa item dari menu. Untuk membuat sebagian besar pelanggan mereka senang, 
# mereka ingin menghapus hanya tiga makanan penutup yang paling tidak populer dari 
# menu. Kita memiliki daftar makanan penutup yang disajikan restoran, serta hitungan 
# berapa kali makanan penutup tersebut dijual dalam seminggu terakhir. Buat visualisasi 
# yang menunjukkan popularitas relatif dari makanan penutup. Sebutkan tiga makanan 
# penutup yang harus disingkirkan.

# In[ ]:


dessert_sales = {
 'Lava Cake': 14,
 'Mousse': 5,
 'Chocolate Cake': 12,
 'Ice Cream': 19,
 'Truffles': 6,
 'Brownie': 8,
 'Chocolate Chip Cookie': 12,
 'Chocolate Pudding': 9,
 'Souffle': 10,
 'Chocolate Cheesecake': 17,
 'Chocolate Chips': 2,
 'Fudge': 9,
 'Mochi': 13,
}


# Penjelasan No. 3
# 
# Chart apa yang anda pilih untuk problem diatas dan mengapa anda memilih chart 
# tersebut?
# 
# Makanan penutup apa saja yang perlu anda sarankan untuk dikeluarkan dari menu?

# Soal 4: Penggunaan CPU 
# Kita memiliki penggunaan CPU rata-rata per jam untuk komputer pekerja selama 
# seminggu. Setiap baris data mewakili satu hari dalam seminggu yang dimulai dengan 
# Senin. Setiap kolom data adalah satu jam dalam sehari dimulai dengan 0 menjadi tengah 
# malam. 
# Buat bagan yang menunjukkan penggunaan CPU selama seminggu. Anda harus dapat 
# menjawab pertanyaan-pertanyaan berikut menggunakan bagan: 
# • Jam berapa pekerja biasanya makan siang? 
# • Apakah pekerja tersebut bekerja pada akhir pekan? 
# • Pada hari apa pekerja mulai bekerja pada komputer mereka pada malam hari?

# In[ ]:


cpu_usage = [
 [2, 2, 4, 2, 4, 1, 1, 4, 4, 12, 22, 23, 45, 9, 33, 56, 23, 40, 21, 6, 6, 2, 2, 3], # Monday
 [1, 2, 3, 2, 3, 2, 3, 2, 7, 22, 45, 44, 33, 9, 23, 19, 33, 56, 12, 2, 3, 1, 2, 2], # Tuesday
 [2, 3, 1, 2, 4, 4, 2, 2, 1, 2, 5, 31, 54, 7, 6, 34, 68, 34, 49, 6, 6, 2, 2, 3], # Wednesday
 [1, 2, 3, 2, 4, 1, 2, 4, 1, 17, 24, 18, 41, 3, 44, 42, 12, 36, 41, 2, 2, 4, 2, 4], # Thursday
 [4, 1, 2, 2, 3, 2, 5, 1, 2, 12, 33, 27, 43, 8, 38, 53, 29, 45, 39, 3, 1, 1, 3, 4], # Friday
 [2, 3, 1, 2, 2, 5, 2, 8, 4, 2, 3, 1, 5, 1, 2, 3, 2, 6, 1, 2, 2, 1, 4, 3], # Saturday
 [1, 2, 3, 1, 1, 3, 4, 2, 3, 1, 2, 2, 5, 3, 2, 1, 4, 2, 45, 26, 33, 2, 2, 1], # Sunday
]


# Penjelasan No. 4
# 
# Chart apa yang anda pilih untuk problem diatas dan mengapa anda memilih chart 
# tersebut?
# 
# Jam berapa pekerja biasanya makan siang?
# 
# Apakah pekerja tersebut bekerja pada akhir pekan?
# 
# Pada hari apa pekerja mulai bekerja pada komputer mereka pada malam hari?

# Latihan 5: Jamur
# Seorang peneliti sedang mempelajari jamur. Mereka telah menemukan cincin jamur dan 
# memberi label koordinat. Biasanya jamur menyebar keluar dari pusat jamur awal.
# Dengan koordinat di bawah ini, peneliti ingin menjawab pertanyaan: Kira-kira di
# manakah letak pusat pertumbuhan jamur? Buat bagan yang memungkinkan peneliti 
# memperkirakan pusat pertumbuhan.

# In[ ]:


x = [4.61, 5.08, 5.18, 7.82, 10.46, 7.66, 7.6, 9.32, 14.04, 9.95, 4.95, 7.23, 
 5.21, 8.64, 10.08, 8.32, 12.83, 7.51, 7.82, 6.29, 0.04, 6.62, 13.16, 6.34, 
 0.09, 10.04, 13.06, 9.54, 11.32, 7.12, -0.67, 10.5, 8.37, 7.24, 
9.18, 10.12, 12.29, 8.53, 11.11, 9.65, 9.42, 8.61, -0.67, 5.94, 6.49, 
7.57, 3.11, 8.7, 5.28, 8.28, 9.55, 8.33, 13.7, 6.65, 2.4, 3.54, 9.19, 7.51, 
-0.68,
 8.47, 14.82, 5.31, 14.01, 8.75, -0.57, 5.35, 10.51, 3.11, -0.26
, 5.74,
 8.33, 6.5, 13.85, 9.78, 4.91, 4.19, 14.8, 10.04, 13.47, 3.28];
y = [-2.36, -3.41, 13.01, -2.91, -2.28, 12.83, 13.13, 11.94, 0.93, -2.76, 13.31,
 -3.57, -2.33, 12.43, -1.83, 12.32, -0.42, -3.08, -2.98, 12.46, 
8.34, -3.19,
 -0.47, 12.78, 2.12, -2.72, 10.64, 11.98, 12.21, 12.52, 5.53, 11.72, 12.91,
 12.56, -2.49, 12.08, -1.09, -2.89, -1.78, -2.47, 12.77, 12.41, 
5.33, -3.23,
 13.45, -3.41, 12.46, 12.1, -2.56, 12.51, -2.37, 12.76, 9.69, 12.59, -1.12,
 -2.8, 12.94, -3.55, 7.33, 12.59, 2.92, 12.7, 0.5, 12.57, 6.39, 
12.84,
 -1.95, 11.76, 6.82, 12.44, 13.28, -3.46, 0.7, -2.55, -2.37, 12.48, 7.26,
 -2.45, 0.31, -2.51]


# Penjelasan No. 5
# 
# Chart apa yang anda pilih untuk problem diatas dan mengapa anda memilih chart 
# tersebut?
# 
# Koordinat pusat (x,y) pusat pertumbuhan jamur berada di?
