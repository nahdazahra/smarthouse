# Smarthouse over Telegram

![](/assets/smarthouse.png)

Smarthouse \(rumah pintar\) adalah miniatur dari sebuah rumah yang menerapkan IoT \(Internet of Things\). Rumah ini memanfaatkan bot dari aplikasi Telegram untuk mengendalikan alat yang terpasang di dalamnya. Contoh yang digunakan dalam rumah ini adalah mengendalikan lampu dan pintu garasi. Demi keamanan rumah, pengguna yang memiliki akses untuk mengendalikan smarthouse ini.

---

## How to Build

### Requirements

* Telegram bot \(click here how to get Telegram bot\)
* Servo
* Raspberry pi 2
* LED lamp
* Breadboard
* Jumper wires
* Miniature house

### Installations

#### _Telegram Bot_

1. Setelah install aplikasi Telegram di perangkat \(Smartphone/PC/Laptop/WebApp\) Anda, bisa langsung login ke akun Telegram Anda atau jika belum memiliki akun Telegram bisa juga mendaftarkan akun baru.
2. Cari "@BotFather" tanpa tanda petik pada _search bar_ aplikasi Telegram.
   **Keterangan:** @BotFather adalah bot resmi dari telegram yang tugasnya melahirkan/menciptakan bot baru.
   ![Screenshot 1](/images/1buat.PNG)
3. Klik start atau ketik /start untuk memulai pembuatan bot.
   ![Screenshot 2](/images/2buat.PNG)
4. Ketik /newbot untuk membuat bot baru.
   ![Screenshot 3](/images/3buat.PNG)
5. Masukkan nama bot yang Anda inginkan.
   ![Screenshot 4](/images/4buat.PNG)
6. Masukkan username bot yang Anda inginkan. Username tersebut harus berakiran 'bot' tanpa spasi.
7. Simpan `<token key>` dari bot Anda yang diberikan oleh @BotFather.
   ![Screenshot 5](/images/5buat.PNG)
8. Cari bot Anda pada _search bar_ dan buka bot tersebut.
9. Klik start dan bot baru Anda telah jadi.

### II. Cara menambahkan _command suggestion_ pada bot Telegram

1. Cari kembali akun @BotFather pada _search bar_ aplikasi Telegram.
2. Lalu ketikkan /setcommands untuk menngatur perintah pada bot.
   ![Screenshot 6](/images/7command.PNG)
3. Pilih bot yang akan diatur perintahnya.
   ![Screenshot 7](/images/6command.PNG)
4. Masukkan perintah-perintah apa saja yang ingin ditambahkan beserta deskripsi perintahnya sesuai format pada gambar dibawah ini.
   **NB :** _command_ tidak boleh terdiri dari huruf kapital dan spasi.
   ![Screenshot 8](/images/8command.PNG)
5. Ketika berhasil maka akan muncul balasan seperti gambar dibawah ini.
   ![Screenshot 9](/images/9command.PNG)
6. _Restart_ aplikasi Telegram Anda lalu buka bot Telegram yang telah Anda atur perintahnya

#### _IoT Configuration_

1. Install [Raspbian](https://www.raspberrypi.org/documentation/installation/installing-images/) pada sd card untuk Raspberry pi.
2. Masukkan token untuk bot yang akan digunakan ke script API telegram \(/examples/echobot2.py\).
3. ```
   ...
   def main():
       # Create the EventHandler and pass it your bot's token.
       updater = Updater("458534210:AAHOeYPZamMU9bqH-MV36tOBnKj4FhWuvoo")
       ...
   ```

   Buat script menggunakan python untuk mengendalikan servo \(e.g. servobuka.py dan servotutup.py, dengan perubahan sudut yang digunakan untuk pintu garasi 90°\).

4. Buat script menggunakan python untuk menghidupkan atau mematikan lampu led \(e.g. lampu1nyala.py dan lampu1mati.py\).

5. Masukkan command yang diinginkan sesuai dengan kebutuhan ke script echobot2.py.

6. ```
       ...
       # Get the dispatcher to register handlers
       dp = updater.dispatcher
       #one = os.system('python ./servo.py')
       # on different commands - answer in Telegram
       #updater.message.reply_text('Selamat Datang di SmartHouseAJK\n\n/help\n   --> Melihat Panduan Penggunaan')
       dp.add_handler(CommandHandler("start", start))
       dp.add_handler(CommandHandler("help", help))
       dp.add_handler(CommandHandler("bukagarasi", buka))
       dp.add_handler(CommandHandler("tutupgarasi", tutup))
       dp.add_handler(CommandHandler("status", status))
       dp.add_handler(CommandHandler("matikanlampu1", mati1)) #matikanlampugarasi
       dp.add_handler(CommandHandler("nyalakanlampu1", nyala1)) #nyalakanlampugarasi
       dp.add_handler(CommandHandler("matikanlampu2", mati2)) #matikanlampurumah
       dp.add_handler(CommandHandler("nyalakanlampu2", nyala2)) #nyalakanrampurumah
       dp.add_handler(CommandHandler("matikanlampu3", mati3)) #matikanlampudepan
       dp.add_handler(CommandHandler("nyalakanlampu3", nyala3)) #nyalakanlampudepan
       dp.add_handler(CommandHandler("tambahadmin", admin))
       ...
   ```

   Buat fungsi untuk masing-masing command yang ada pada bot tersebut, contohnya kode berikut yangg merupakan fungsi untuk menutup pintu garasi.

7. ```
   ...
   def tutup(bot, update):
        file = open("admin.txt","r")
        file2 = file.read()
        if update.message.chat.username in file2:
           f = open('garasi.log', 'r')
           g = f.read().split(" ")
           if "tutup\n" in g:
              update.message.reply_text("Garasi sudah tutup")
           else :
              os.system('python ./servotutup.py')
              update.message.reply_text("Menutup garasi")
        else :
           update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')
           ...
   ```

   Untuk mengetahui status dari alat tersebut, maka dilakukan pencatatan menggunakan log

8. ```
   import logging
   import os
   ...
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       level=logging.INFO)

   logger = logging.getLogger(__name__)
   ...
   ```

   Untuk menjaga keamanan, gunakan fitur admin dengan menambahkan list _username_ dari admin ke file "admin.txt", lalu buat fungsi admin di script echobot2.py \(sesuaikan fungsi yang dijalankan dengan kebutuhan\).

9. ```
   def admin(bot,update):
       file = open('admin.txt','r')
       file2 = file.read()
       if update.message.chat.username in file2:
       	 filew = open("admin.txt","a")
       	 temp = update.message.text
       	 temp2 = temp.split(" ")
       	 newadmin = temp2[1]
       	 filew.write(newadmin+"\n")
       	 update.message.reply_text("username "+newadmin+" telah ditambahkan")
       else :
            update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')
       file.close()
       ...
   ```

   Selanjutnya untuk setiap fungsi _command_, dapat ditambahkan pengecekan untuk user yang berhak menggunakan bot tersebut, misalnya

10. ```
    def mati1(bot, update):
        file = open("admin.txt","r")
        file2 = file.read()
        if update.message.chat.username in file2:
            f = open('lampu1.log', 'r')
            g = f.read().split(" ")
            if "mati\n" in g:
            ...
    ```

    Tambahkan _command_ lain sesuai dengan kebutuhan.



#### _Build Up IoT_

1. Sesuaikan _jumper wire _yang dibutuhkan untuk menyambungkan Raspberry pi dengan servo \(_female-female_\) maupun dengan breadboard \(_male-female_\).
2. Sesuaikan tipe pin pada Raspberry pi dan servo maupun _breadboard _yang akan disambung dengan menggunakan _jumper wires._![](/assets/import.png)
3. Ketika semua _jumper wires _telah terhubung antara Raspberry dengan servo atau breadboard, maka kita dapat menguji script yang menjalankan servo \(buka-tutup pintu garasi\) dan lampu \(mati-hidup\). Jika alat sudah berjalan sesuai dengan keinginan, maka dapat kita coba langsung menggunakan bot telegram.
4. Pastikan Raspberry pi terhubung dengan koneksi internet.

**NB : Breadboard digunakan karena aliran listrik dari raspberry tidak kuat untuk menyalakan lampu led, sedangkan jika lampu dinyalakan menggunakan daya baterai, aliran listrik yang dialirkan terlalu besar, kapasitasnya berlebihan.**

