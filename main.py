from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
feedback_storage = []

# ---------- AUDIO BONUS ----------
page_turn_sound = '''
    <audio id="flipSound">
        <source src="/static/page-turn.mp3" type="audio/mpeg">
    </audio>
'''
# ---------- GLOBAL STYLE & SCRIPT ----------
base_style_and_script = '''
    <style>
        @keyframes fadeOut {
            from { opacity: 1; transform: rotateY(0deg); }
            to { opacity: 0; transform: rotateY(90deg); }
        }

        body {
            animation: fadeIn 0.6s ease-in;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-image: url('/static/sincan.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            font-family: sans-serif;
            color: #ffffff;
            text-align: center;
            padding: 40px 10px;
        }

        .circle-btn {
            position: fixed;
            top: 50%;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: rgba(255,255,255,0.8);
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #333;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
            z-index: 999;
        }

        #nextBtn { right: 20px; }
        #backBtn { left: 20px; }

        .page-container {
            transition: transform 0.8s ease, opacity 0.8s ease;
            transform-origin: left;
        }

        .fade-out {
            animation: fadeOut 0.8s ease forwards;
        }

        .centered-img {
            max-width: 300px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
    </style>

    <audio id="bgAudio" loop>
    <source src="/static/too_good.mp3" type="audio/mpeg">
</audio>

<script>
    // Agar lagu tetap main saat pindah halaman
    window.addEventListener("DOMContentLoaded", function() {
        const bgAudio = document.getElementById("bgAudio");
        if (sessionStorage.getItem("musicStarted") === "true") {
            bgAudio.play().catch(() => {});
        }

        window.playMusic = function() {
            bgAudio.play();
            sessionStorage.setItem("musicStarted", "true");
        };
    });
</script>

    <script src="/static/script.js"></script>
'''

def render_page(content, current_page, total_pages=9):
    prev_btn = f'''
        <form class="nav-form" action="{{{{ url_for('page{current_page - 1}') }}}}" method="get">
            <button type="submit" class="circle-btn" id="backBtn">&#8592;</button>
        </form>''' if current_page > 1 else ''

    next_btn = f'''
        <form class="nav-form" action="{{{{ url_for('page{current_page + 1}') }}}}" method="get">
            <button type="submit" class="circle-btn" id="nextBtn">&#8594;</button>
        </form>''' if current_page < total_pages else ''

    return render_template_string(f'''
        <html>
        <head>
            <title>Page{current_page}</title>
            {base_style_and_script}
        </head>
        <body>
            {page_turn_sound}
            {prev_btn}
            {next_btn}
            <div class="page-container">
                {content}
            </div>
        </body>
        </html>
    ''')

@app.route("/")
def page1():
    return render_page('''
        <h1>hai be!</h1>
        <p style="max-width:500px; margin:auto;">
            <b>sebelum kamu mulai scroll, aku mau kasih tau dikit</b><br><br>
            di halaman ini ada lagu yang aku pasang buat nemenin kamu baca,<br>
            jangan lupa untuk kamu klik dulu lagunya yaa 🔉<br><br>

            play music 🎵<br><br>
            <button onclick="playMusic()" style="
                padding: 10px 20px;
                font-size: 16px;
                background-color: #ffffffcc;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                color: #333;
                box-shadow: 1px 1px 8px rgba(0,0,0,0.2);">
                ▶️ Play Lagu: Too Good To Say Goodbye
            </button>

            <br><br>
            buat navigasi, kamu tinggal klik tombol <b>panah kanan</b> di sebelah kanan layar buat lanjut,<br>
            dan <b>panah kiri</b> kalau kamu mau balik ke halaman sebelumnya ⬅️➡️<br><br>
            selamat menikmati be!
        </p>
    ''', 1)

@app.route("/page2")
def page2():
    return render_page('''
        <p style="max-width:600px; margin:auto;">
            <b>sebelumnya, aku buat project ini semingguan</b><br><br>
            dari banyak error, layar tiba-tiba hitam, lagu yang ga muncul di Safari, dan segala macemnya<br>
            aku benerin semuanya dan alhamdulillah di hari Rabu project ini bisa jalan<br><br>
            ini tempatku ngungkapin isi hati — biar kamu ga bosan, aku luangin waktuku buat bikin ini <br><br>
            maaf ya be kalo jelek, aku udah coba semaksimal mungkin..<br><br>
            sebenernya program ini udah jadi, tapi aku revisi ulang karena sebelumnya background-nya dinosaurus wkwk 😅<br>
            akhirnya aku ganti jadi Sincan — biar sesuai kesukaanmu <br><br>
            <b>hope u like it!</b>
        </p>
    ''', 2)

@app.route("/page3")
def page3():
    return render_page('''
        <img src="/static/something.jpg" class="centered-img">
        <p style="max-width:600px; margin:auto;">
            <b>kamu masih inget ga ini pap yang kamu kirim ke aku tanggal 1 Maret?</b><br><br>
            kamu pap es krim, dan aku notice sampe aku simpen baik-baik <br><br>
            pas kita ketemu Day 1 aku beliin es krim itu ke kamu (dua malah!) 🍦<br>
            sayangnya kamu ga makan karena keburu mencair, gapapa kok!
        </p>
    ''', 3)

@app.route("/page4")
def page4():
    return render_page('''
        <img src="/static/try.png" class="centered-img">
        <p style="max-width:600px; margin:auto;">
            <b>be tau ga...</b><br>
            setiap kita salah paham atau ada yang bikin kamu sedih, aku selalu catet itu <br>
            biar aku bisa belajar, inget, dan ga ngulangin kesalahan yang sama<br><br>
            aku minta maaf atas semua kondisi yang bikin kita sekarang ga sejalan<br>
            maaf aku masih banyak salahnya ke kamu 🥺
        </p>
    ''', 4)

@app.route("/page5")
def page5():
    return render_page('''
        <img src="/static/dongeng.png" class="centered-img">
        <p style="max-width:600px; margin:auto;">
            hal yang paling aku tunggu tiap malam itu... <b>dongengin kamu</b> 💬<br><br>
            tapi tiap kali aku mau dongeng, aku selalu catet biar ga kelamaan kamu nungguin aku 
        </p>
    ''', 5)

@app.route("/page6")
def page6():
    return render_page('''
        <p style="max-width:600px; margin:auto; line-height:1.6;">
            aku tau kok, kondisi kita sekarang lagi ga baik-baik aja...<br><br>
            tapi sebelum aku nyerah, aku mau tau...<br>
            <b>masih bisa ga ya kita balik seperti dulu?</b><br><br>
            cerita tiap malam, saling becanda dengan spontan, aku kangen banget itu <br>
            aku tau LDR bikin kamu bosan, dan aku ngerti kok. Tapi aku juga udah coba...<br><br>
            aku cuma butuh kamu ikut coba bareng aku <br><br>
            kita pernah janji buat belajar jadi lebih baik satu sama lain kan?<br>
            yuk biasain ngobrolin masalah hari itu, jangan tidur dalam keadaan berat hati...<br><br>
            be, lihat aku ya... ini mungkin langkah terakhir aku buat kita<br>
            aku masih mau bareng kamu, jatuh bangun sama kamu <br>
            <b>aku masih mau belajar jadi pria yang baik buat kamu</b><br>
            masih banyak kota-kota yang harus kita taklukan bareng...<br><br>
            tapi kalau setelah baca semua ini kamu tetep ga ngerasa apa-apa...<br>
            gapapa, mungkin aku pantas sakit dan kecewa sekarang.<br><br>
            kita udah belajar sabar dan kuat, kita keren banget ya kalo diliat-liat...
        </p>
    ''', 6)

@app.route("/page7", methods=["GET", "POST"])
def page7():
    if request.method == "POST":
        message = request.form.get("feeling")
        if message:
            feedback_storage.append(message.strip())
        return redirect(url_for("page7", thanks=1))

    thank_you_message = ''
    if request.args.get("thanks"):
        thank_you_message = '''
            <div class="feedback-box" style="background-color: rgba(200,255,200,0.9);">
                <p style="color:#004400;">terima kasih yaa sayang sudah ngisi!</p>
            </div>
        '''

    return render_page(f'''
        <img id="slideImage" src="/static/wle.jpg" class="centered-img">
        <p style="max-width:600px; margin:auto;">
            <b>terima kasih udah baca sampai akhir ya!</b><br><br>
            semalam aku ngerjain ini, padahal harusnya ngerjain laprak hehe<br>
            tapi aku anak teknik juga, jadi mau unjuk skill dikit wkwkw<br><br>
            jaga kesehatan ya be, minum vitaminnya jangan lupa!<br>
            aku ga pernah salah kasih kamu julukan... <b>POAT — Prettiest of All Time 💐</b><br><br>
            have a nice day, fighter — <b>Fitriya Rahmah!</b>
        </p>

        <form method="POST">
            <div class="feedback-box">
                <p>boleh kamu utarain ga perasaan kamu setelah lihat ini?<br>
                aku pengen tau dong 💌</p>
                <textarea name="feeling" placeholder="tulis di sini ya be"></textarea><br><br>
                <button type="submit">Enter</button>
            </div>
        </form>

        {thank_you_message}

        <script>
            const images = [
                "/static/wle.jpg",
                "/static/koki.jpg",
                "/static/first.jpg",
                "/static/aww.jpg"
            ];
            let current = 0;
            const slide = document.getElementById("slideImage");
            setInterval(() => {{
                current = (current + 1) % images.length;
                slide.src = images[current];
            }}, 2000);
        </script>
    ''', 7)

@app.route("/page8")
def page8():
    return render_page('''
        <div class="closing-box" style="max-width:600px; margin:auto;">
            <p>
                <b>malam kemarin kamu sempat tanya kenapa aku masih bertahan di sini?</b><br><br>
                beberapa kali aku kecewa, tapi aku tetap respon kamu baik, dan aku kasih kesempatan berkali-kali...<br><br>
                kenapa?<br>
                karena aku pengen bawa kamu keluar dari zona toxic yang bikin kamu keras dan susah terbuka.<br><br>
                aku gamau lihat kamu tenggelam dalam gelap, ga tau arah, dan ga tau harus mulai dari mana...<br><br>
                kalau kamu nanya, apa aku capek? sedih? mental lelah?<br>
                <b>iya</b>. Tapi lebih sedih lagi kalau aku gagal bantu kamu keluar dari zona itu.
            </p>
        </div>
    ''', 8)

@app.route("/page9")
def page9():
    return render_template_string(f'''
        <html>
        <head>
            <title>Penutup</title>
            {base_style_and_script}
            <style>
                .closing-box {{
                    max-width: 600px;
                    margin: auto;
                    text-align: center;
                }}
                .big-button {{
                    background-color: #ff7eb9;
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    font-size: 18px;
                    border-radius: 12px;
                    cursor: pointer;
                    margin-top: 20px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                }}
            </style>
        </head>
        <body>
            {page_turn_sound}

            <!-- Background music for page 9 -->
            <audio controls>
                    <source src="/static/love_lesson_skyline.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>

            <div class="closing-box">
                <p>
                    <b>makasih yaa be udah baca semuanya sampai akhir 💌</b><br><br>
                    aku tau isinya panjang banget, sampe aku bingung sendiri sama program yang aku buat haha<br><br>
                    kalau kamu udah baca semua dan mau nutup halamannya,<br>
                    tinggal klik tombol di bawah ini yaa 🫶
                </p>

                <p style="color:#ffdcdc; margin-top:30px;">
                    💡 <b>Note:</b><br>
                    oh iya be, di halaman ini lagunya beda ya 🎶<br>
                    jadi <b>pause dulu lagu yang tadi</b>,<br>
                    lalu <b>klik tombol play di bawah ini</b> buat putar lagu spesial Page 9 💗
                </p>

                <p style="margin-top: 40px; font-style: italic;">
                    i'm sending u this because i want u to know how truly grateful i am<br>
                    to have met someone as amazing as u and u mean the world to me.<br><br>

                    i hope u know how glad i am to have u in my life,<br>
                    and i wish i never have to lose u.<br><br>

                    u're incredible, u make me smile and laugh so much.<br>
                    u're my favorite destination, my home. <br><br>

                    please don't be too hard on urself, because u're more than enough.<br>
                    i love u so much <br><br>

                    <b>remember fit, as long as i'm alive u'll always have someone<br>
                    who's proud of u in everything.</b>
                </p>

                <form action="/goodbye">
                    <button type="submit" class="big-button">Selesai 💌</button>
                </form>
            </div>
        </body>
        </html>
    ''')

@app.route("/lihat_pesan_rahasia")
def lihat_pesan_rahasia():
    result = "<h2>📥 Semua Respon yang Masuk:</h2><ul>"
    for i, msg in enumerate(feedback_storage, 1):
        result += f"<li><b>{i}.</b> {msg}</li><br>"
    result += "</ul>"
    return render_template_string(f'''
        <html>
        <head>{base_style_and_script}</head>
        <body>{result}</body>
        </html>
    ''')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)