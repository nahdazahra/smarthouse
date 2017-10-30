# Smarthouse using Telegram

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
   **NB :** _command_ harus huruf kecil semua & tidak ada spasi.
   ![Screenshot 8](/images/8command.PNG)
5. Ketika berhasil maka akan muncul balasan seperti gambar dibawah ini.
   ![Screenshot 9](/images/9command.PNG)
6. _Restart_ aplikasi Telegram Anda lalu buka bot Telegram yang telah Anda atur perintahnya

#### _IoT Configuration_

1. Install [Raspbian](https://www.raspberrypi.org/documentation/installation/installing-images/) pada sd card untuk Raspberry pi.
2. Masukkan token untuk bot yang akan digunakan ke script API telegram.
3. ```
   ...
   def main():
       # Create the EventHandler and pass it your bot's token.
       updater = Updater("458534210:AAHOeYPZamMU9bqH-MV36tOBnKj4FhWuvoo")
       ...
   ```

   Buat script menggunakan python untuk mengendalikan servo \(e.g. servobuka.py dan servotutup.py, dengan perubahan sudut yang digunakan untuk pintu garasi 90°\).
4. Buat script menggunakan python untuk mengendalikan lampu led \(e.g. lampu1nyala.py dan lampu1mati.py\).
5. Masukkan command yang diinginkan sesuai dengan kebutuhan ke script API Telegram.

### Step 

Sesuaikan _jumper wire _yang dibutuhkan untuk menyambungkan Raspberry pi dengan servo \(_female-female_\) maupun board \(_male-female_\).





