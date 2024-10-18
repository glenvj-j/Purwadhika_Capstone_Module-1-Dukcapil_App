<h1>DUKCAPIL Kabupaten Bandung</h1>

for Educational Purpose Only

Background
Berawal dari rasa penasaran saat melihat nomor NIK di KTP, setelah mencari tau lebih jauh ternyata setiap angka di NIK bisa kita baca loh.
Kemudian saya mencoba untuk membuat program di Python untuk mengautomate proses pembacaan ini, setelah berhasil untuk membaca saya coba untuk reverse menjadi mengenerate dan sukses juga.

Dari sana saya kembangkan menjadi sebuah aplikasi yang tujuan akhirnya bisa mengikuti sistem dari dukcapil yang sebenarnya.
Pembuatan aplikasi ini hanya untuk keperluan penilaian capstone di Purwadhika.


Fitur
Aplikasi ini memiliki beberapa fitur utama yang terdiri dari

  1. Lihat Data Penduduk (READ)
  2. Tambahkan Data Penduduk (CREATE)
  3. Ubah Data Penduduk (UPDATE)
  4. Hapus Data Penduduk (DELETE)
  5. Cek Data dari NIK Asli (BONUS FEATURE)
  6. Admin (Restore Deleted dan Change Password)
  7. Tutup Program

Special Feature
  1.NIK Generator in CREATE Feature
    Using Gender, Place of Birth, and Date of Birth data, I can generate NIK just like a real NIK in our official KTP
  2.Read NIK from Real NIK
    Reversing the code from NIK generator, I can predict some of your information. Don't worry this program won't hold any confidental information
  3.Restore Deleted Data (Admin Menu)
    Even thought in Delete Menu already mentioned the data deleted cannot be retrive, I made this feature just in case for someone that 'accidentaly' delete the data.
    This feature works by using second database that hold deleted data, from that I can restore the data to main database by append

Flow Chart




Notes
Things to know before using the app:
password_user = "123456"
password_admin = "987654"

Di setiap menu bisa mengetik 'cancel' atau 'batal' jika ingin membatalkan operasi



Sumber Data
https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bandung
https://kodewilayah.id/
