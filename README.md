<h1>DUKCAPIL Kabupaten Bandung</h1>
<sub>for Educational Purpose Only</sub>

<br>
<br>


> [!NOTE]
> password_user = "123456"    |    password_admin = "987654"<br>
> Type 'cancel' or 'batal' if you want to abort feature mid use

<br>

<b>BACKGROUND</b>

All started from my curiosity when I saw the NIK number on the KTP, I am askinh myself can we read this number?
After researching further, I found out that each digit in the NIK can actually be interpreted. From there I tried to create a program in Python to automate this reading process and I successfuly create the code.

On October 2024 I got the assignment to create capstone project from Purwadhika, I choose this Dukcapil app to expand my NIK Generator that I already created.

------------

<b>FEATURE</b>
<br>
<br>
Main Feature of this app:
  1. Lihat Data Penduduk (READ)<br>
  &nbsp;&nbsp;Showing all data in database also you can search by NIK or Kecamatan
  3. Tambahkan Data Penduduk (CREATE)<br>
  &nbsp;&nbsp;Adding New Data to database, got 2 option to add NIK manually or by generated
  5. Ubah Data Penduduk (UPDATE)<br>
  &nbsp;&nbsp;Updating Data on database, you can also choose what column to change
  6. Hapus Data Penduduk (DELETE)<br>
  &nbsp;&nbsp;Delete by NIK or Name (by name you required to type the exact name)
  7. Cek Data dari NIK Asli (BONUS FEATURE)<br>
  &nbsp;&nbsp;Read you real NIK and get the reading result
  8. Admin (Restore Deleted dan Change Password)<br>
  &nbsp;&nbsp;You can change user password, restore deleted data, and delete all data at once
  9. Tutup Program<br>
  &nbsp;&nbsp;Sayonara

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
![Flow1](https://github.com/user-attachments/assets/abf6ac44-9e6a-4444-8745-7db97b9e472f)
![Flow2](https://github.com/user-attachments/assets/b6a89af6-b852-46bb-a923-dad668ed2dde)
![Flow3](https://github.com/user-attachments/assets/94a94bc4-131a-45a6-b51a-95f392b253a4)
![Flow4](https://github.com/user-attachments/assets/b4e7a449-d2cf-4166-a81f-ea081a091564)
![Flow5](https://github.com/user-attachments/assets/8084ddab-d1f9-4733-8684-233fc86dae8f)
![Flow6](https://github.com/user-attachments/assets/4101a16c-72d8-415a-b49f-fe3340f3ac43)


--------



<br>
Source

[Wikipedia](https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bandung)<br>
[KodeWilayah](https://kodewilayah.id/)
