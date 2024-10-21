import time




#-----DATABASE------------------------------------------------------------------------------------------------------------------------------------------------#

data_base_penduduk = [
    ["3204137004920001","Edis Hilvia","Bandung","30-04-92","banjaran","Wanita"],
    ["3204096905050001","Kinasih Nur","Bandung","29-05-05","Margahayu","Wanita"],
    ["3204080502020001","Supriyono","Cilacap","05-02-02","Bojongsoang","Pria",],
    ["3204111212990001","Sulistyo","Cimahi","12-12-99","Katapang","Pria"],
    ["3204332501830001","Andi Kurniawan","Bandung","25-01-83","Majalaya","Pria"],
    ["3204115910500001","Devy Lesman","Bandung","19-10-50","Katapang","Wanita"],
    ]

data_base_penduduk_deleted = [
    ["3204081912450001","Adris Inar","Bandung","19-12-45","Bojongsoang","Pria"]
    ]

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




#-----AESTHETIC------------------------------------------------------------------------------------------------------------------------------------------------#

def header_tabel():
    print("="*137)
    print("║ NIK\t\t\t|Nama\t\t\t|Tempat Lahir\t\t|Tanggal Lahir\t\t|Kecamatan\t\t|Jenis Kelamin\t║")
    print("="*137)

def loading():
    print()
    keyword = 'Memuat...'
    for i in keyword:
        print(i,end='', flush=True)
        time.sleep(0.1)
    print('\n\n\n')

def separator():
    print('-'*100)

#-----1 READ------------------------------------------------------------------------------------------------------------------------------------------------#

def menu_read():
    print('''
                   -----------------------
                   | Lihat Data Penduduk |
                   -----------------------
        Menu :
          
        1.Tampilkan Semua Data
        2.Cari dari NIK
        3.Cari dari Kecamatan
        4.Kembali ke Menu Utama

''')

def menu_lihat_data_penduduk():
    while True:
        try:
            menu_read()
            menu_choosen1 = int(input("Pilih Nomor yang diinginkan: ")) #choose what you want to do
            if menu_choosen1 == 1: #tampilkan semua data
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to read menu
                    print("\n")
                    print("-----------------\n!Database kosong!\n-----------------")
                    separator()
                else:
                    loading()
                    print("\n\t\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                    print("-"*137)
                    print("\n")
            elif menu_choosen1 == 2: #cari dari NIK
                input_NIK_checker = input("Masukkan NIK yang ingin dicari (16 digit angka): ")
                if input_NIK_checker == "cancel" or input_NIK_checker == "batal" : #abort function
                    print()
                    print("Operasi dibatalkan, kembali ke menu...")
                    separator()
                    break
                while True: #checking input, if true continue to next line
                    if len(input_NIK_checker) == 16 and input_NIK_checker.isnumeric:
                        break        
                    else:
                        print("Format salah, masukan 16 digit angka NIK")
                        input_NIK_checker = input("Masukkan NIK yang ingin dicari: ")
                NIK_status = False #storing true or false in data is in database
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to read menu
                    print("\n")
                    print("----------------------\n!Data base kosong!\n----------------------")
                else :
                    for i in data_base_penduduk: #checking data in database, if found update value NIK_status
                        if i[0] == input_NIK_checker:
                            NIK_status += True
                            print()
                        else:
                            continue
                    if NIK_status == True: #show data yang sesuai dengan NIK
                        print("==NIK ditemukan di Database==")
                        print()
                        print("Lanjut Proses Pengecekan")
                        loading()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        for j in data_base_penduduk:
                                if j[0] == input_NIK_checker:
                                    print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                                else:
                                     continue
                        print("-"*137)
                        print("\n\n\n")
                        separator()
                    elif NIK_status == False:
                        loading()
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                        print("\n\n\n")
                        separator()
                    continue

            elif menu_choosen1 == 3:
                input_kecamatan_checker = input("Masukkan kecamatan yang ingin dicari: ").lower()
                kecamatan_status = 0
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to read menu
                    print("\n")
                    print("----------------------\n!Data base kosong!\n----------------------")
                else :
                    for i in data_base_penduduk: #checking data in database, if found update value kecamatan_status
                        if i[4].lower() == input_kecamatan_checker:
                            kecamatan_status += True
                            print()
                        else:
                            continue
                    if kecamatan_status >= 1: #show data yang sesuai dengan NIK
                        print("Lanjut Proses Pengecekan....")
                        print(f"=={kecamatan_status} data ditemukan dalam database==")
                        loading()
                        print("\n\t\t\t\t\t-= List Data Penduduk =-\n")
                        header_tabel()
                        for j in data_base_penduduk:
                                if j[4].lower() == input_kecamatan_checker:
                                    print(f'║ {j[0]}\t{j[1].capitalize()}\t\t{j[2].capitalize()}\t\t\t{j[3]}\t\t{j[4].capitalize()}\t\t{j[5].capitalize()}\t\t║')
                                else:
                                     continue
                        print("-"*137)
                    elif kecamatan_status != 1:
                        print("\n==Data kecamatan tidak ditemukan, kembali ke menu==")
                        separator()
                    continue
            elif menu_choosen1 == 4:
                print("Kembali ke Menu Utama>")
                separator()
                break
            else : #show this if input not 1-4
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError: #show this if input other than number
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")



#-----2 CREATE------------------------------------------------------------------------------------------------------------------------------------------------#

#-----NIK Generator
#===== Tanggal Lahir =====#
def convert_tanggal():
    global tanggal_lahir #to be used in create function for preview
    tanggal_lahir = ""
    tanggal_lahir = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")
    while True: #long rules to make sure input of tanggal lahir right
        if len(tanggal_lahir) == 8 and "-" in tanggal_lahir and tanggal_lahir.count("-") == 2 and tanggal_lahir[0:2].isnumeric() and int(tanggal_lahir[0:2]) < 32 and tanggal_lahir[3:5].isnumeric() and int(tanggal_lahir[3:5]) < 13 and tanggal_lahir[6:8].isnumeric() and tanggal_lahir[2] == "-" and tanggal_lahir[5] == "-":
            break        
        else:
            print("!Format salah, harap ikuti format yang benar!")
            tanggal_lahir = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")
    while True:
        if int(tanggal_lahir[6:8]) < 8 or int(tanggal_lahir[6:8]) > 24:
            break
        else:
            print("Umur anda belum cukup, minimal umur 17 tahun")
            tanggal_lahir = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")
    tanggal_lahir_clean = tanggal_lahir.replace('-', '').replace('/','')
    return tanggal_lahir_clean #to be used for NIK Generator

#===== Kecamatan =====#

def convert_kecamatan():
    global kecamatan #to be used in create function for preview
    kecamatan = input("Masukan Kecamatan yang sesuai : ")
    while True:
        if kecamatan.capitalize() in dataKodeKecamatan:
            kecamatan_to_kode = dataKodeKecamatan.get(kecamatan.capitalize()) 
            return kecamatan_to_kode
        else:
            print("!Kecamatan tidak ditemukan dalam database!")
            kecamatan = input("Harap Masukan Kecamatan yang sesuai : ")

    
def NIK_Generator(): #combining kecamatan and jenis kelamin to generate NIK
    hasilkecamatan = convert_kecamatan()
    global JenisKelamin #to be used in create function for preview
    JenisKelamin = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
    while True:
        if JenisKelamin.lower() == "pria" or JenisKelamin.lower() == "wanita":
            break
        else :
            print("Mohon pilih antara Pria/Wanita!")
            JenisKelamin = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
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
                   ---------------------------
                   | Tambahkan Data Penduduk |
                   ---------------------------
        
        Menu :
          
        1.Tambahkan Data Penduduk (NIK Manual)
        2.Tambahkan Data Penduduk (NIK Auto Generated)
        3.Kembali ke Menu Utama

''')

def menu_tambahkan_data_penduduk():
    while True:
        try:
            menu_create()
            menu_choosen2 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen2 == 1: #tambahkan data penduduk start
                if menu_choosen2 == 1: #tambahkan data penduduk start
                    new_data_temp = [] #storing all input data before add to main database
                    NIK_manual_input = input("Masukan NIK yang kamu inginkan : ") #NIK
                    while True:
                        if len(NIK_manual_input) == 16 and NIK_manual_input.isnumeric:
                            break 
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_manual_input = input("Masukan NIK yang kamu inginkan : ")
                    NIK_checker = True
                    for z in data_base_penduduk: #menentukan apakah ada NIK di dalam list atau tidak, if found duplicate will break
                        if z[0] == NIK_manual_input:
                            NIK_checker = False 
                            print("\n\n\n")
                            print("\t\t==NIK sudah ada di Database==")
                            print("\n\n")
                            separator()
                            break
                        else:
                            continue
                    if NIK_checker == True: 
                        input_nama_manual = input("Masukkan Nama (min 8 & max 15 huruf): ").capitalize() #input nama
                        if input_nama_manual == "cancel" or input_nama_manual == "batal" : #abort function
                            print()
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            break
                        while True : #checking input
                            if len(input_nama_manual) <= 15 and len(input_nama_manual)>=8: #checking nama input, must be between 8 and 15
                                break
                            else:
                                print("!Format salah, masukan min 8 & max 15 huruf!")
                                input_nama_manual = input("Masukkan Nama (min 8 & max 15 huruf): ") 
                        
                        tempat_lahir_manual = input("Masukkan Tempat Lahir (max 7 huruf): ") #input tempat lahir   
                        if tempat_lahir_manual == "cancel" or tempat_lahir_manual == "batal" :  #abort function
                            print()
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            break
                        while True : #checking input tempat lahir
                            if len(tempat_lahir_manual) <= 7 and tempat_lahir_manual.isalpha(): #checking tempat lahir input
                                break
                            else:
                                print("!Format salah, masukan max 7 huruf & tanpa angka!")
                                tempat_lahir_manual = input("Masukkan Tempat Lahir (max 7 huruf): ")
                    
                        tanggal_lahir_manual = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")
                        while True: #long rules to make sure input of tanggal lahir right
                            if len(tanggal_lahir_manual) == 8 and "-" in tanggal_lahir_manual and tanggal_lahir_manual.count("-") == 2 and tanggal_lahir_manual[0:2].isnumeric() and int(tanggal_lahir_manual[0:2]) < 32 and tanggal_lahir_manual[3:5].isnumeric() and int(tanggal_lahir_manual[3:5]) < 13 and tanggal_lahir_manual[6:8].isnumeric() and tanggal_lahir_manual[2] == "-" and tanggal_lahir_manual[5] == "-":
                                break        
                            else:
                                print("!Format salah, harap ikuti format yang benar!")
                                tanggal_lahir_manual = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")
                        while True:
                            if int(tanggal_lahir_manual[6:8]) < 8 or int(tanggal_lahir_manual[6:8]) > 24:
                                break
                            else:
                                print("Umur anda belum cukup, minimal umur 17 tahun")
                                tanggal_lahir_manual = input("Masukkan Tanggal Lahir dengan format cth. (20-10-90) : ")

                        kecamatan_manual = input("Masukan Kecamatan yang sesuai : ")
                        while True:
                            if kecamatan_manual.capitalize() in dataKodeKecamatan:
                                break
                            else:
                                print("!Kecamatan tidak ditemukan dalam database!")
                                kecamatan_manual = input("Harap Masukan Kecamatan yang sesuai : ")
                        JenisKelamin_manual = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                        while True :
                            if JenisKelamin_manual == "pria" or JenisKelamin_manual == "wanita":
                                break
                            else:
                                print("Mohon pilih antara Pria/Wanita!")
                                JenisKelamin_manual = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                        loading()
                        print("-=Preview data yang telah dimasukkan=- ") #preview from inputed data
                        ktp_layout = f'''
=================================================

NIK : {NIK_manual_input.capitalize()}
Nama : {input_nama_manual.capitalize()}
Tmpt/Tgl Lahir : {tempat_lahir_manual.capitalize()},{tanggal_lahir_manual}\t\U0001f600
Kecamatan : {kecamatan_manual.capitalize()}
{JenisKelamin_manual.capitalize()}

=================================================
'''         
                        print(ktp_layout)
                        jawaban_save_create = input("Apakah anda ingin menyimpan data (Y/N)? ") #prompt to save or not
                        if jawaban_save_create.lower() == "y":
                            new_data_temp = [NIK_manual_input,input_nama_manual.capitalize(),tempat_lahir_manual.capitalize(),tanggal_lahir_manual,kecamatan_manual.capitalize(),JenisKelamin_manual.capitalize()]
                            data_base_penduduk.append(new_data_temp)
                            print("Data Berhasil di Simpan!")
                            separator()
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            continue
                    else:
                        continue
            elif menu_choosen2 == 2: #tambahkan data penduduk start
                new_data_temp = [] #storing all input data before add to main database
                print()
                input_nama = input("Masukkan Nama (min 8 & max 15 huruf): ").capitalize() #input nama
                if input_nama == "cancel" or input_nama == "batal" : #abort function
                    print()
                    print("Operasi dibatalkan, kembali ke menu...")
                    separator()
                    break
                while True : #checking input
                    if len(input_nama) <= 15 and len(input_nama)>=8: #checking nama input, must be between 8 and 15
                        break
                    else:
                        print("!Format salah, masukan min 8 & max 15 huruf!")
                        input_nama = input("Masukkan Nama (min 8 & max 15 huruf): ") 
                tempat_lahir = input("Masukkan Tempat Lahir (max 7 huruf): ") #input tempat lahir
                if tempat_lahir == "cancel" or tempat_lahir == "batal" :  #abort function
                    print()
                    print("Operasi dibatalkan, kembali ke menu...")
                    separator()
                    break
                while True : #checking input tempat lahir
                    if len(tempat_lahir) <= 7 and tempat_lahir.isalpha(): #checking tempat lahir input
                        break
                    else:
                        print("!Format salah, masukan max 7 huruf & tanpa angka!")
                        tempat_lahir = input("Masukkan Tempat Lahir (max 7 huruf): ")
                NIK_generated = NIK_Generator() # <<----- generate tanggal lahir, kecamatan, jenis kelamin
                NIK_checker = True
                for l in data_base_penduduk: #menentukan apakah ada NIK di dalam list atau tidak, if found duplicate will break
                    if l[0] == NIK_generated:
                        NIK_checker = False 
                        print("\n\n\n")
                        print("\t\t==NIK sudah ada di Database==")
                        print("\n\n")
                        separator()
                        break
                    else:
                        continue
                if NIK_checker == True: 
                    print()     
                    loading()
                    print("-=Preview data yang telah dimasukkan=- ") #preview from inputed data
                    ktp_layout = f'''
=================================================

  NIK : {NIK_generated.capitalize()}
  Nama : {input_nama.capitalize()}
  Tmpt/Tgl Lahir : {tempat_lahir.capitalize()},{tanggal_lahir}\t\U0001f600
  Kecamatan : {kecamatan.capitalize()}
  {JenisKelamin.capitalize()}

=================================================
'''
                    print(ktp_layout)
                    jawaban_save_create = input("Apakah anda ingin menyimpan data (Y/N)? ") #prompt to save or not
                    if jawaban_save_create.lower() == "y":
                        new_data_temp = [NIK_generated,input_nama.capitalize(),tempat_lahir.capitalize(),tanggal_lahir,kecamatan.capitalize(),JenisKelamin.capitalize()]
                        data_base_penduduk.append(new_data_temp)
                        print("Data Berhasil di Simpan!")
                        separator()
                    else:
                        print("Operasi dibatalkan, kembali ke menu...")
                        separator()
                        continue
                else:
                    continue
            elif menu_choosen2 == 3:
                print("Kembali ke Menu Utama>")
                separator()
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")


#-----3 UPDATE------------------------------------------------------------------------------------------------------------------------------------------------#


def menu_update():
    print('''
                   ----------------------
                   | Ubah Data Penduduk |
                   ----------------------
          
        Menu :
          
        1.Ubah Data Penduduk
        2.Kembali ke Menu Utama
          

''')
    
def menu_update_data_penduduk():
    while True:
        try:
            menu_update()
            menu_choosen3 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen3 == 1: #ubah data penduduk
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to update menu
                    print("\n")
                    print("-----------------\n!Database kosong!\n-----------------")
                    separator()
                else:
                    print()
                    loading()
                    print("\n\t\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                    print("-"*137)
                    print()
                    NIK_input_update = input("Masukan NIK yang ingin ubah : ")
                    if NIK_input_update == "cancel" or NIK_input_update == "batal" : #untuk cancel kalau ga jadi ngisi
                        print()
                        print("Operasi dibatalkan, kembali ke menu...")
                        separator()
                        break
                    while True:
                        if len(NIK_input_update) == 16 and NIK_input_update.isnumeric:
                            break 
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_input_update = input("Masukkan NIK yang ingin diubah: ")
                    print()
                    NIK_status = False #storing true or false the nik found in database
                    temp_choosen_update = "" #storing choosen data that will be updated for preview purpose
                    for k in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if k[0] == NIK_input_update:
                            NIK_status += True
                            temp_choosen_update = k
                            index_siap_update = data_base_penduduk.index(k) #ambil index yang bakal diupdate
                            print()
                        else:
                            continue
                    if NIK_status == True:
                        print("==Data ditemukan dalam database==")
                        print()
                        print("Lanjut Proses Pengecekan")
                        loading()
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_update[0]}\t{temp_choosen_update[1].capitalize()}\t\t{temp_choosen_update[2].capitalize()}\t\t\t{temp_choosen_update[3]}\t\t{temp_choosen_update[4].capitalize()}\t\t{temp_choosen_update[5].capitalize()}\t\t║')
                        print("-"*137)
                        print("\n")
                        jawaban_update_after_preview = input("Apakah anda ingin melanjutkan ubah data (Y/N)? ")
                        if jawaban_update_after_preview.lower() == "y":
                            print("Lanjut Proses")
                            print("\n")
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            print("\n\n")
                            break
                        pilihan_choosen_update = input("Data mana yang ingin diubah? : ") #mulai update di sini
                        if pilihan_choosen_update == "cancel" or pilihan_choosen_update == "batal" :
                            print()
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            print("\n\n")
                            break
                        index_pilihan = 0 #storing which index will be updated
                        if pilihan_choosen_update.lower() == "nama":
                            print()
                            print("==Ubah Nama Terpilih==")
                            print()
                            x_input_baru = input("Masukkan Nama (max 15 huruf & min 8): ")
                            while True :
                                if len(x_input_baru) <= 15 and len(x_input_baru)>=8:
                                    break
                                else:
                                    print("Format salah, max 15 huruf & min 8")
                                    x_input_baru = input("Masukkan Nama (max 15 huruf & min 8): ") #max 15
                            index_pilihan = 1 #index nama
                        elif pilihan_choosen_update.lower() == "tempat lahir" or pilihan_choosen_update.lower() == "tempat":
                            print()
                            print("==Ubah Tempat Lahir Terpilih==")
                            print()
                            x_input_baru = input("Masukkan Tempat Lahir (max 7 huruf): ")
                            while True :
                                if len(x_input_baru) <= 7 and x_input_baru.isalpha():
                                    break
                                else:
                                    print("Format salah, max 7 huruf")
                                    x_input_baru = input("Masukkan Tempat Lahir (max 7 huruf): ") #max 15
                            index_pilihan = 2 #index tempat lahir
                        elif pilihan_choosen_update.lower() == "tanggal lahir" or pilihan_choosen_update.lower() == "tanggal":
                            print()
                            print("==Ubah Tanggal Lahir Terpilih==")
                            print()
                            x_input_baru = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
                            while True :
                                if len(x_input_baru) == 8 and "-" in x_input_baru and x_input_baru.count("-") == 2 and x_input_baru[0:2].isnumeric and x_input_baru[3:5].isnumeric and x_input_baru[6:8].isnumeric and x_input_baru[2] == "-" and x_input_baru[5] == "-" and int(x_input_baru[0:2]) < 32 and x_input_baru[3:5].isnumeric() and int(x_input_baru[3:5]) < 13:
                                    break
                                else:
                                    print("!Format salah, harap ikuti format yang benar!")
                                    x_input_baru = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
                            while True:
                                if int(x_input_baru[6:8]) < 8 or int(x_input_baru[6:8]) > 24:
                                    break
                                else:
                                    print("Umur anda belum cukup, minimal umur 17 tahun")
                                    x_input_baru = input("Masukkan dengan Format Tanggal cth. (20-10-90) : ")
                            index_pilihan = 3 #index tanggal lahir
                        elif pilihan_choosen_update.lower() == "kecamatan":
                            print()
                            print("==Ubah Kecamatan Terpilih==")
                            print()
                            x_input_baru = input("Harap Masukan Kecamatan yang sesuai : ")
                            while True :
                                if x_input_baru.capitalize() in dataKodeKecamatan:
                                    break
                                else:
                                    print("!Kecamatan tidak ditemukan dalam database!")
                                    x_input_baru = input("Harap Masukan Kecamatan yang sesuai : ")
                            index_pilihan = 4 #index kecamatan
                        elif pilihan_choosen_update.lower() == "jenis kelamin":
                            print()
                            print("==Ubah Jenis Kelamin Terpilih==")
                            print()
                            x_input_baru = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                            while True :
                                if x_input_baru.lower() == "pria" or x_input_baru.lower() == "wanita":
                                    break
                                else:
                                    print("Mohon pilih antara Pria/Wanita!")
                                    x_input_baru = input("Masukan Jenis Kelamin (Pria/Wanita) : ")
                            index_pilihan = 5 #index jenis kelamin
                        elif pilihan_choosen_update.upper() == "NIK":
                            print()
                            print("-=Mohon maaf nomor NIK tidak bisa diubah=-")
                            continue
                        else: #if user input other than choice
                            print()
                            print("Pilihan Tidak Tersedia")
                            separator()
                            continue

                        jawaban_update = input("Apakah anda yakin ingin mengubah data (Y/N)? ") #prompt to save the update or not
                        if jawaban_update.lower() == "y":
                            data_base_penduduk[index_siap_update][index_pilihan] = x_input_baru #choose index data and which index will be updated
                            loading()
                            print("Data Berhasil di ubah!")
                            print()
                            print("\n\n\n")
                            separator()
                        else:
                            print()
                            print("Operasi dibatalkan, kembali ke menu...")
                            print("\n\n\n")
                            separator()
                            continue

                    elif NIK_status == False:
                        loading()
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                        print("\n\n\n")
                        separator()
                    continue
                            
            elif menu_choosen3 == 2:
                print("Kembali ke Menu Utama>")
                print("\n\n\n")
                separator()
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)
                print("\n\n\n")
                separator()

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")


#-----4 DELETE------------------------------------------------------------------------------------------------------------------------------------------------#


def menu_delete():
    print('''
                   -----------------------
                   | Hapus Data Penduduk |
                   -----------------------
          
        Menu :
          
        1.Hapus Data Penduduk
        2.Hapus menggunakan Nama
        3.Kembali ke Menu Utama
          

''')
    
def menu_hapus_data_penduduk():
    while True:
        try:
            menu_delete()
            menu_choosen4 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen4 == 1: #hapus data penduduk by NIK
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to delete menu
                    print("\n")
                    print("-----------------\n!Database kosong!\n-----------------")
                    separator()
                else:
                    loading()
                    print("\n\t\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                    print("-"*137)
                    print()
                    NIK_input_delete = input("Masukan NIK yang ingin dihapus : ")
                    if NIK_input_delete == "cancel" or NIK_input_delete == "batal": #abort function
                        print()
                        print("Operasi dibatalkan, kembali ke menu...")
                        separator()
                        break
                    
                    while True:
                        if len(NIK_input_delete) == 16 and NIK_input_delete.isnumeric:
                            break        
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_input_delete = input("Masukkan NIK yang ingin dihapus: ")
                    print()
                    
                    NIK_status = False #storing true or false the nik found in database
                    temp_choosen_delete = "" #storing choosen data that will be deleted for preview purpose
                    for o in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if o[0] == NIK_input_delete:
                            NIK_status += True
                            temp_choosen_delete = o
                            index_siap_delete = data_base_penduduk.index(o) #ambil index yang bakal dihapus
                            print()
                        else:
                            continue
                    if NIK_status == True:
                        print("==Data ditemukan dalam database==")
                        print()
                        print("Lanjut Proses Pengecekan")
                        loading()
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_delete[0]}\t{temp_choosen_delete[1].capitalize()}\t\t{temp_choosen_delete[2].capitalize()}\t\t\t{temp_choosen_delete[3]}\t\t{temp_choosen_delete[4].capitalize()}\t\t{temp_choosen_delete[5].capitalize()}\t\t║')
                        print("-"*137)
                        print("\n")
                        jawaban_delete = input("Apakah anda yakin ingin menghapus data?\nData yang sudah dihapus tidak dapat dikembalikan!! (Y/N) ") #prompt to delete data
                        if jawaban_delete.lower() == "y":
                            data_base_penduduk_deleted.append(data_base_penduduk[index_siap_delete])
                            data_base_penduduk.pop(index_siap_delete)
                            loading()
                            print()
                            print("Data Berhasil dihapus!")
                            print()
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            continue

                    
                    elif NIK_status == False:
                        print("\n==Data NIK tidak ditemukan, kembali ke menu==")
                        separator()
                    continue
                            
            elif menu_choosen4 == 2:   #hapus data penduduk by Nama
                if len(data_base_penduduk) == 0: #cheking if data exist in database, if not will back to delete menu
                    print("\n")
                    print("-----------------\n!Database kosong!\n-----------------")
                    separator()
                else:
                    loading()
                    print("\n\t\t\t\t\t\t-= Daftar Data Penduduk =-\n")
                    header_tabel()
                    for i in data_base_penduduk:
                                print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                    print("-"*137)
                    print()
                    nama_input_delete = input("Masukan Nama yang ingin dihapus : ").lower().rstrip()
                    if nama_input_delete == "cancel" or nama_input_delete == "batal" :
                        print()
                        print("Operasi dibatalkan, kembali ke menu...")
                        separator()
                        break
                    print()
                    nama_status = False #storing true or false the nik found in database
                    temp_choosen_delete = "" #storing choosen data that will be deleted for preview purpose
                    for r in data_base_penduduk: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if r[1].lower() == nama_input_delete:
                            nama_status += True
                            temp_choosen_delete = r
                            index_siap_delete = data_base_penduduk.index(r) #ambil index yang bakal dihapus
                            print()
                        else:
                            continue
                    if nama_status == True:
                        print("==Data ditemukan dalam database==")
                        print()
                        print("Lanjut Proses Pengecekan")
                        loading()
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_delete[0]}\t{temp_choosen_delete[1].capitalize()}\t\t{temp_choosen_delete[2].capitalize()}\t\t\t{temp_choosen_delete[3]}\t\t{temp_choosen_delete[4].capitalize()}\t\t{temp_choosen_delete[5].capitalize()}\t\t║')
                        print("-"*137)
                        print("\n")
                        jawaban_delete = input("Apakah anda yakin ingin menghapus data?\nData yang sudah dihapus tidak dapat dikembalikan!! (Y/N) ") #prompt to delete data
                        if jawaban_delete.lower() == "y":
                            data_base_penduduk_deleted.append(data_base_penduduk[index_siap_delete]) #storing deleted data to recyle bin database
                            data_base_penduduk.pop(index_siap_delete) #delete selected index
                            print()
                            print("Data Berhasil dihapus!")
                            print("\n\n\n")
                            separator()
                            print()
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            print("\n\n\n")
                            separator()
                            continue                    
                    elif nama_status == False:
                        print("\n==Nama tidak ditemukan, harap mengetik sesuai nama di database, kembali ke menu==")
                        print("\n\n\n")
                        separator()
                    continue
                            
            elif menu_choosen4 == 3:
                print("Kembali ke Menu Utama>")
                separator()
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)
                print("\n\n\n")
                separator()

        except ValueError:
            print("\n")
            print("Harap mengisi dengan angka!\n---------------------------")

#-----5 NIK READER BONUS FEATURE------------------------------------------------------------------------------------------------------------------------------------------------#

database_kode_wilayah = {"11" : "Aceh","12" : "Sumatera Utara","13" : "Sumatera Barat","16" : "Sumatera Selatan","14" : "Riau","21" : "Kepulauan Riau","15" : "Jambi","17" : "Bengkulu","18" : "Lampung","19" : "Bangka Belitung","31" : "DKI Jakarta",
                         "36" : "Banten","32" : "Jawa Barat","33" : "Jawa Tengah","34" : "DI Yogyakarta","35" : "Jawa Timur","51" : "Bali","61" : "Kalimantan Barat","62" : "Kalimantan Tengah","63" : "Kalimantan Selatan","64" : "Kalimantan Timur",
                         "65" : "Kalimantan Utara","52" : "Nusa Tenggara Barat","53" : "Nusa Tenggara Timur","71" : "Sulawesi Utara","72" : "Sulawesi Tengah","73" : "Sulawesi Selatan","74" : "Sulawesi Tenggara","75" : "Gorontalo","76" : "Sulawesi Barat",
                         "81" : "Maluku","82" : "Maluku Utara","91" : "Papua","92" : "Papua Barat",}


def NIK_reader():
    try :  
        print('''
                   --------------------------
                   | Cek Data dari NIK kamu |
                   --------------------------
              
              ''')
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
        loading()
        print()
        print("-"*121)
        print(f'>\tKamu adalah seorang {JenisKelamin} dengan domisili {kode_wilayah} dan orang ke {jumlah_orang} yang lahir di tanggal {tanggal} {bulan} {tahun}\t<')
        print("-"*121)
    except:
        print()
        print("Format tidak sesuai, kembali ke Menu Utama")
        separator()




#-----6 ADMIN------------------------------------------------------------------------------------------------------------------------------------------------#

password_user = "123456"
password_admin = "987654"

def menu_admin():
    print('''
                   -----------------------
                   |      Menu Admin     |
                   -----------------------
        Menu :
          
        1.Ganti Password User
        2.Pulihkan Data yang telah dihapus
        3.Hapus Semua Data
        4.Kembali ke Menu Utama

''')


def admin_menu_login(): # admin password checker, kalau sudah benar lanjut ke menu admin
    while True:
        global password_admin
        print()
        print("-"*47)
        print("Masukan Password Admin untuk mengakses menu ini")
        print("-"*47)
        print()
        password = input("Password: ")
        if password == password_admin:
            separator()
            admin_menu_list()
            break
        else:
            print("Password salah, kembali ke Menu Utama")
            separator()
            break




def admin_menu_list():
    while True:
        try:
            menu_admin()
            menu_choosen6 = int(input("Pilih Nomor yang diinginkan: "))
            if menu_choosen6 == 1: #ganti password user
                change_password_user()
            elif menu_choosen6 == 2: #restore data from recycle bin
                if len(data_base_penduduk_deleted) == 0: #cheking if data exist in database, if not will back to admin menu
                    print("\n")
                    print("-----------------\n!Database kosong!\n-----------------")
                    separator()
                else:
                    loading()
                    print("\n\t\t\t\t\t\t-= Daftar Data Terhapus =-\n")
                    header_tabel()
                    for i in data_base_penduduk_deleted:
                                print(f'║ {i[0]}\t{i[1].capitalize()}\t\t{i[2].capitalize()}\t\t\t{i[3]}\t\t{i[4].capitalize()}\t\t{i[5].capitalize()}\t\t║')
                    print("-"*137)
                    print("Data di dalam keranjang sampah akan dihapus otomatis setelah 30 hari!")
                    print()
                    print()
                    NIK_input_restore = input("Masukan NIK yang ingin dipulihkan : ")
                    if NIK_input_restore  == "cancel" or NIK_input_restore  == "batal":
                        print()
                        print("Operasi dibatalkan, kembali ke menu...")
                        separator()
                        break
                    while True:
                        if len(NIK_input_restore) == 16 and NIK_input_restore.isnumeric: #input checker
                            break        
                        else:
                            print("Format salah, masukan 16 digit angka NIK")
                            NIK_input_restore = input("Masukkan NIK yang ingin dipulihkan: ")
                    print()
                    NIK_restore_status = False
                    temp_choosen_restore = "" #for preview purpose
                    for o in data_base_penduduk_deleted: #menentukan apakah ada di dalam list atau tidak, kalau ada lanjut
                        if o[0] == NIK_input_restore:
                            NIK_restore_status += True
                            temp_choosen_restore = o
                            index_siap_restore = data_base_penduduk_deleted.index(o) #ambil index yang bakal direstore
                            print()
                        else:
                            continue
                    if NIK_restore_status == True:
                        print("==Data ditemukan dalam keranjang sampah==")
                        print()
                        loading()
                        print()
                        print("\n\t\t\t\t\t-= Detail Data Penduduk =-\n")
                        header_tabel()
                        print(f'║ {temp_choosen_restore[0]}\t{temp_choosen_restore[1].capitalize()}\t\t{temp_choosen_restore[2].capitalize()}\t\t\t{temp_choosen_restore[3]}\t\t{temp_choosen_restore[4].capitalize()}\t\t{temp_choosen_restore[5].capitalize()}\t\t║')
                        print("-"*137)
                        print("\n")
                        jawaban_delete = input("Apakah anda yakin ingin memulihkan data? (Y/N) ")
                        if jawaban_delete.lower() == "y":
                            data_base_penduduk.append(data_base_penduduk_deleted[index_siap_restore]) #add selected data to be restored to main database
                            data_base_penduduk_deleted.pop(index_siap_restore) #delete the selected data after restored in database deleted
                            loading()
                            print()
                            print("Data Berhasil dipulihkan !")
                            print()
                        else:
                            print("Operasi dibatalkan, kembali ke menu...")
                            separator()
                            continue
            elif menu_choosen6 == 3:
                hapus_all_input = input("Apakah kamu yakin untuk menghapus semua data? (Y/N) ")
                if hapus_all_input.lower() == "y":
                    data_base_penduduk.clear()
                    print("Semua data berhasil dihapus")
                else:
                    separator()
                    continue
            elif menu_choosen6 == 4:
                print("Kembali ke Menu Utama>")
                separator()
                break
            else :
                print("\n\n")
                print("!Pilihan menu tidak ada, harap memilih sesuai menu yang tersedia!\n"+'-'*65)
                print("\n\n\n")
                separator()

        except ValueError:
                print("\n")
                print("Harap mengisi dengan angka!\n---------------------------")


def change_password_user():
    global password_user
    print()
    print("-"*20)
    print("Ganti Password User")
    print("-"*20)
    print()
    password_new = input("Masukkan Password Baru (hanya angka dan 6 digit) : ")
    while True: #checking input, if true continue to next line
            if len(password_new) == 6 and password_new.isnumeric:
                break        
            else:
                print("Format salah, masukan 6 digit angka untuk Password")
                password_new = input("Masukkan password baru : ")
    password_user = password_new
    loading()
    print("Password anda berhasil diubah...")
    separator()

def pass_login_menu():
    while True:
        global password_admin
        global password_user
        print()
        print("-"*34)
        print("DISDUKCAPIL Kabupaten Bandung v1.0")
        print("-"*34)
        print()
        password = input("Masukkan Password untuk mengakses sistem: ")
        if password == password_user or password == password_admin:
            break
        else:
            print()
            print("Password Salah, harap menghubungi team IT support... default (123456)")
            print()
            continue

def delete_menu_login():
    while True:
        global password_user
        print()
        print("-"*47)
        print("Masukan Password User untuk mengakses menu ini")
        print("-"*47)
        print()
        password = input("Password: ")
        if password == password_user:
            separator()
            menu_hapus_data_penduduk()
            break
        else:
            print("Password salah, kembali ke Menu Utama")
            separator()
            break



#-----MAIN MENU------------------------------------------------------------------------------------------------------------------------------------------------#

def menu_utama():
    print()
    print(f'''
          ===========================================================
          Selamat datang di sistem DISDUKCAPIL Kabupaten Bandung v1.0
          ===========================================================

          List Program :

          1.Lihat Data Penduduk
          2.Tambahkan Data Penduduk
          3.Ubah Data Penduduk
          4.Hapus Data Penduduk
          
          5.Cek Data dari NIK Kamu
          6.Menu Admin
          7.Tutup Program
          

          
          --------= Sehat Selalu untuk Kita Semua =--------
                        {time.ctime()}
          ''')

menu_choosen = 0
def main_program():
    pass_login_menu()
    print('\n')
    loading()
    separator()
    while True:
        menu_utama()
        try:
            menu_choosen   = int(input("Pilih Menu yang ingin dijalankan : "))
            if menu_choosen   == 1:
                separator()
                menu_lihat_data_penduduk()
            elif menu_choosen   == 2:
                separator()
                menu_tambahkan_data_penduduk()
            elif menu_choosen   == 3:
                separator()
                menu_update_data_penduduk()
            elif menu_choosen   == 4:
                separator()
                delete_menu_login()
            elif menu_choosen   == 5:
                separator()
                NIK_reader()
            elif menu_choosen == 6:
                separator()
                admin_menu_login()
            elif menu_choosen == 7:
                separator()
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





#-----MAIN PROGRAM------------------------------------------------------------------------------------------------------------------------------------------------#

main_program()
