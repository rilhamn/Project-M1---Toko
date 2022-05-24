#===================================== MAIN MENU FUNCTION ==========================================#
#Function Menu Utama
def main_menu():
    print(""" 
Selamat Datang di Toko 

List Menu Utama:
1. Menampilkan Daftar Item
2. Menambah Item
3. Update Item
4. Hapus Item
5. Item Terjual dan Gross Revenue
6. Exit Program
    """)
    angka_menu_utama=input("Masukan angka menu yang ingin dijalankan = ")

    #Menampilkan Daftar Buah
    if angka_menu_utama==str(1):
        show_menu()

    #Menambahkan Item
    elif angka_menu_utama==str(2):
        create_menu()

    #Update Item
    elif angka_menu_utama==str(3):
        update_menu()

    #Hapus Item
    elif angka_menu_utama==str(4):
        delete_menu()

    #Jual Item
    elif angka_menu_utama==str(5):
        sell_menu()

    #Exit Program
    elif angka_menu_utama==str(6):
        print("\nTerima Kasih")
        quit()

    #Other Input
    else:
        print("Silahkan Ketik 1/2/3/4/5")
        main_menu()

#======================================== FUNCTION SHOW ===========================================#
#Function Menu Menampilakan item
def show_menu():
    print(""" 
List Menu Menampilkan Item:
1. Menampilkan Seluruh Daftar Item
2. Menampilkan Daftar Item yang Diinginkan
3. Kembali ke Menu Utama
    """)
    angka_menu_menampilakan=input("Masukan angka menu yang ingin dijalankan = ")
    if angka_menu_menampilakan==str(1):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            print("Maaf, tidak ada item yang dapat ditampilkan karena daftar item kosong")
        else:
            show_all()
        show_menu()
    elif angka_menu_menampilakan==str(2):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            print("Maaf, tidak ada item yang dapat ditampilkan karena daftar item kosong")
        else:
            show_specific_menu()
        show_menu()
    elif angka_menu_menampilakan==str(3):
        main_menu()
    else:
        print("Silahkan Ketik 1/2/3")
        show_menu()

#Function Menampilkan seluruh Item
def show_all():
    print(f"""
Daftar Item:
Tipe\tID\tNama\tStock\tHarga""")
    for k, v in (dict_toko.items()):
        if v!={}:
            print(k.capitalize(), end="\t")       
            x=0         
            for k1, v1 in sorted(v.items()):
                if x!=0:
                    print(" ", end="\t")
                print(k1.upper(), end="\t")            
                for v2 in v1.values():
                    print(str(v2).capitalize(), end="\t")
                x+=1
                print(" ")

#Function Menu Menampilakan Sebagian Item
def show_specific_menu():
    print(""" 
List Menu Menampilkan Sebagian Item:
1. Menampilkan Daftar Item Berdasarkan Tipe
2. Menampilkan Item Berdasarkan ID
3. Kembali ke Menu Menampilkan Item
    """)
    angka_menu_menampilakan_sebagian=input("Masukan angka menu yang ingin dijalankan = ")
    if angka_menu_menampilakan_sebagian==str(1):
        tipe_item_menampilkan = input("Tipe item apa yang ingin ditampilakan = ").lower()
        show_specific1(tipe_item_menampilkan)
        show_specific_menu()
    elif angka_menu_menampilakan_sebagian==str(2):
        id_item_menampilkan=input("ID Item yang ingin ditampilkan = ").lower()
        tipe_item_menampilkan=convert_id_tipe(id_item_menampilkan)
        show_specific2(tipe_item_menampilkan, id_item_menampilkan)
        show_specific_menu()       
    elif angka_menu_menampilakan_sebagian==str(3):
        show_menu()
    else:
        print("Silahkan ketik 1/2/3")
        show_specific_menu()

#Function Menampilakan Sebagian Item berdasarkan Tipe
def show_specific1(tipe_item_menampikan1):
    if tipe_item_menampikan1 in dict_toko.keys() and dict_toko[tipe_item_menampikan1]!={}:
        print(f"""
Daftar Item:
Tipe\tID\tNama\tStock\tHarga""")
        x=0
        print(tipe_item_menampikan1.capitalize(), end="\t")            
        for k, v in sorted(dict_toko[tipe_item_menampikan1].items()): 
            if x==0:
                print(k.upper(), end="\t")
            else:
                print("\t"+k.upper(), end="\t")                                       
            for k1, v1 in v.items():
                print(str(v1).capitalize(), end="\t")
            print(" ")
            x+=1    
    else:
        print("Maaf, tipe item tidak dapat ditemukan")

#Function Menampilakan Sebagian Item berdasarkan ID
def show_specific2(tipe_item_menampikan2, id_item_menampilakan2):
    if tipe_item_menampikan2!="nodata":
        print(f"""
Daftar Item:
ID\tNama\tStock\tHarga""")
        print(id_item_menampilakan2.upper(), end="\t")               
        for v in dict_toko[tipe_item_menampikan2][id_item_menampilakan2].values(): 
                print(str(v).capitalize(), end="\t")
        print(" ")               
    else:
        print("Maaf, item tidak dapat ditemukan")

#Function Menampilkan daftar item terjual
def show_cart(dict_cart1):
    print(f"""
Daftar Item yang Terjual:
Tipe\tID\tNama\tQty\tHarga\tTotal""")
    for k, v in dict_cart1.items():
        if v!={}:
            print(k.capitalize(), end="\t")       
            x=0         
            for k1, v1 in sorted(v.items()):
                if x==0:
                    print(k1.upper(), end="\t")   
                else:
                    print(" ", end="\t")
                    print(k1.upper(), end="\t")            
                for k2, v2 in v1.items():
                    print(str(v2).capitalize(), end="\t")
                x+=1
                print(" ")

#======================================== FUNCTION TAMBAH ==========================================#
#Function Menu Menambahkan Item
def create_menu():
    print(""" 
List Menu Menambah Item:
1. Menambah Item Baru pada Daftar Item
2. Kembali ke Menu Utama
    """)
    angka_menu_menambah=input("Masukan angka menu yang ingin dijalankan = ")
    if angka_menu_menambah==str(1):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            pass
        else:
            show_all()
        create()
        create_menu()
    elif angka_menu_menambah==str(2):
        main_menu()
    else:
        print("Silahkan Ketik 1/2")
        create_menu()

#Function Menambahkan Item
def create():
    dict_add={} #dictionary Kosong
    tipe_item_menambah=input("\nTipe item yang ingin ditambah = ").lower()
    if tipe_item_menambah in dict_toko.keys():
        id_item_menambah=input("ID item yang ingin ditambah = ").lower()
        konfirmasi_item=convert_id_tipe(id_item_menambah)
        if konfirmasi_item!="nodata":
            print("Item dengan ID yang sama sudah ada")
        else:
            nama_item_baru=input("Nama Item = ")
            while True:
                stock_item_baru=input("Stock Item = ")
                if stock_item_baru.isnumeric():
                    stock_item_baru=int(stock_item_baru)
                    break
                else:
                    print("Mohon masukan data numerical")
            while True:
                harga_item_baru=input("Harga Item = ")
                if harga_item_baru.isnumeric():
                    harga_item_baru=int(harga_item_baru)
                    break
                else:
                    print("Mohon masukan data numerical")
            dict_add[id_item_menambah]={"nama":nama_item_baru,"stock":stock_item_baru, "harga":harga_item_baru}
            while True:
                continue_process("menambah")
                angka_menambah=input("Masukan angka menu yang ingin dijalankan = ").lower()
                if angka_menambah=="1":
                    dict_toko[tipe_item_menambah].update(dict_add)
                    print("Data Tersimpan")
                    break
                elif angka_menambah=="2":
                    break
                else:
                    print("Silahkan Ketik 1/2")
    else:
        print("Maaf, tipe item tidak tersedia")

#======================================== FUNCTION UPDATE ==========================================#
#Function Menu Update Data
def update_menu():
    print(""" 
List Menu Update Item:
1. Update Data Item 
2. Kembali ke Menu Utama
    """)
    angka_menu_update=input("Masukan angka menu yang ingin dijalankan = ").lower()
    if angka_menu_update==str(1):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            print("Maaf, tidak dapat melakukan proses ini karena daftar item kosong")
        else:
            show_all()
            update()
        update_menu()
    elif angka_menu_update==str(2):
        main_menu()
    else:
        print("Silahkan Ketik 1/2")
        update_menu()

#Function Update Data
def update():
    id_item_update=input("\nID Item yang ingin diupdate = ").lower()
    tipe_item_update=convert_id_tipe(id_item_update)
    if tipe_item_update!="nodata":
        show_specific2(tipe_item_update, id_item_update)
        while True:
            continue_process("update")
            angka_update1=input("Masukan angka menu yang ingin dijalankan = ")
            if angka_update1=="1":
                while True:
                    data_key_update=input("Masukan data apa yang ingin diupdate = ").lower()
                    if data_key_update in dict_toko[tipe_item_update][id_item_update]:
                        if data_key_update=="nama":
                            data_value_update=input("Masukan value data yang ingin diupdate = ")
                        else:
                            while True:
                                data_value_update=input("Masukan value data yang ingin diupdate = ")
                                if data_value_update.isnumeric():
                                    data_value_update=int(data_value_update)
                                    break
                                else:
                                    print("Mohon masukan data numerical")
                        while True:
                            continue_process("update")
                            angka_update2=input("Masukan angka menu yang ingin dijalankan = ")
                            if angka_update2=="1": 
                                dict_toko[tipe_item_update][id_item_update][data_key_update]=data_value_update
                                print("Data Terupdate")
                                break
                            elif angka_update2=="2":
                                break
                            else:
                                print("Silahkan Ketik 1/2")
                        break        
                    else:
                        print("silahakan ketik nama/stock/harga")
                break
            elif angka_update1=="2":
                break
            else:
                print("Silahkan Ketik 1/2")
    else:
        print("Maaf, item tidak dapat ditemukan")

#======================================== FUNCTION HAPUS ===========================================#
#Function Menu Menghapus Item
def delete_menu():
    print(""" 
List Menu Menghapus Item:
1. Menghapus Item pada Daftar Item
2. Kembali ke Menu Utama
    """)
    angka_menu_menghapus=input("Masukan angka menu yang ingin dijalankan = ")
    if angka_menu_menghapus==str(1):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            print("Maaf, tidak dapat melakukan proses ini karena daftar item kosong")
        else:
            show_all()
            delete()
        delete_menu()
    elif angka_menu_menghapus==str(2):
        main_menu()
    else:
        print("Silahkan Ketik 1/2")
        delete_menu()

#Function Menghapus Item
def delete():
    id_item_menghapus=input("\nID item yang ingin dihapus = ").lower()
    tipe_item_menghapus=convert_id_tipe(id_item_menghapus)
    if tipe_item_menghapus!="nodata":
        show_specific2(tipe_item_menghapus, id_item_menghapus)
        while True:
            continue_process("menghapus")
            angka_menghapus=input("Masukan angka menu yang ingin dijalankan = ").lower()
            if angka_menghapus=="1":
                dict_toko[tipe_item_menghapus].pop(id_item_menghapus)
                print("Data Dihapus")
                break
            elif angka_menghapus=="2":
                break
            else:
                print("Silahkan Ketik 1/2")
    else:
        print("Maaf, item tidak dapat ditemukan")

#========================================= FUNCTION SELL ===========================================#
#Function Menu Item Terjual
def sell_menu():
    print(""" 
List Menu Item Terjual:
1. Item Terjual pada Daftar Item
2. Tampilkan Total Keuntungan Kotor 
3. Kembali ke Menu Utama
    """)
    angka_menu_terjual = input("Masukan angka menu yang ingin dijalankan = ")
    if angka_menu_terjual==str(1):
        if dict_toko["makanan"]=={} and dict_toko["minuman"]=={} and dict_toko["beauty"]=={}: 
            print("Maaf, tidak dapat melakukan proses ini karena daftar item kosong")
        else:
            show_all()
            sell()
        sell_menu()
    elif angka_menu_terjual==str(2):
        print(f"Total keuntungan kotor toko selama ini = {gross_revenue}")
        sell_menu()
    elif angka_menu_terjual==str(3):
        main_menu()
    else:
        print("Silahkan Ketik 1/2")
        sell_menu()

#Function Item Terjual
def sell():
    dict_cart={"makanan":{}, "minuman":{}, "beauty":{}}
    while True:
        dict_cart_add={}
        id_item_terjual=input("\nMasukan ID item yang terjual = ").lower()
        tipe_item_terjual=convert_id_tipe(id_item_terjual)
        if tipe_item_terjual!="nodata":
            jumlah_item_terjual=int(input("Masukan jumlah item yang terjual = "))
            convert_id_tipe(id_item_terjual)
            if int(dict_toko[tipe_item_terjual][id_item_terjual]["stock"])<jumlah_item_terjual:
                print("Jumlah yang dimasukkan terlalu banyak")
                print(f"""Stock {dict_toko[tipe_item_terjual][id_item_terjual]["nama"]} tinggal={dict_toko[tipe_item_terjual][id_item_terjual]["stock"]}""")
            else:
                dict_cart_add[id_item_terjual]={"nama":dict_toko[tipe_item_terjual][id_item_terjual]["nama"],
                                                "qty":jumlah_item_terjual, 
                                                "harga":dict_toko[tipe_item_terjual][id_item_terjual]["harga"],
                                                "total":jumlah_item_terjual*dict_toko[tipe_item_terjual][id_item_terjual]["harga"]}
                dict_cart[tipe_item_terjual].update(dict_cart_add)
                show_cart(dict_cart)
                print(""" 
List Menu Pencatatan Item Terjual:
1. Menambah Item yang Terjual 
2. Memfinalisasi Total Item yang Terjual 
3. Membatalkan Finalisasi Item Terjual dan Kembali ke List Menu Item Terjual
            """)
                while True:
                    angka_terjual2=input("Masukan angka menu yang ingin dijalankan = ")
                    if angka_terjual2==str(1):
                        break
                    elif angka_terjual2==str(2):
                        total=0
                        for k, v in dict_cart.items():
                            for k1, v1 in v.items():
                                dict_toko[k][k1]["stock"]-=v1["qty"]
                                total += v1["qty"]*v1["harga"]
                        print(f"Total keuntungan kotor di penjualan ini = {total}")
                        global gross_revenue
                        gross_revenue=gross_revenue+total
                        sell_menu()
                    elif angka_terjual2==str(3):
                        sell_menu()
                    else:
                        print("Silahkan Ketik 1/2")
        else:
            print("Maaf, item tidak dapat ditemukan")

#======================================== FUNCTION EXTRA ===========================================#
#Function Untuk Mengetahui Tipe item dari ID Item dan Mengecek apakah ID Item ada atau tidak
def convert_id_tipe(id_item): 
    tipe_item="nodata"
    for k, v in dict_toko.items():
        for k1 in v.keys():
            if k1==id_item:
                tipe_item=k
    return tipe_item

#Function Apabila Ingin Melanjutkan Proses
def continue_process(tipe_proses):
    print(f""" 
Apakah anda yakin untuk {tipe_proses} item:
1. Ya
2. Tidak
    """)

#================================ INTIAL CONDITION AND PROCESS =====================================#
#Project Description :
#Program yang dibuat untuk pendataan item di sebuah toko yang menjual tiga tipe item (makanan, minuman, beauty)
#Di setiap tipe item ini akan ada beberapa barang yang memiliki unique id
#unique id akan menjadi key untuk beberapa value item tersebut (nama, stock dan harga)

#Constraint:
#Tipe item dianggap bersifat tidak bisa dimodifikasi(tambah, hapus, update)
#ID item dianggap bersifat tidak bisa diupdate tapi daftar item bisa dilakukan penambahan dan pengurangan ID item
#segala input dalam program, tidak case sensitif bahkan ID item
#ID item bisa kombinasi apapun dan hanya bersifat unique pada kombinasinya 

#Initial Dicitonary
dict_toko = {"makanan":{"rt1":{"nama":"roti","stock":6,"harga":15000}, }, 
            "minuman":{"su3":{"nama":"susu","stock":8,"harga":16500}, "js1":{"nama":"jus","stock":10,"harga":22000}, }, 
            "beauty":{"sh1":{"nama":"shampo","stock":5,"harga":50000}, }} 

#dict_toko1 = {"makanan":{}, "minuman":{}, "beauty":{}} #Dummy dictionary

#Revenue
gross_revenue=0

#Market Process
main_menu()
