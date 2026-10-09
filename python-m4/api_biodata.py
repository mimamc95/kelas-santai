# Tugas: api_biodata.py
# GET / -> pesan sambutan
# GET /biodata ->JSON:nama,kota, hobi(list)
# GET /halo/<nama> -> sapaan personal
# GET /umur/<int:tahun> -> hitung 2026 - tahun lahir
# sertakan requirement.txt (flask) Kumpulkan folder/zip/github


from flask import Flask, jsonify
app = Flask(__name__) 

@app.route("/")
def index():
    return ("Hai, selamat datang di api biodata saya")
    

## Running framework Flask  @localhost:5000
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
