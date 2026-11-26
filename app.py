from flask import Flask, render_template, request

app = Flask(__name__)

# Mengizinkan method GET (untuk membuka halaman) dan POST (untuk mengirim data)
@app.route("/", methods=["GET", "POST"])
def index():
    hasil_parsing = None

    if request.method == "POST":
        # Mengambil nilai parameter berdasarkan atribut 'name' pada TextField HTML
        nama_user = request.form.get("nama_pengguna")
        hasil_parsing = f"Halo, {nama_user}! Data berhasil diparsing menggunakan method POST."

    return render_template("index.html", hasil=hasil_parsing)

if __name__ == "__main__":
    app.run(debug=True)