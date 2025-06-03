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

    <audio id="bgAudio" autoplay loop>
        <source src="/static/too_good.mp3" type="audio/mpeg">
    </audio>

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
            <title>Page {current_page}</title>
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
            <b>sebelum kamu mulai scroll, aku mau kasih tau dikit <br><br>
            di halaman ini ada lagu yang aku pasang buat nemenin kamu baca,
            jadi jangan lupa nyalain volume kamu yaa <br><br>
            buat navigasi, kamu tinggal klik tombol <b>panah kanan</b> di sebelah kanan layar buat lanjut,<br>
            dan <b>panah kiri</b> kalau kamu mau balik ke halaman sebelumnya ⬅️➡️<br><br>
            selamat menikmati be!
        </p>
    ''', 1)


@app.route("/page2")
def page2():
    return render_page('''
        <p><b>sebelumnya, akup buat project ini semingguan<br>
        dan dari project yang aku buat ini buat kamu, dari yang banyak error nya, tiba tiba jadi hitam selayar,
        lagu nya ga muncul kalo di play si safari dan segala macem nya.<br>
        aku benerin semuanya, alhamdulillahnya di hari rabu project ini bisa aku jalanin<br>
        dan disini aku mau ngutarain perasaan ku dan kamu juga tapi lewat yang aku kerjakan ini,
        <br>kesannya biar ga boring jadinya aku luangin waktuku buat bikin ini deh<br>
        cuman maaf ya be kalo jelek, im tryinggg my best to make it..
        <br>tadi tu ya sebenernya program nya uda jadi tapi tiba tiba aku revisi ulang <br>karena background sebelumnya nya
        yang aku pilih dinosaurus wkwkw <br><b>dan akhirnya, aku ganti sincan agar biar sesuai kesukaanmu!</br>
        <b>hope u like it!<br>
    ''', 2)

@app.route("/page3")
def page3():
    return render_page('''
        <img src="/static/something.jpg" class="centered-img">
        <p>
        <b>kamu masi inget ga ini pap kamu yang kamu kasih ke aku tanggal 1 maret,<br>
        kamu kasi pap aku eskrim dan aku notice trus simpen baik baik<br><br>
        pas kita ketemu kemarin day 1 aku beliin kamu eskrim ini tau 2,<br>
        sayang ga kamu makan ya karena uda mencair duluan wkwkwk gapapa </p>
    ''', 3)

@app.route("/page4")
def page4():
    return render_page('''
        <img src="/static/try.png" class="centered-img">
        <p>
        <b>be tau ga setiap aku mungkin ada salah atau kita misscom,<br>
        aku selalu catet itu agar aku bisa inget,<br>
        terus belajar jadi lebih baik dan berusaha sebaik mungkin<br>
        untuk tidak mengulangi hal tersebut.<br><br>
        aku minta maaf atas kondisi yang terjadi sama kita sekarang,<br>maaf aku masih banyak salah ke kamu dan
        kita jadi ga searah sekarang
        </p>
    ''', 4)

@app.route("/page5")
def page5():
    return render_page('''
        <img src="/static/dongeng.png" class="centered-img">
        <p>
        <b>sekarang hal dongengin kamu adalah hal yang aku tungguin tau be,<br>
        tapi ga lupa tiap aku mau dongengin kamu<br>
        selalu aku catet biar ga kelamaan kamu nunggu nya hehe..
        </p>
    ''', 5)

@app.route("/page6")
def page6():
    return render_page('''
        <p style="max-width:600px; line-height:1.6;">
            <b>aku tau kok be kondisi kita sekarang kita lagi ga baik baik saja,<br>
            tapi sebelum aku nyerah, aku masih pingin tau<br>
            <b>masih bisa ga ya kita balik seperti dulu.<br><br>
            tukar cerita setiap malam setelah apa yang kita lewatin hari itu,<br>
            kita becanda dengan respon natural yang biasanya, jujur aku kangen hal itu<br>
            aku tahu kondisi LDR ini bikin kamu bosan<br>
            dan aku sebenernya try kok be buat ga gitu gitu juga.<br><br>
            aku juga mau coba hal baru dan seru bareng kamu<br>
            tapi, aku juga ga bisa jalan sendiri..</b><br>
            <b>aku cuma butuh kamu buat ikut juga...<br>
            kita pernah sama sama mau coba menjadi better satu sama lain kan?<br>
            kamu bisa ga biasakan setiap kita ada masalah di hari itu, kita obrolin langsung,
            karena tidur dalam keadaan heavy hearts cause problem yang belum selesai<br>
            itu ga enak banget be, aku beberapa kali ngerasain itu sampai hambar<br>
            <br>be, look at me please on last i try for us. aku masih mau ngelangkah bareng sama kamu, 
            ngerasain jatuh bangun sama kamu<br>
            <b>aku masih mau belajar banyak menjadi pria yang baik buat kamu<br>
            masih banyak juga plan kota kota yang harus kita taklukan berdua<br>
            tapi.. jika setelah kamu membaca semua halaman yang aku buat ini dan tidak ada yang berubah dari perasaanmu sama sekali<br>
            tak apa, maybe i deserve all the pain and disappointment rn, i mean it is my fault, i should've done better.<br>
            gapapa aku ikhlas kita uda sejauh ini, kita berdua uda belajar sabar<br>
            kita keren ya kalo diliat liat.. <br>
        </p>
    ''', 6)

@app.route("/page7", methods=["GET", "POST"])
def page7():
    if request.method == "POST":
        message = request.form.get("feeling")
        if message:
            feedback_storage.append(message.strip())  # Tersimpan hanya untuk kamu
        return redirect(url_for("page7", thanks=1))

    # Tampilkan ucapan terima kasih jika ada
    thank_you_message = ''
    if request.args.get("thanks"):
        thank_you_message = '''
            <div class="feedback-box" style="background-color: rgba(200,255,200,0.9);">
                <p style="color:#004400;">terima kasih yaa sayang sudah ngisi!</p>
            </div>
        '''

    return render_page(f'''
        <img id="slideImage" src="/static/wle.jpg" class="centered-img">
        <p><b>terimakasih udah mau baca sampai akhir ya!<br>
        aku semaleman ngerjain ini be harusnya aku buat laprak cuman
        gampang deh besok aja bisa<br> mantan mu juga anak teknik jadi aku mau unjuk skill dikit wkwk.<br>
        <br>tetep jaga kesehatanmu ya, vitamin nya jangan lupa diminum
        <br>aku ga pernah salah kasih kamu julukan POAT <b> PRETTIEST OF ALL TIME
        <b><br>have a nice day fighter, <b>fitriya rahmah!</b></p>

        <form method="POST">
            <div class="feedback-box">
                <p>boleh kamu utarain ga perasaan kamu setelah lihat ini,<br>
                aku pengen tau dong</p>
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
        <div class="closing-box">
            <p>
                <b>oh iya saat kita conversation malam hari kemarin kemarin,<br>
                kamu sempat nanya kan? kenapa aku masih disini.<br><br>
                sekalian aku mau jawab, beberapa kali aku kecewa sama kamu,<br>
                tetapi aku masi meresponmu dengan baik bahkan ngasi kesempatan kamu untuk kesekian kali dan kalinya.</b><br><br>
                kalo kamu bertanya kenapa?<br>
                karna aku ingin bawa kamu keluar dari zona toxic mu be yang ngebuat watak mu jadi keras.<br><br>
                kalo aku bertanya lagi kenapa aku lakuin itu?<br>
                aku akan jawab bahwa aku gamau ngelihat seseorang kesesat didalam kegelepan<br>
                yang bahkan dia aja gatau harus keluar lewat mana dan dari mana serta harus mulai dari mana.<br><br>
                kalo kamu bertanya mengenai bagaimana perasaan aku apa?,<br>
                apa aku sedih?, apa aku lelah? cape? mental?<br>
                jawabannya jelas iya,
                tapi rasanya lebih ngena kalo aku gagal dan gabisa bawa kamu keluar dari zona itu.<b><br>
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
        </head>
        <body>
            {page_turn_sound}
            <div class="closing-box">
                <p>
                    <b>makasi yaa be udah mau baca semuanya sampai akhir <br><br>
                    <b>aku tau isinya banyak dan panjang, jujur sampe aku bingung sama program yang kubuat sendiri<br><br>
                    kalo kamu udah baca semuanya dan mau nutup halamannya,<br>
                    kamu bisa klik tombol di bawah ini yaa 🫶</b>
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