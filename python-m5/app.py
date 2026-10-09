from flask import Flask, jsonify, request
import json


app = Flask(__name__)

#  Read Data
@app.route("/", methods= ["GET"])
def beranda ():
   return ("Selamat datang di REST API Python @Meeting-5")

# Create Data
@app.route("/createNote", methods=["POST"])
def createNote():
    # Buka file database.json dengan mode write jika file kosong
    try:
        with open("database.json", "r") as f:
            dataLama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        dataLama = []

    # Terima data JSON dari Request
    data = request.get_json()
    idNote = data["idNote"]
    title = data["title"]
    content = data["content"]

    dataBaru = {"idNote":idNote, "title":title, "content":content}
    
    # Tambahkan data dengan Append
    dataLama.append(dataBaru)

    # Simpan kembali ke dalam Database 
    with open("database.json", "w") as f:
        json.dump(dataLama, f, indent=4)

    return jsonify({
        "status": 201,
        "message": "Data berhasil ditambahkan",
        "data": dataBaru
    }), 201

# Read All Data
@app.route("/getNote", methods=["GET"])
def getRoute():
    # Buka file dengan nama database.json
    with open("database.json", "r") as f:
        data = json.load(f)

        return jsonify({
            "status":200,
            "message":"data berhasil diambil.",
            "data":data
        }), 200

# Read Data By ID
@app.route("/getNoteById/<int:idNote>",methods = ["GET"])
def getNoteByID(idNote):
    # Buka file dengan nama database.json
    with open ("database.json", "r") as f:
        data =json.load(f)  # Mencari data berdasarkan Id Note yang di input 

        # Lakukan validasi, kembalikan 404 jika data tidak ditemukan dan kalau kosong kembalikan 400
        if idNote == 0:
            return jsonify({
              "status": 400,
              "message": "ID tidak boleh 0"  
            }), 400
        else:
            # Lakukan perulangan untuk mencari data berdasarkan ID yang di input
            for data in data:
                if data["idNote"] == idNote:
                    return jsonify({
                        "status": 200,
                        "message": "Data berhasil ditemukan",
                        "data":data
                    }), 200
            #  Jika data tidak ditemukan maka kembalikan 404
            return jsonify({
                "status":404,
                "message": "Data tidak ditemukan",
            }), 404


# Update Data By ID



# Delete Data By ID
@app.route("/deleteNote/<int:idNote>", methods=["DELETE"])
def deleteNote(idNote):

    # Lakukan validasi, kembalikan 404 jika data tidak ditemukan dan kalau kosong kembalikan 400
    if idNote == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0"
        }), 400

    # Buka file database.json dengan mode write jika file kosong
    try:
        with open("database.json", "r") as f:
            daftarNote = json.load(f)
    except (json.JSONDecodeError,FileNotFoundError):
            daftarNote = []

    # Lakukan perulangan untuk mencari data berdasarkan ID yang di input
    for note in daftarNote:
        if note["idNote"] == idNote:
            # Hapus catatan dari daftar
            daftarNote.remove(note)

            # Simpan perubahan ke file database.json
            with open("database.json", "w") as f:
                json.dump(daftarNote, f, indent=4)

            return jsonify({
                "status": 200,
                "message": "Data berhasil dihapus",
                "data": note
    }), 200

    # Jika data tidak ditemukan
    return jsonify({
        "status": 404,
        "message": "Data tidak ditemukan"
    }), 404


#  Running Flask at http://localhost:5000/
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
