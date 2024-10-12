data_base_penduduk = [
    ["3204137004920004","Edis Hilvia","Bandung","30-04-92","Banjaran","Wanita"],
    ["3204136905050001","Kinasih Nur","Bandung","29-05-05","Margahayu","Wanita"],
    ["3204080502020001","Supriyono","Cilacap","05-02-02","Bojongsoang","Pria",],
    ["3204111212990001","Sulistyo","Cimahi","12-12-99","Katapang","Pria"],
    ["3204332501830001","Andi Kurniawan","Bandung","25-01-83","Majalaya","Pria"],
    ["3204115910500001","Devy Lesman","Bandung","19-10-50","Katapang","Wanita"],
    ]



#-----READ------------------------------------------------------------------------------------------------------------------------------------------------#

def menu_read():
    print('''
          
                    Lihat Data Penduduk
                    -------------------
        Menu :
          
        1.Tampilkan semua data
        2.Cari dari NIK
        3.Cari dari Kecamatan
        4.Kembali ke menu utama

''')

def header_tabel():
    print("="*137)
    print("║ NIK\t\t\t|Nama\t\t\t|Tempat Lahir\t\t|Tanggal Lahir\t\t|Kecamatan\t\t|Jenis Kelamin\t║")
    print("="*137)

def menu_lihat_data_penduduk():
    while True:
        try:
            menu_read()
            menu_choosen1 = int(input("Pilih Nomor yang diinginkan: ")) # inget ubah angka menu choosen nya
            if menu_choosen1 == 1:
                if len(data_base_penduduk) == 0:
                    print("\n")
                    print("----------------------\n!Database kosong!\n----------------------")
                else:
                    print("\n\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}\t\t║')
                    print("-"*137)
            elif menu_choosen1 == 2:
                input_NIK_checker = input("Masukkan NIK yang ingin dicari (16 digit angka): ")
                NIK_status = 0
                while True:
                    if len(input_NIK_checker) == 16 and input_NIK_checker.isnumeric:
                        break        
                    else:
                        print("Format salah, masukan 16 digit angka NIK")
                        input_NIK_checker = input("Masukkan NIK yang ingin dicari: ")
                if len(data_base_penduduk) == 0:
                    print("\n")
                    print("----------------------\n!Data base kosong!\n----------------------")
                else :
                    for i in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak,
                        if i[0] == input_NIK_checker:
                            NIK_status += True 
                            print("==NIK ditemukan di Database==")
                            print()
                        else:
                            continue
                    if NIK_status == 1:
                        print("Lanjut Proses Pengecekan....")
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        for j in data_base_penduduk:
                                if j[0] == input_NIK_checker:
                                    print(f'║ {i[0]}\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}\t\t║')
                                else:
                                     continue
                        print("-"*137)
                    elif NIK_status != 1:
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                    continue

            elif menu_choosen1 == 3:
                print("Menu mencari berdasarkan Kecamatan")
                input_kecamatan_checker = input("Masukkan kecamatan yang ingin dicari: ").capitalize()
                kecamatan_status = 0
                if len(data_base_penduduk) == 0:
                    print("\n")
                    print("----------------------\n!Data base kosong!\n----------------------")
                else :
                    for i in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak,
                        if i[4] == input_kecamatan_checker:
                            kecamatan_status += True 
                            print("==NIK ditemukan di Database==")
                            print()
                        else:
                            continue
                    if kecamatan_status >= 1:
                        print("Lanjut Proses Pengecekan....")
                        print("\n\t\t\t\t\t-= List Data Penduduk =-\n")
                        header_tabel()
                        for j in data_base_penduduk:
                                if j[4] == input_kecamatan_checker.capitalize():
                                    print(f'║ {j[0]}\t{j[1]}\t\t{j[2]}\t\t\t{j[3]}\t\t{j[4]}\t\t{j[5]}\t\t║')
                                else:
                                     continue
                        print("-"*137)
                    elif kecamatan_status != 1:
                        print("\n==Data kecamatan tidak ditemukan, kembali ke menu==")
                    continue
            elif menu_choosen1 == 4:
                print("Kembali ke menu utama>")
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")



#-----CREATE------------------------------------------------------------------------------------------------------------------------------------------------#

#-----NIK Generator
#===== Tanggal Lahir =====#
def convert_tanggal():
    global tanggal_lahir
    tanggal_lahir = ""
    tanggal_lahir = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
    while True:
        if len(tanggal_lahir) == 8 and "-" in tanggal_lahir:
            break        
        else:
            print("!Format salah, harap ikuti format yang benar!")
            tanggal_lahir = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
    tanggal_lahir_clean = tanggal_lahir.replace('-', '').replace('/','')
    return tanggal_lahir_clean

#===== Kecamatan =====#
dataKodeKecamatan = {
    "Cileunyi"      :	"320405",
    "Cimenyan"      :	"320406",
    "Cilengkrang"   :	"320407",
    "Bojongsoang"   :	"320408",
    "Margahayu"     :	"320409",
    "Margaasih"     :	"320410",
    "Katapang"      :	"320411",
    "Dayeuhkolot"   :	"320412",
    "Banjaran"      :	"320413",
    "Pameungpeuk"   :	"320414",
    "Pangalengan"   :	"320415",
    "Arjasari"      :	"320416",
    "Cimaung"       :	"320417",
    "Cicalengka"    :	"320425",
    "Nagreg"        :	"320426",
    "Cikancung"     :	"320427",
    "Rancaekek"     :	"320428",
    "Ciparay"       :	"320429",
    "Pacet"         :	"320430",
    "Kertasari"     :	"320431",
    "Baleendah"     :	"320432",
    "Majalaya"      :	"320433",
    "Solokanjeruk"  :	"320434",
    "Paseh"         :	"320435",
    "Ibun"          :	"320436",
    "Soreang"       :	"320437",
    "Pasirjambu"    :	"320438",
    "Ciwidey"       :	"320439",
    "Rancabali"     :	"320440",
    "Cangkuang"     :	"320444",
    "Kutawaringin"  :	"320446"
    }

def convert_kecamatan():
    global kecamatan
    kecamatan = ""
    kecamatan = input("Masukan Kecamatan yang sesuai : ")
    while True:
        if kecamatan.capitalize() in dataKodeKecamatan:
            kecamatan_to_kode = dataKodeKecamatan.get(kecamatan.capitalize()) 
            return kecamatan_to_kode
        else:
            print("!Kecamatan tidak ditemukan dalam database!")
            kecamatan = input("Harap Masukan Kecamatan yang sesuai : ")

def NIK_Generator():
    hasilkecamatan = convert_kecamatan()
    global JenisKelamin
    JenisKelamin = ""
    jenis_kelamin_input = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
    while True:
        if jenis_kelamin_input.lower() == "pria" or jenis_kelamin_input.lower() == "wanita":
            JenisKelamin += jenis_kelamin_input
            break
        else :
            print("Mohon pilih antara Pria/Wanita!")
            jenis_kelamin_input = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
    hasiltanggal = convert_tanggal()
    kodeakhir = "0001"
    if JenisKelamin == 'wanita':
        kode_wanita = int(hasiltanggal[0:2])+40
        hasiltanggal = str(kode_wanita) + hasiltanggal[2:]
        return hasilkecamatan+hasiltanggal+kodeakhir
    else:  
        return hasilkecamatan+hasiltanggal+kodeakhir


#==================================


def menu_create():
    print('''
          
                    Tambahkan Data Penduduk
                    -----------------------
        Menu :
          
        1.Tambahkan Data Penduduk
        2.Kembali ke menu utama

''')

def menu_tambahkan_data_penduduk():
    while True:
        try:
            menu_create()
            menu_choosen2 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen2 == 1:
                new_data_temp = []
                print()
                input_nama = input("Masukkan Nama (max 15 huruf & min 8): ") #max 15 <<----- NAMA
                while True :
                    if len(input_nama) <= 15 and len(input_nama)>=8:
                        break
                    else:
                        print("!Format salah, masukan max 15 huruf!")
                        input_nama = input("Masukkan Nama (max 15 huruf & min 8): ") #max 15
                tempat_lahir = input("Masukkan Tempat Lahir (max 7 char): ") #max 7 <<----- tempat lahir
                while True :
                    if len(tempat_lahir) <= 7 and tempat_lahir.isalpha():
                        break
                    else:
                        print("!Format salah, masukan max 7 huruf & tanpa angka!")
                        tempat_lahir = input("Masukkan Tempat Lahir (max 7 char): ")
                NIK_generated = NIK_Generator() # <<----- tanggal lahir, kecamatan, jenis kelamin
                NIK_checker = True
                for l in data_base_penduduk: #menentukan apakah ada NIK di dalam list atau tidak,
                        if l[0] == NIK_generated:
                            NIK_checker = False 
                            print()
                            print("\t\t==NIK sudah ada di Database==")
                            break
                        else:
                            continue
                if NIK_checker == True: 
                    print()     
                    print("-=Preview data yang telah dimasukkan=- ")
                    ktp_layout = f'''
=================================================

  NIK : {NIK_generated.capitalize()}
  Nama : {input_nama.capitalize()}
  Tmpt/Tgl Lahir : {tempat_lahir.capitalize()},{tanggal_lahir}\t\U0001f600
  Alamat : {kecamatan.capitalize()}
  {JenisKelamin.capitalize()}

=================================================
'''
                    print(ktp_layout)
                    jawaban_save_create = input("Apakah anda ingin menyimpan data (Y/N)? ")
                    if jawaban_save_create.lower() == "y":
                        new_data_temp = [NIK_generated,input_nama.capitalize(),tempat_lahir.capitalize(),tanggal_lahir,kecamatan.capitalize(),JenisKelamin.capitalize()]
                        data_base_penduduk.append(new_data_temp)
                        print("Data Berhasil di Simpan!")
                    else:
                        print("Operasi dibatalkan, kembali ke menu...")
                        continue
                else:
                    continue
            elif menu_choosen2 == 2:
                print("Kembali ke menu utama>")
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")


#-----UPDATE------------------------------------------------------------------------------------------------------------------------------------------------#


def menu_update():
    print('''
          
                    Ubah Data Penduduk
                    ------------------
        Menu :
          
        1.Ubah Data Penduduk
        2.Kembali ke menu utama

''')
    
def menu_update_data_penduduk():
    while True:
        try:
            menu_update()
            menu_choosen3 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen3 == 1:
                if len(data_base_penduduk) == 0:
                    print("\n")
                    print("----------------------\n!Database kosong!\n----------------------")
                else:
                    print()
                    print("\n\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}\t\t║')
                    print("-"*137)
                    NIK_input_update = input("Masukan NIK yang ingin ubah : ")
                    NIK_status = 0
                    while True:
                        if len(NIK_input_update) == 16 and NIK_input_update.isnumeric:
                            break        
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_input_update = input("Masukkan NIK yang ingin diubah: ")
                    print()
                    temp_choosen_update = ""
                    for k in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if k[0] == NIK_input_update:
                            NIK_status += True
                            temp_choosen_update = k
                            index_siap_update = data_base_penduduk.index(k) #ambil index yang bakal dihapus
                            print("==Data ditemukan dalam database==")
                            print()
                        else:
                            continue
                    if NIK_status == 1:
                        print("Lanjut Proses Pengecekan....")
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_update[0]}\t{temp_choosen_update[1]}\t\t{temp_choosen_update[2]}\t\t\t{temp_choosen_update[3]}\t\t{temp_choosen_update[4]}\t\t{temp_choosen_update[5]}\t\t║')
                        print("-"*137)
                        print("\n")
                        #mulai update di sini
                        pilihan_choosen_update = input("Data mana yang ingin diubah? : ")
                        index_pilihan = 0
                        if pilihan_choosen_update.lower() == "nama":
                            print()
                            print("Ubah Nama Terpilih")
                            x_input_baru = input("Masukkan Nama (max 15 huruf & min 8): ")
                            while True :
                                if len(x_input_baru) <= 15 and len(x_input_baru)>=8:
                                    break
                                else:
                                    print("Format salah, max 15 huruf & min 8")
                                    x_input_baru = input("Masukkan Nama (max 15 huruf & min 8): ") #max 15
                            index_pilihan = 1
                        elif pilihan_choosen_update.lower() == "tempat lahir":
                            print()
                            print("Ubah Tempat Lahir Terpilih")
                            x_input_baru = input("Masukkan Tempat Lahir (max 7 char): ")
                            while True :
                                if len(x_input_baru) <= 7 and x_input_baru.isalpha():
                                    break
                                else:
                                    print("Format salah, max 7 huruf")
                                    x_input_baru = input("Masukkan Tempat Lahir (max 7 char): ") #max 15
                            index_pilihan = 2
                        elif pilihan_choosen_update.lower() == "tanggal lahir":
                            print()
                            print("Ubah Tanggal Lahir Terpilih")
                            x_input_baru = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
                            while True :
                                if len(x_input_baru) == 8 and "-" in x_input_baru:
                                    break
                                else:
                                    print("!Format salah, harap ikuti format yang benar!")
                                    x_input_baru = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
                            index_pilihan = 3
                        elif pilihan_choosen_update.lower() == "kecamatan":
                            print()
                            print("Ubah Kecamatan Terpilih")
                            x_input_baru = input("Harap Masukan Kecamatan yang sesuai : ")
                            while True :
                                if x_input_baru.capitalize() in dataKodeKecamatan:
                                    break
                                else:
                                    print("!Kecamatan tidak ditemukan dalam database!")
                                    x_input_baru = input("Harap Masukan Kecamatan yang sesuai : ")
                            index_pilihan = 4
                        elif pilihan_choosen_update.lower() == "jenis kelamin":
                            print()
                            print("Ubah Jenis Kelamin Terpilih")
                            x_input_baru = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                            while True :
                                if x_input_baru.lower() == "pria" or x_input_baru.lower() == "wanita":
                                    break
                                else:
                                    print("Mohon pilih antara Pria/Wanita!")
                                    x_input_baru = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                            index_pilihan = 5
                            
                        else:
                            print("Pilihan Tidak Tersedia")
                            continue

                        jawaban_update = input("Apakah anda yakin ingin mengubah data (Y/N)? ")
                        if jawaban_update.lower() == "y":
                            data_base_penduduk[index_siap_update][index_pilihan] = x_input_baru
                            print("Data Berhasil di ubah!")
                            print()
                        else:
                            print()
                            print("Operasi dibatalkan, kembali ke menu...")
                            continue

                    elif NIK_status != 1:
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                    continue
                            
            elif menu_choosen3 == 2:
                print("Kembali ke menu utama>")
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")


#-----DELETE------------------------------------------------------------------------------------------------------------------------------------------------#


def menu_delete():
    print('''
          
                    Hapus Data Penduduk
                    -------------------
        Menu :
          
        1.Hapus Data Penduduk
        2.Kembali ke menu utama

''')
    
def menu_hapus_data_penduduk():
    while True:
        try:
            menu_delete()
            menu_choosen4 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen4 == 1:
                if len(data_base_penduduk) == 0:
                    print("\n")
                    print("----------------------\n!Database kosong!\n----------------------")
                else:
                    print("\n\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}\t\t║')
                    print("-"*137)
                    NIK_input_delete = input("Masukan NIK yang ingin dihapus : ")
                    NIK_status = 0
                    while True:
                        if len(NIK_input_delete) == 16 and NIK_input_delete.isnumeric:
                            break        
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_input_delete = input("Masukkan NIK yang ingin dihapus: ")
                    print()
                    temp_choosen_delete = ""
                    for o in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if o[0] == NIK_input_delete:
                            NIK_status += True
                            temp_choosen_delete = o
                            index_siap_delete = []
                            index_siap_delete = data_base_penduduk.index(o) #ambil index yang bakal dihapus
                            print("==Data ditemukan dalam database==")
                            print()
                        else:
                            continue
                    if NIK_status == 1:
                        print("Lanjut Proses Pengecekan....")
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_delete[0]}\t{temp_choosen_delete[1]}\t\t{temp_choosen_delete[2]}\t\t\t{temp_choosen_delete[3]}\t\t{temp_choosen_delete[4]}\t\t{temp_choosen_delete[5]}\t\t║')
                        print("-"*137)
                        print("\n")
                        jawaban_delete = input("Apakah anda yakin ingin menghapus data?\nData yang sudah dihapus tidak dapat dikembalikan!! (Y/N) ")
                        if jawaban_delete.lower() == "y":
                            data_base_penduduk.pop(index_siap_delete)
                            print()
                            print("Data Berhasil dihapus!")
                            print()
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            continue

                    
                    elif NIK_status != 1:
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                    continue
                            
            elif menu_choosen4 == 2:
                print("Kembali ke menu utama>")
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")

#-----NIK READER BONUS FEATURE------------------------------------------------------------------------------------------------------------------------------------------------#

database_kode_wilayah = {"11" : "Aceh","12" : "Sumatera Utara","13" : "Sumatera Barat","16" : "Sumatera Selatan","14" : "Riau","21" : "Kepulauan Riau","15" : "Jambi","17" : "Bengkulu","18" : "Lampung","19" : "Bangka Belitung","31" : "DKI Jakarta",
                         "36" : "Banten","32" : "Jawa Barat","33" : "Jawa Tengah","34" : "DI Yogyakarta","35" : "Jawa Timur","51" : "Bali","61" : "Kalimantan Barat","62" : "Kalimantan Tengah","63" : "Kalimantan Selatan","64" : "Kalimantan Timur",
                         "65" : "Kalimantan Utara","52" : "Nusa Tenggara Barat","53" : "Nusa Tenggara Timur","71" : "Sulawesi Utara","72" : "Sulawesi Tengah","73" : "Sulawesi Selatan","74" : "Sulawesi Tenggara","75" : "Gorontalo","76" : "Sulawesi Barat",
                         "81" : "Maluku","82" : "Maluku Utara","91" : "Papua","92" : "Papua Barat",}


def NIK_reader():
    print()
    NIK = input("Masukan NIK anda dan akan muncul detail KTP anda : ")
    kode_wilayah = database_kode_wilayah.get(NIK[0:2])
    JenisKelamin = ""

    if int(NIK[6:8]) > 31:
        tanggal = int(NIK[6:8])-40
        JenisKelamin += "Wanita"
    else : 
        tanggal = NIK[6:8]
        JenisKelamin = "Pria"

    list_bulan = ["Januari", "Februari","Maret","April","May","Juni","Juli","Agustus","September","Oktober","November","Desember"]

    bulan = list_bulan[int(NIK[8:10])-1]

    if int(NIK[10:12]) > 40: tahun = "19" + str(NIK[10:12])
    else : tahun = "20" + str(NIK[10:12])

    jumlah_orang = int(NIK[14:16:1])
    print()
    print("-"*120)
    print(f'|\tKamu adalah seorang {JenisKelamin} dengan domisili {kode_wilayah} dan orang ke {jumlah_orang} yang lahir di tanggal {tanggal} {bulan} {tahun}\t|')
    print("-"*120)

#-----MAIN PROGRAM------------------------------------------------------------------------------------------------------------------------------------------------#

def menu_utama():
    print('''
          ======================================================
          Selamat datang di sistem DISDUKCAPIL Kota Bandung v1.0
          ======================================================

          List Program :

          1.Lihat Data Penduduk
          2.Tambahkan Data Penduduk
          3.Ubah Data Penduduk
          4.Hapus Data Penduduk
          5.Cek Data dari NIK Kamu
          6.Tutup Program

          
          --------= Sehat Selalu untuk Kita Semua =--------
          ''')

menu_choosen = 0
def main_program():
    while True:
        menu_utama()
        try:
            menu_choosen   = int(input("Pilih Menu yang ingin dijalankan : "))
            if menu_choosen   == 1:
                menu_choosen1 = 0
                menu_lihat_data_penduduk()
            elif menu_choosen   == 2:
                menu_choosen2 = 0
                menu_tambahkan_data_penduduk()
            elif menu_choosen   == 3:
                menu_update_data_penduduk()
            elif menu_choosen   == 4:
                menu_hapus_data_penduduk()
            elif menu_choosen   == 5:
                NIK_reader()
            elif menu_choosen == 6:
                print()
                print("-=Program ditutup, sampai jumpa lagi!=-")
                print()
                break
            else:
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)
                
        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")

main_program()