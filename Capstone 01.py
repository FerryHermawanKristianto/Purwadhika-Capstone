# kali ini saya membuat sebuah program yang akan membatu guru dalam mendata siswanya. ada empat fitur utama di dalam program
# ini yaitu membaca atau mencari data, menghapus data, mengedit data, dan menambahkan data. untuk fitur membaca atau mencari data,
# saya buat aga seorang guru bisa menampilkan tabel yang sudah dibuat dan melihat data siswa mulai dari nama, nilai, dan id siswa.
# Selain itu guru juga bisa mencari data siswa berdasarkan id siswa. pada program ini saya buat bisa ada 2 nama anak yang sama tetapi idnya berbeda.
# Jadi data yang unik atau setiap murid berbeda yaitu id dari anak itu sendiri. Untuk fitur menghapus data sesuai namanya program ini bisa untuk menghapus 3 data sekaligus
# yaitu id nama dan nilai sesuai dengan cara memasukkan id siswa yang ketiga datanya ingin dihapus
# untuk fitur edit data, saya membuat agar guru masih bisa mengedit nama, nilai, maupun id apabila terjadi kesalahan dalam menginpu data maupun typo, tetapi  saat mengidit data,
# saya buat agar jika mengidt id siswa maka idnya tidak bisa memakai id siswa yang sudah ada
# untuk fitur terakhir yaitu menambahkan data, sesuai namanya saya buat agar guru bisa menambahkan data murid beserta id dan nilainya.


from prettytable import PrettyTable
# jadi disini saya memakai library prettytable untuk membuat tabel
import operator
# saya juga memakai module berupa operator untuk mensortir dictionary didalam list

# pertama tama saya membuat list yang terdiri dari dictionary yang berisi data siswa
data_nilai_siswa = [
    {"nama": "Bunda", "nilai": 100, "id": 317005},
    {"nama": "Budi", "nilai": 0, "id": 317002},
    {"nama": "Cinta", "nilai": 80, "id": 317003},
    {"nama": "Dodi", "nilai": 50, "id": 317004}
]
# saya juga membuat list untuk menampun data yang dihapus sebagai bahan untuk backup data
backup_data = []

# disini saya membuat function user input yang bakal membutuhkan argument text
# jadi saya bikin fungsi ini karena saya membutuhkan fungsi yang hanya bisa mendapatkan input berupa integer dana agar efektif, karena bakal banyak dipake fungsi ini


def user_input(text):
    while (True):
        try:
            choice = int(input(text))
            break
        except ValueError:
            print("Please input integer only...")
    return choice

# Kalau yang ini saya membuatnya untuk mendapatkan konfirmasi karena dibutuhkan pada saat delete, tambah maupun update data sehingga user bisa hati hati tidak mendelete atau menambah maupun update data sembarangan


def confirmation():
    while (True):
        confirmation = user_input(
            "Continue?\n1.Yes\n2.No\nKetikkan pilihan anda: ")
        if confirmation == 1:
            return True
        elif confirmation == 2:
            return False
        else:
            print("The option you entered is not valid")

# Disini saya juga membuat function untuk mencari tau apakah ada id pada argument sudah ada di dalam data pada data_nilai_siswa.
# Kalau sudah ada id yang sama maka dikasih tau di index ke berapa pada data_nilai_siswa yang memiliki id pada argument


def search_id(id):
    for i in range(len(data_nilai_siswa)):
        if id == data_nilai_siswa[i]["id"]:
            return i
    return -1


# untuk function ini, berfungsi untuk menampilkan seluruh data pada list data_nilai_siswa dalam bentuk tabel


def tampilkan_tabel():
    myTable = PrettyTable()
    for i in range(len(data_nilai_siswa)):
        myTable.field_names = ["Nama", "Nilai", "Id"]
        myTable.add_row([data_nilai_siswa[i]["nama"],
                        data_nilai_siswa[i]["nilai"], data_nilai_siswa[i]["id"]])
    print(myTable)

# Sedangkan untuk function ini, berfungsi untuk menampilkan data hanya satu index pada list data_nilai_siswa dalam bentuk tabel yang terdiri dari nama nilai dan id dari satu siwa saja


def tampilkan_data(i):
    myTable = PrettyTable()
    myTable.field_names = ["Nama", "Nilai", "Id"]
    myTable.add_row([data_nilai_siswa[i]["nama"],
                     data_nilai_siswa[i]["nilai"], data_nilai_siswa[i]["id"]])
    print(myTable)


while (True):
    # diawali dengan meminta user untuk memilih dari ke 5 opsi
    pilihan_utama = user_input(
        "1.Search Data\n2.Add Data\n3.Update Data\n4.Hapus data\n5.Recover data\n6.Exit\nKetikkan pilihan anda: ")
    # kalau yang dipilih opsi pertama
    if pilihan_utama == 1:
        while (True):
            # maka ditanyakan lagi 3 opsi
            subpilihan = user_input(
                "1.Tampilkan seluruh data\n2.Mencari Nilai Siswa\n3.Exit\nKetikkan pilihan anda: ")
            # kalau yang dipilih opsi pertama maka akan ngecek terlebih dahulu ada tidak data dalam data_nilai_siswa
            if subpilihan == 1:
                if len(data_nilai_siswa) == 0:
                    # kalau ga ada dikasih tau tidak ada
                    print("Data Does not exist")
                else:
                    while (True):
                        subpilihan = user_input(
                            "1.Urut dari nilai terbesar\n2.Urut sesuai abjad nama\n3.Urut dari id terkecil\nKetikkan pilihan anda:")
                        if subpilihan == 1:
                            # disini saya membuat terurut data dengan dari paling besar ke paling kecil nilainya berdasarkan nilai
                            data_nilai_siswa.sort(
                                key=operator.itemgetter("nilai"), reverse=True)
                            break
                        elif subpilihan == 2:
                            # disini saya membuat terurut data sesuai abjad dari a-z
                            data_nilai_siswa.sort(
                                key=operator.itemgetter("nama"))
                            break
                        elif subpilihan == 3:
                            # dan disini saya membuat terurut berdasarkan id terkecil ke terbesar
                            data_nilai_siswa.sort(
                                key=operator.itemgetter("id"))
                            break
                        else:
                            print("Inpur Invalid")
                    # kalau ada maka ditampilkan tabel dengan data seluruh siswa
                    tampilkan_tabel()
            elif subpilihan == 2:
                # kalau yang dipilih opsi kedua, maka akan ditanyakan id siswa yang dicari datanya
                id = user_input("Id: ")
                # dan di cek ada tidak data itu di dalam list data_nilai_siswa
                exist = search_id(id)
                if exist == -1:
                    # kalau tidak ada datanya maka dikasih tau
                    print("Data does not exist")
                else:
                    # kalau ada datanya maka ditampilin tabel dengan data cuman satu siswa sesuai id yang sudah diinput tadi
                    tampilkan_data(exist)
            elif subpilihan == 3:
                # kalau dipilih opsi ketika maka dia keluar dari loop dan balik ke menu utama
                break
            else:
                # kalau dinput angka selain 1 2 dan 3 maka yang diinput tidak valid dan balik ke subpilihan yang diatas
                print("The option you entered is not valid")
    # jika yang dipilih pilihan kedua
    elif pilihan_utama == 2:
        while (True):
            # maka ditanyakan 2 opsi
            subpilihan = user_input(
                "1.Tambahkan data siswa\n2.Exit\nKetikkan pilihan anda: ")
            # kalau opsi pertama yang dipilih
            if subpilihan == 1:
                # maka akan ditanyakan id siswa dan dilihat ada tidak id tersebut dalam list
                id = user_input("Id: ")
                if search_id(id) != -1:
                    # kalau ada maka tidak usah ditambahin lagi datanya palingpun tinggal edit datanya
                    print("Data already exists")
                else:
                    # kalau belum ada, maka ditanyakan nama dan nilai siswa yang akan dimasukkan datanya
                    nama = input("Nama: ")
                    nilai = user_input("Nilai: ")
                    # disini akan ditanyakan ulang apakah mau lanjut ditambahkan atau tidak
                    if confirmation():
                        # jika user setuju maka ditambahkan data itu  ke dalam list data_nilai_siswa
                        data_nilai_siswa.append(
                            {"nama": nama, "nilai": nilai, "id": id})
                        print("Data successfully saved")
            elif subpilihan == 2:
                # yang ini sama seperti yang diatas kalau pilih opsi kedua akan ke main menu
                break
            else:
                # dan kalau tidak valid data yang diinput maka dikasih tau
                print("The option you entered is not valid")
    elif pilihan_utama == 3:
        while (True):
            # disini user disuruh pilih antara 3 pilihan lagi
            subpilihan = user_input(
                "1.Perbaharui nilai atau nama atau id siswa\n2.Exit\nKetikkan pilihan anda: ")
            if subpilihan == 1:
                # kalau dipilih opsi yang pertama maka, dicek dulu ada tidak id siswa pada data
                id = user_input("Id: ")
                exist = search_id(id)
                if exist == -1:
                    print("The data you are looking for does not exist")
                else:
                    # kalau ada maka ditampilkan lagi data siswa tersebut
                    tampilkan_data(exist)
                    # jika user setuju untuk lanjut maka
                    if confirmation():
                        while (True):
                            # terdapat 3 pilihan lagi
                            pilih = user_input(
                                "1.Ubah Nama\n2.Ubah Nilai\n3.Ubah Id\nKetikkan pilihan anda:  ")
                            if pilih == 1:
                                # pilihan pertama untuk cuman ubah nama siswa
                                nama_baru = input("Nama Siswa: ")
                                if confirmation():
                                    data_nilai_siswa[exist]["nama"] = nama_baru
                                    print("Data successfully updated")
                                break
                            elif pilih == 2:
                                # pilihan kedua untuk uba nilai siswa
                                nilai_baru = user_input("Nilai: ")
                                if confirmation():
                                    data_nilai_siswa[exist]["nilai"] = nilai_baru
                                    print("Data successfully updated")
                                break
                            elif pilih == 3:
                                # dan pilihan terakhir untuk ubah id siswa
                                while (True):
                                    id_baru = user_input("Id: ")
                                    exist2 = search_id(id_baru)
                                    print(id_baru)
                                    # tetapi ketika id siswa yang baru uda ada pada data sehingga terjadi kesamaan id maka akan ditolah dan ditanyakan id yang baru lagi
                                    if exist2 != -1:
                                        print("Id already exist")
                                    else:
                                        id = id_baru
                                        break
                                if confirmation():
                                    data_nilai_siswa[exist]["id"] = id
                                    print("Data successfully updated")
                                break
                            else:
                                print("Input tidak valid")
            elif subpilihan == 2:
                break
            else:
                print("The option you entered is not valid")
    elif pilihan_utama == 4:
        # untuk pilihan yang keempat
        while (True):
            # disuruh pilih opsi atara 2 data
            subpilihan = user_input(
                "1.Hapus data\n2.Exit\nKetikkan pilihan anda: ")
            if subpilihan == 1:
                # untuk pilihan pertama seperti biasa ditanyakan dahulu id siswa yang mau dihapus
                id = user_input("Id: ")
                exist = search_id(id)
                if exist == -1:
                    # kalau tidak ada id pada data maka akan dikasih tau
                    print("The data you are looking for does not exist")
                else:
                    # dan kalau ada maka ditampilkan data siswa tersebut dan ditanyakan apakah mau lanjut
                    tampilkan_data(exist)
                    if confirmation():
                        # setelah user memutuskan untuk continue maka data yang mau dihapus dipindahkan atau di cut ke backup_data agar nantinya bisa di restore
                        backup_data.append(
                            {"nama": data_nilai_siswa[exist]["nama"], "nilai": data_nilai_siswa[exist]["nilai"], "id": data_nilai_siswa[exist]["id"]})
                        # kalau iya maka akan dihapus
                        data_nilai_siswa.pop(exist)
                        print("Data successfully deleted")
            elif subpilihan == 2:
                break
            else:
                print("The option you entered is not valid")
    elif pilihan_utama == 5:
        # untuk pilihan ke lima akan ditanyakan apakah mau lanjut recover data
        if confirmation():
            # kalo iya maka semua ddata yang sudah tersimpan sementara di backup_data akan dibalikkan lagi ke backup_data
            for i in range(len(backup_data)):
                data_nilai_siswa.append(
                    {"nama": backup_data[i]["nama"], "nilai": backup_data[i]["nilai"], "id": backup_data[i]["id"]})
            # lalu data sementara di backup_data akan dihapus
            backup_data.clear()
            print("Data successfully recover")
    elif pilihan_utama == 6:
        data_nilai_siswa.sort()
        tampilkan_tabel()
    elif pilihan_utama == 7:
        # untuk pilihan terakhir memungkinkan kita untuk menghentikan program
        break
    else:
        # kalau opsi yang dipilih selain angka 1 2 3 4 dan 5 maka otomatis dikasih tau invalid input dan disuruh memilih opsi kembali
        print("The option you entered is not valid")