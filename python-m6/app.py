from datetime import datetime               # Untuk memanage waktu
import os                                   # Untuk membaca environment variable
from flask import Flask, jsonify, request   # Framework WEB untuk REST API dari python

# Sebuah module ORM agar bisa terhubung ke databse
from sqlalchemy import create_engine, String, DateTime, select, ForeignKey                 # Type data
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship   # ORM dari sqlalchemy 

app = Flask (__name__)
app.json.sort_keys = False  # Agar urutan key JSON sesuai dengan urutan dictionary


# Koneksi ke MySQL (port: 3306) menggunakan driver PyMySQL
# Format : mysql+pymysql://user:password@host:port/nama_database
DATABASE_URL = os.getenv(
    "DATABASE_URL","mysql+pymysql://root:@localhost:3306/perpustakaan"
    ) 
engine = create_engine(DATABASE_URL, pool_pre_ping= True)   # Fungsi untuk mengaktifkan database


# Config Model Database SQLAlchemy 
class Base(DeclarativeBase): 
    pass

# Class tabel Penulis Buku
class Penulis(Base):
    __tablename__ = "penulis"
    idPenulis: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    namaPenulis: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    createdAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updatedAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def info(self):
        return {
            "idPenulis": self.idPenulis,
            "namaPenulis": self.namaPenulis,
            "email": self.email,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }

# Class tabel Kategori Buku
class Kategori(Base):
    __tablename__ = "kategori"
    idKategori: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    namaKategori: Mapped[str] = mapped_column(String(100))
    deskripsi: Mapped[str] = mapped_column(String(255))
    createdAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updatedAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def info(self):
        return {
            "idKategori": self.idKategori,
            "namaKategori": self.namaKategori,
            "deskripsi": self.deskripsi,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }

# Class tabel Buku
class Buku(Base):
    __tablename__ = "buku"
    idBuku: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    judul: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str] = mapped_column(String(13))
    tahunTerbit: Mapped[int] = mapped_column(String(10))
    harga: Mapped[int] = mapped_column(String(10))
    idPenulis: Mapped[int] = mapped_column(ForeignKey("penulis.idPenulis"))
    idKategori: Mapped[int] = mapped_column(ForeignKey("kategori.idKategori"))
    createdAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updatedAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    # Relasi ORM ke Penulis dan Kategori supaya bisa memanggil info() dalam bentuk json / dictionary 
    penulis: Mapped["Penulis"] = relationship()
    kategori: Mapped["Kategori"] = relationship()

    def info(self):
        return {
            "idBuku": self.idBuku,
            "judul": self.judul,
            "isbn": self.isbn,
            "harga": self.harga,
            "idKategori": self.idKategori,
            "kategori": self.kategori.info() if self.kategori else None,
            "idPenulis": self.idPenulis,
            "penulis": self.penulis.info() if self.penulis else None,
            "tahunTerbit": self.tahunTerbit,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }

# Buat tabel otomatis jika tabel belum ada
Base.metadata.create_all(engine)

# Beranda REST API
@app.route("/api/", methods= ["GET"])
def beranda():
    return "Hallo, selamat datang di System REST API Perpustakaan dengan MySQL + SQLAlchemy"

# Create Penulis Buku
@app.route("/api/penulis", methods= ["POST"])
def create_penulis():
    data = request.get_json()
    if not data or not "namaPenulis" in data or not "email" in data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        # Apakah email sudah terdaftar di database?
        statement = select(Penulis).where(Penulis.email == data["email"])
        penulisTerdaftar = session.scalars(statement).first()

        # Email sudah terdaftar?
        if penulisTerdaftar:
            return jsonify({
                "status": "Conflict",
                "message": f"Email {data['email']} sudah terdaftar di database"
            }),409
            
        # Simpan email jika belum terdaftar
        penulis = Penulis(
            namaPenulis = data["namaPenulis"],
            email = data["email"]
            )
        session.add(penulis)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data penulis berhasil ditambahkan",
            "data": penulis.info()
        }), 201

# Read Semua Penulis Buku
@app.route("/api/penulis", methods= ["GET"])
def get_penulis():
    with Session(engine) as session:
        penulis = session.query(Penulis).all()
        return jsonify({
            "status": "Success",
            "message": "Data penulis berhasil diambil",
            "data": [p.info() for p in penulis]
        }), 200    

# Read Penulis Buku berdasarkan ID
@app.route("/api/penulis/<int:idPenulis>", methods= ["GET"])
def get_penulis_by_id(idPenulis: int):
    with Session(engine) as session:
        penulis = session.get(Penulis, idPenulis)
        if not penulis:
            return jsonify({"error": "Penulis tidak ditemukan"}), 404
        return jsonify({
            "status": "Success",
            "message": "Data penulis berhasil diambil",
            "data": penulis.info()
        }), 200

# Update Penulis Buku berdasarkan ID
@app.route("/api/penulis/<int:idPenulis>", methods= ["PUT"])
def update_penulis(idPenulis: int):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        penulis = session.get(Penulis, idPenulis)
        if not penulis:
            return jsonify({"error": "Penulis tidak ditemukan"}), 404
        if "namaPenulis" in data:
            penulis.namaPenulis = data["namaPenulis"]
        if "email" in data:
            penulis.email = data["email"]
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data penulis berhasil diupdate",
            "data": penulis.info()
        }), 200

# Delete Penulis Buku berdasarkan ID
@app.route("/api/penulis/<int:idPenulis>", methods= ["DELETE"])
def delete_penulis(idPenulis: int):
    with Session(engine) as session:
        penulis = session.get(Penulis, idPenulis)
        if not penulis:
            return jsonify({"error": "Penulis tidak ditemukan"}), 404

        # Cek apakah penulis masih memiliki data buku terkait
        statement = select(Buku).where(Buku.idPenulis == idPenulis)
        bukuTerkait = session.scalars(statement).first()
        if bukuTerkait:
            return jsonify({
                "error": "Conflict",
                "message": "Penulis tidak dapat dihapus karena masih memiliki relasi dengan data buku"
            }), 409

        # Hapus jika tidak memiliki relasi 
        session.delete(penulis)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Penulis berhasil dihapus",
            "data": penulis.info()
        }), 200        

# Create Kategori Buku
@app.route("/api/kategori", methods=["POST"])
def create_kategori():
    data = request.get_json()
    if not data or not "namaKategori" in data or not "deskripsi" in data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        # Apakah kategori sudah terdaftar di database?
        statement = select(Kategori).where(Kategori.namaKategori == data["namaKategori"])
        kategoriTerdaftar = session.scalars(statement).first()

        # Kategori sudah terdaftar?
        if kategoriTerdaftar:
            return jsonify({
                "error": "Conflict",
                "message": f"Kategori {data['namaKategori']} sudah terdaftar di database"
            }),409
            
        # Simpan kategori jika belum terdaftar
        kategori = Kategori(
            namaKategori = data["namaKategori"],
            deskripsi = data["deskripsi"]
            )
        session.add(kategori)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data kategori berhasil ditambahkan",
            "data": kategori.info()
        }), 201

# Read Semua Kategori Buku
@app.route("/api/kategori", methods=["GET"])
def get_kategori():
    with Session(engine) as session:
        kategori = session.query(Kategori).all()
        return jsonify({
            "status": "Success",
            "message": "Data kategori berhasil diambil",
            "data": [k.info() for k in kategori]
        }), 200    

# Read Kategori Buku berdasarkan ID
@app.route("/api/kategori/<int:idKategori>", methods=["GET"])
def get_kategori_by_id(idKategori: int):
    with Session(engine) as session:
        kategori = session.get(Kategori, idKategori)
        if not kategori:
            return jsonify({"error": "Kategori tidak ditemukan"}), 404
        return jsonify({
            "status": "Success",
            "message": "Data kategori berhasil diambil",
            "data": kategori.info()
        }), 200

# Update Kategori Buku berdasarkan ID
@app.route("/api/kategori/<int:idKategori>", methods=["PUT"])
def update_kategori(idKategori: int):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        kategori = session.get(Kategori, idKategori)
        if not kategori:
            return jsonify({"error": "Kategori tidak ditemukan"}), 404
        if "namaKategori" in data:
            kategori.namaKategori = data["namaKategori"]
        if "deskripsi" in data:
            kategori.deskripsi = data["deskripsi"]
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data kategori berhasil diupdate",
            "data": kategori.info()
        }), 200

# Delete Kategori Buku berdasarkan ID
@app.route("/api/kategori/<int:idKategori>", methods=["DELETE"])
def delete_kategori(idKategori: int):
    with Session(engine) as session:
        kategori = session.get(Kategori, idKategori)
        if not kategori:
            return jsonify({"error": "Kategori tidak ditemukan"}), 404

        # Cek apakah kategori masih memiliki data buku terkait
        statement = select(Buku).where(Buku.idKategori == idKategori)
        bukuTerkait = session.scalars(statement).first()
        if bukuTerkait:
            return jsonify({
                "error": "Conflict",
                "message": "Kategori tidak dapat dihapus karena masih memiliki relasi dengan data buku"
            }), 409

        # Hapus jika tidak memiliki relasi 
        session.delete(kategori)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data kategori berhasil dihapus",
            "data": kategori.info()
        }), 200        

# Create Buku
@app.route("/api/buku", methods= ["POST"])
def create_buku():
    data = request.get_json()
    if not data or not "judul" in data or not "isbn" in data or not "tahunTerbit" in data or not "harga" in data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        # Apakah isbn sudah terdaftar di database?
        statement = select(Buku).where(Buku.isbn == data["isbn"])
        bukuTerdaftar = session.scalars(statement).first()

        # Buku sudah terdaftar?
        if bukuTerdaftar:
            return jsonify({
                "error": "Conflict",
                "message": f"Buku dengan ISBN {data['isbn']} sudah terdaftar di database"
            }),409
            
        # Simpan buku jika belum terdaftar
        buku = Buku(
            judul = data["judul"],
            isbn = data["isbn"],
            tahunTerbit = data["tahunTerbit"],
            harga = data["harga"],
            idPenulis = data["idPenulis"],
            idKategori = data["idKategori"]
            )
        session.add(buku)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil ditambahkan",
            "data": buku.info()
        }), 201

# Read Semua Buku
@app.route("/api/buku", methods= ["GET"])
def get_buku():
    with Session(engine) as session:
        buku = session.query(Buku).all()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diambil",
            "data": [b.info() for b in buku]
        }), 200    

# Read Buku berdasarkan ID
@app.route("/api/buku/<int:idBuku>", methods= ["GET"])
def get_buku_by_id(idBuku: int):
    with Session(engine) as session:
        buku = session.get(Buku, idBuku)
        if not buku:
            return jsonify({"error": "Buku tidak ditemukan"}), 404
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diambil",
            "data": buku.info()
        }), 200

# Update Buku berdasarkan ID
@app.route("/api/buku/<int:idBuku>", methods= ["PUT"])
def update_buku(idBuku: int):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data kurang lengkap"}), 400
    with Session(engine) as session:
        buku = session.get(Buku, idBuku)
        if not buku:
            return jsonify({"error": "Buku tidak ditemukan"}), 404
        if "judul" in data:
            buku.judul = data["judul"]
        if "isbn" in data:
            buku.isbn = data["isbn"]
        if "tahunTerbit" in data:
            buku.tahunTerbit = data["tahunTerbit"]
        if "harga" in data:
            buku.harga = data["harga"]
        if "idPenulis" in data:
            buku.idPenulis = data["idPenulis"]
        if "idKategori" in data:
            buku.idKategori = data["idKategori"]
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diupdate",
            "data": buku.info()
        }), 200

# Delete Buku berdasarkan ID
@app.route("/api/buku/<int:idBuku>", methods= ["DELETE"])
def delete_buku(idBuku: int):
    with Session(engine) as session:
        buku = session.get(Buku, idBuku)
        if not buku:
            return jsonify({"error": "Buku tidak ditemukan"}), 404

        # Cek apakah Buku masih memiliki data buku terkait
        statement = select(Buku).where(Buku.idBuku == idBuku)
        bukuTerkait = session.scalars(statement).first()
        if bukuTerkait:
            return jsonify({
                "error": "Conflict",
                "message": "Buku tidak dapat dihapus karena masih memiliki relasi dengan data Penulis atau Kategori"
            }), 409

        # Hapus jika tidak memiliki relasi 
        session.delete(buku)
        session.commit()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil dihapus",
            "data": buku.info()
        }), 200
     

# Filter Penulis Buku
@app.route("/api/buku/penulis/<int:idPenulis>", methods= ["GET"])
def get_buku_by_penulis(idPenulis: int):
    with Session(engine) as session:
        buku = session.query(Buku).filter(Buku.idPenulis == idPenulis).all()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diambil",
            "data": [b.info() for b in buku]
        }), 200

# Filter Kategori Buku
@app.route("/api/buku/kategori/<int:idKategori>", methods= ["GET"])
def get_buku_by_kategori(idKategori: int):
    with Session(engine) as session:
        buku = session.query(Buku).filter(Buku.idKategori == idKategori).all()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diambil",
            "data": [b.info() for b in buku]
        }), 200

# Cari Judul Buku
@app.route("/api/buku/judul/<string:judul>", methods= ["GET"])
def get_buku_by_judul(judul: str):
    with Session(engine) as session:
        buku = session.query(Buku).filter(Buku.judul == judul).all()
        return jsonify({
            "status": "Success",
            "message": "Data buku berhasil diambil",
            "data": [b.info() for b in buku]
        }), 200

#  Running Flask at http://localhost:5000/
if __name__ == "__main__":
    app.run(host='127.0.0.1', port= 5000, debug=True)