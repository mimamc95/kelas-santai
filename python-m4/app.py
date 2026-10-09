from flask import Flask, jsonify

#Flask itu Framework, dia bisa membuat sebuah web 
#jsonify untuk membuat respone menjadi json 
app = Flask(__name__) #Setingan Utama dari Flask Itu sendiri 
#Ini devinisi dari flask 
#/daftar, /admin/login
#Devifiin Route nya atau Endpoint nya (URL)
#local tidak dapat di akses oleh orang lain 
# baseUrl = http://localhost:5000/
#kalo sudah pake domain atau IP Public itu bisa akses 
# baseUrl = https://kelas.kelasantai.online/
@app.route("/")
def index():
    return "Hello World" #mengembalikan nilai string biasa 

@app.route("/user/get-user", methods=["GET"])
def getUser():
    #Semua Logika untuk 1 endpoint akan di definisikan di sini 
    data = [{
        "username": "bagja",
        "password": "[PASSWORD]",
        "nama": "Bagja",
        "role": "Admin"
    }, 
    {
        "username": "asep",
        "password": "[PASSWORD]",
        "nama": "Asep",
        "role": "User"
    }]  

    return jsonify({
        "statusCode": 200,
        "massage":"Data Berhasil Di Ambil", 
        "data": data,
    })

# #1 Fungsi 1 Endpoint 
# @app.route("/user/login", methods=["POST"])
# def login():
#     #Semua Logika untuk 1 endpoint akan di definisikan di sini 

#     # nerima data 


#     # ngecek di database ada apa enggak 


#     # ngecek pass nya sama apa enggak 


#     # ngirimin informasi yang berharga yang bisa. keamanan
#     return jsonify({
#         "statusCode": 200,
#         "massage":"Data Berhasil Di Ambil", 
#     })

# @app.route("/user/get-user", methods=["GET"])
# def login():
#     #Semua Logika untuk 1 endpoint akan di definisikan di sini 

#     # nerima data 


#     # ngecek di database ada apa enggak 


#     # ngecek pass nya sama apa enggak 


#     # ngirimin informasi yang berharga yang bisa. keamanan
#     return jsonify({
#         "statusCode": 200,
#         "massage":"Data Berhasil Di Ambil", 
#     })

# @app.route("/user/user-update", methods=["PUT"])
# def userUpdate():
#     #Semua Logika untuk 1 endpoint akan di definisikan di sini 

#     # nerima data 


#     # ngecek di database ada apa enggak 


#     # ngecek pass nya sama apa enggak 


#     # ngirimin informasi yang berharga yang bisa. keamanan
#     return jsonify({
#         "statusCode": 200,
#         "massage":"Data Berhasil Di Ambil", 
#     })

# @app.route("/user/delete-data", methods=["DELETE"])
# def deleteData():
#     #Semua Logika untuk 1 endpoint akan di definisikan di sini 

#     # nerima data 


#     # ngecek di database ada apa enggak 


#     # ngecek pass nya sama apa enggak 


#     # ngirimin informasi yang berharga yang bisa. keamanan
#     return jsonify({
#         "statusCode": 200,
#         "massage":"Data Berhasil Di Ambil", 
#     })


# @app.route("/user/register", methods=["POST"])
# def register():
#     #Semua Logika untuk 1 endpoint akan di definisikan di sini 
#     return jsonify({
#         "statusCode": 200,
#         "massage":"Data Berhasil Di Ambil", 
#     })


# Dynamic Route
@app.route("/user/<username>/login", methods=["POST"])
def login(username):
    return jsonify({
        "statusCode": 200,
        "massage":"Data Berhasil Di Ambil", 
    })


    
#ini untuk runiing framework flask 
if __name__ == '__main__':
    app.run(debug=True) #debug true ini untuk mempermudah kita dalam melihat error saat kita melakukan perubahan 
    
