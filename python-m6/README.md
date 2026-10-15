# 📚 REST API Perpustakaan (Flask & SQLAlchemy)

Dokumentasi instalasi, konfigurasi, dan panduan pengujian endpoint REST API Perpustakaan menggunakan Flask, SQLAlchemy ORM, dan database MySQL.

---

## 📋 Daftar Isi
1. [Prasyarat Sistem](#-prasyarat-sistem)
2. [Konfigurasi Database](#-konfigurasi-database)
3. [Instalasi & Menjalankan Aplikasi](#-instalasi--menjalankan-aplikasi)
   - [1. Buka Terminal ke Folder Proyek](#1-buka-terminal-ke-folder-proyek)
   - [2. Buat Virtual Environment (venv_meeting6)](#2-buat-virtual-environment-venv_meeting6)
   - [3. Aktifkan Virtual Environment](#3-aktifkan-virtual-environment)
   - [4. Install Dependencies dari requirements.txt](#4-install-dependencies-dari-requirementstxt)
   - [5. Jalankan Aplikasi](#5-jalankan-aplikasi)
4. [Panduan Pengujian API dengan Postman](#-panduan-pengujian-api-dengan-postman)
   - [Daftar Endpoint](#ringkasan-endpoint)
   - [Detail Pengujian Tiap Endpoint](#detail-pengujian-tiap-endpoint)

---

## 💻 Prasyarat Sistem
Pastikan telah menginstal tools berikut di komputer:
* **Python 3.10+** (pastikan opsi `Add Python to PATH` dicentang saat instalasi)
* **MySQL Database Server** (melalui **XAMPP**, **Laragon**, atau MySQL Standalone)
* **Postman** (atau alternatif seperti *Thunder Client* / *Insomnia*)

---

## 🗄 Konfigurasi Database

1. Jalankan MySQL Service (misal buka **XAMPP Control Panel** lalu klik **Start** pada modul MySQL).
2. Buka MySQL client favorit Anda (phpMyAdmin, DBeaver, HeidiSQL, atau Terminal MySQL).
3. Buat database baru bernama `perpustakaan`:
   ```sql
   CREATE DATABASE perpustakaan;
   ```
4. *Konfigurasi Koneksi default di `app.py`:*
   ```text
   mysql+pymysql://root:@localhost:3306/perpustakaan
   ```
   > **Catatan:** Jika MySQL Anda memiliki password atau port berbeda, atur Environment Variable `DATABASE_URL` terlebih dahulu, contoh:
   > ```bash
   > # PowerShell
   > $env:DATABASE_URL="mysql+pymysql://username:password@localhost:3306/perpustakaan"
   > ```

---

## 🚀 Instalasi & Menjalankan Aplikasi

Ikuti langkah-langkah berikut secara berurutan:

### 1. Buka Terminal ke Folder Proyek
Buka terminal (PowerShell / Command Prompt) dan pastikan berada pada direktori `python-m6`:
```powershell
cd "<Lokasi_Folder>\python-m6"
```

### 2. Buat Virtual Environment (`venv_meeting6`)
Jalankan perintah berikut untuk membuat virtual environment bernama `venv_meeting6`:
```powershell
python -m venv venv_meeting6
```

### 3. Aktifkan Virtual Environment

Pilih perintah sesuai terminal yang Anda gunakan:

* **Windows PowerShell:**
  ```powershell
  .\venv_meeting6\Scripts\Activate.ps1
  ```
  *(Jika muncul pesan peringatan `Execution Policy`, jalankan perintah `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` terlebih dahulu)*

* **Windows Command Prompt (CMD):**
  ```cmd
  venv_meeting6\Scripts\activate.bat
  ```

* **Git Bash / Linux / macOS:**
  ```bash
  source venv_meeting6/Scripts/activate
  ```

Tanda jika virtual environment telah aktif: di awal baris terminal akan terdapat prefix `(venv_meeting6)`.

### 4. Install Dependencies dari `requirements.txt`
Pastikan virtual environment telah aktif, lalu jalankan:
```powershell
pip install -r requirements.txt
```

> **Info modul yang terpasang:**
> - `Flask` (Web framework)
> - `SQLAlchemy` (ORM Database)
> - `PyMySQL` (Driver koneksi Python ke MySQL)

### 5. Jalankan Aplikasi
Jalankan file `app.py`:
```powershell
python app.py
```

Jika berhasil, server akan berjalan dengan output seperti berikut:
```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```
Tabel database (`penulis`, `kategori`, dan `buku`) akan dibuat secara otomatis saat aplikasi pertama kali dijalankan.

---

## 📮 Panduan Pengujian API dengan Postman

Base URL: `http://localhost:5000` atau `http://127.0.0.1:5000`

### Koleksi Ringkasan Endpoint

| No | Modul | Method | Endpoint | Keterangan |
|---|---|---|---|---|
| 1 | **Beranda** | `GET` | `/api/` | Halaman selamat datang |
| 2 | **Penulis** | `POST` | `/api/penulis` | Tambah penulis baru |
| 3 | | `GET` | `/api/penulis` | Ambil semua data penulis |
| 4 | | `GET` | `/api/penulis/{idPenulis}` | Ambil data penulis berdasarkan ID |
| 5 | | `PUT` | `/api/penulis/{idPenulis}` | Update data penulis berdasarkan ID |
| 6 | | `DELETE` | `/api/penulis/{idPenulis}` | Hapus data penulis berdasarkan ID |
| 7 | **Kategori** | `POST` | `/api/kategori` | Tambah kategori baru |
| 8 | | `GET` | `/api/kategori` | Ambil semua data kategori |
| 9 | | `GET` | `/api/kategori/{idKategori}` | Ambil data kategori berdasarkan ID |
| 10 | | `PUT` | `/api/kategori/{idKategori}` | Update data kategori berdasarkan ID |
| 11 | | `DELETE` | `/api/kategori/{idKategori}` | Hapus data kategori berdasarkan ID |
| 12 | **Buku** | `POST` | `/api/buku` | Tambah buku baru |
| 13 | | `GET` | `/api/buku` | Ambil semua data buku |
| 14 | | `GET` | `/api/buku/{idBuku}` | Ambil data buku berdasarkan ID |
| 15 | | `PUT` | `/api/buku/{idBuku}` | Update data buku berdasarkan ID |
| 16 | | `GET` | `/api/buku/penulis/{idPenulis}` | Filter buku berdasarkan Penulis |
| 17 | | `GET` | `/api/buku/kategori/{idKategori}` | Filter buku berdasarkan Kategori |
| 18 | | `GET` | `/api/buku/judul/{judul}` | Cari buku berdasarkan Judul |

---

### Detail Pengujian Tiap Endpoint

> **PENTING untuk Request POST dan PUT:**
> Pada Postman, buka tab **Headers** dan pastikan ada `Content-Type: application/json`.
> Pada tab **Body**, pilih **raw** dan ubah formatnya ke **JSON**.

---

#### 1. Beranda API
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/`
* **Response Expected (200 OK):**
  ```text
  Hallo, selamat datang di System REST API Perpustakaan dengan MySQL + SQLAlchemy
  ```

---

#### 2. Penulis Buku (`/api/penulis`)

##### A. Create Penulis Buku
* **Method:** `POST`
* **URL:** `http://localhost:5000/api/penulis`
* **Body (JSON):**
  ```json
  {
    "namaPenulis": "Upin",
    "email": "upin@email.com"
  }
  ```
* **Response Expected (201 Created):**
  ```json
  {
    "status": "success",
    "message": "Buku berhasil ditambahkan",
    "data": {
      "idPenulis": 1,
      "namaPenulis": "Upin",
      "email": "upin@email.com",
      "createdAt": "2026-10-15T19:00:00",
      "updatedAt": "2026-10-15T19:00:00"
    }
  }
  ```

##### B. Get Semua Penulis Buku
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/penulis`
* **Response Expected (200 OK):**
  ```json
  {
    "status": "Success",
    "message": "Data penulis berhasil diambil",
    "data": [
      {
        "idPenulis": 1,
        "namaPenulis": "Upin",
        "email": "upin@email.com",
        "createdAt": "2026-10-15T19:00:00",
        "updatedAt": "2026-10-15T19:00:00"
      }
    ]
  }
  ```

##### C. Get Penulis berdasarkan ID
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/penulis/1`
* **Response Expected (200 OK):**
  ```json
  {
    "idPenulis": 1,
    "namaPenulis": "Upin",
    "email": "upin@email.com",
    "createdAt": "2026-10-15T19:00:00",
    "updatedAt": "2026-10-15T19:00:00"
  }
  ```

##### D. Update Penulis berdasarkan ID
* **Method:** `PUT`
* **URL:** `http://localhost:5000/api/penulis/1`
* **Body (JSON):**
  ```json
  {
    "namaPenulis": "Upin (Updated)",
    "email": "upin_new@email.com"
  }
  ```
* **Response Expected (200 OK):**
  ```json
  {
    "status": "Success",
    "message": "Data penulis berhasil diupdate",
    "data": {
      "idPenulis": 1,
      "namaPenulis": "Upin (Updated)",
      "email": "upin_new@email.com",
      "createdAt": "2026-10-15T19:00:00",
      "updatedAt": "2026-10-15T19:00:00"
    }
  }
  ```

##### E. Delete Penulis berdasarkan ID
* **Method:** `DELETE`
* **URL:** `http://localhost:5000/api/penulis/1`
* **Response Expected (200 OK):**
  ```json
  {
    "status": "Success",
    "message": "Data penulis berhasil dihapus",
    "data": { ... }
  }
  ```

---

#### 3. Kategori Buku (`/api/kategori`)

##### A. Create Kategori Buku
* **Method:** `POST`
* **URL:** `http://localhost:5000/api/kategori`
* **Body (JSON):**
  ```json
  {
    "namaKategori": "Fiksi Petualangan",
    "deskripsi": "Kumpulan novel cerita petualangan seru dan fantasi"
  }
  ```
* **Response Expected (201 Created):**
  ```json
  {
    "idKategori": 1,
    "namaKategori": "Fiksi Petualangan",
    "deskripsi": "Kumpulan novel cerita petualangan seru dan fantasi",
    "createdAt": "2026-10-15T19:00:00",
    "updatedAt": "2026-10-15T19:00:00"
  }
  ```

##### B. Get Semua Kategori
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/kategori`

##### C. Get Kategori berdasarkan ID
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/kategori/1`

##### D. Update Kategori berdasarkan ID
* **Method:** `PUT`
* **URL:** `http://localhost:5000/api/kategori/1`
* **Body (JSON):**
  ```json
  {
    "namaKategori": "Fiksi Fantasi",
    "deskripsi": "Kumpulan novel bergenre fantasi"
  }
  ```

##### E. Delete Kategori berdasarkan ID
* **Method:** `DELETE`
* **URL:** `http://localhost:5000/api/kategori/1`

---

#### 4. Buku (`/api/buku`)

##### A. Create Buku
* **Method:** `POST`
* **URL:** `http://localhost:5000/api/buku`
* **Body (JSON):**
  ```json
  {
    "judul": "Bumi",
    "isbn": "9786020301128",
    "tahunTerbit": "2014",
    "harga": "85000",
    "idPenulis": 1,
    "idKategori": 1
  }
  ```
* **Response Expected (201 Created):**
  ```json
  {
    "status": "Success",
    "message": "Data buku berhasil ditambahkan",
    "data": {
      "idBuku": 1,
      "judul": "Bumi",
      "isbn": "9786020301128",
      "harga": "85000",
      "idKategori": 1,
      "kategori": {
        "idKategori": 1,
        "namaKategori": "Fiksi Petualangan",
        "deskripsi": "Kumpulan novel cerita petualangan seru dan fantasi",
        "createdAt": "2026-10-15T19:00:00",
        "updatedAt": "2026-10-15T19:00:00"
      },
      "idPenulis": 1,
      "penulis": {
        "idPenulis": 1,
        "namaPenulis": "Upin",
        "email": "upin@email.com",
        "createdAt": "2026-10-15T19:00:00",
        "updatedAt": "2026-10-15T19:00:00"
      },
      "tahunTerbit": "2014",
      "createdAt": "2026-10-15T19:00:00",
      "updatedAt": "2026-10-15T19:00:00"
    }
  }
  ```

##### B. Get Semua Buku
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/buku`

##### C. Get Buku berdasarkan ID
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/buku/1`

##### D. Update Buku berdasarkan ID
* **Method:** `PUT`
* **URL:** `http://localhost:5000/api/buku/1`
* **Body (JSON):**
  ```json
  {
    "judul": "Bumi (Edisi Spesial)",
    "harga": "95000"
  }
  ```

##### E. Filter Buku berdasarkan ID Penulis
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/buku/penulis/1`

##### F. Filter Buku berdasarkan ID Kategori
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/buku/kategori/1`

##### G. Cari Buku berdasarkan Judul
* **Method:** `GET`
* **URL:** `http://localhost:5000/api/buku/judul/Bumi`

---

## 🛠 Troubleshooting Umum

1. **Error: `ModuleNotFoundError: No module named 'flask'`**
   * Pastikan virtual environment `venv_meeting6` sudah diaktifkan sebelum menjalankan `python app.py`.
   * Pastikan telah menjalankan `pip install -r requirements.txt`.

2. **Error: `Can't connect to MySQL server on 'localhost'`**
   * Pastikan service MySQL sudah dijalankan (misalnya Start modul MySQL pada XAMPP).
   * Pastikan database `perpustakaan` sudah dibuat.

3. **PowerShell `cannot be loaded because running scripts is disabled on this system`**
   * Buka PowerShell dan jalankan perintah:
     ```powershell
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     ```
   * Kemudian jalankan kembali skrip aktivasi `.\venv_meeting6\Scripts\Activate.ps1`.
