<h1>DUKCAPIL Kabupaten Bandung</h1>
<sub>for Educational Purpose Only</sub>

<br>
<br>

<b>BACKGROUND</b>

All started from my curiosity when I saw the NIK number on the KTP, can we read this number?
After researching further, I found out that each digit in the NIK can actually be interpreted. From there I tried to create a program in Python to automate this reading process and I successfuly create the code.

On October 2024 I got the assignment to create capstone project from Purwadhika, I choose this Dukcapil app to expand my NIK Generator that I already created.

------------

<b>FEATURE</b>
<br>
<br>
Main Feature of this app:
  1. Lihat Data Penduduk (READ)
  2. Tambahkan Data Penduduk (CREATE)
  3. Ubah Data Penduduk (UPDATE)
  4. Hapus Data Penduduk (DELETE)
  5. Cek Data dari NIK Asli (BONUS FEATURE)
  6. Admin (Restore Deleted dan Change Password)
  7. Tutup Program

------------

<b>Special Feature</b>

  1.NIK Generator in CREATE Feature<br>
      Using Gender, Place of Birth, and Date of Birth data, I can generate NIK just like a real NIK in our official KTP<br>
      <br>
  2.Read NIK from Real NIK<br>
      Reversing the code from NIK generator, I can predict some of your information. Don't worry this program won't hold any confidental information<br>
      <br>
  3.Restore Deleted Data (Admin Menu)<br>
      Even thought in Delete Menu already mentioned the data deleted cannot be retrive, I made this feature just in case for someone that 'accidentaly' delete the data.
      This feature works by using second database that hold deleted data, from that I can restore the data to main database by append<br>

------------


Flow Chart


------------

> [!NOTE]
> password_user = "123456"<br>
> password_admin = "987654"<br>
> Type 'cancel' or 'batal' if you want to abort feature mid use


<br>
Source

[Wikipedia](https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bandung)<br>
[KodeWilayah](https://kodewilayah.id/)
