from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mahasiswa.sqlite'  # Database SQLite

db = SQLAlchemy(app)

# Membuat model Mahasiswa
class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    umur = db.Column(db.Integer)
    alamat = db.Column(db.String(200))

# Buat tabel dalam database
db.create_all()

@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    if request.method == 'GET':
        # Mengambil semua data mahasiswa
        mahasiswas = Mahasiswa.query.all()
        data = [{'id': m.id, 'nama': m.nama, 'umur': m.umur, 'alamat': m.alamat} for m in mahasiswas]
        return jsonify(data)

    if request.method == 'POST':
        # Menambahkan data mahasiswa baru
        data = request.get_json()
        mahasiswa_baru = Mahasiswa(nama=data['nama'], umur=data['umur'], alamat=data['alamat'])
        db.session.add(mahasiswa_baru)
        db.session.commit()
        return jsonify({'message': 'Data mahasiswa telah ditambahkan.'})


@app.route('/mahasiswa/<int:id>', methods=['PUT', 'DELETE'])
def update_delete_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get(id)

    if not mahasiswa:
        return jsonify({'message': 'Mahasiswa tidak ditemukan'}), 404

        mahasiswa.nama = data.get('nama', mahasiswa.nama)
        mahasiswa.umur = data.get('umur', mahasiswa.umur)
        mahasiswa.alamat = data.get('alamat', mahasiswa.alamat)
        db.session.commit()
        return jsonify({'message': 'Data mahasiswa telah diperbarui.'})

    if request.method == 'DELETE':
        db.session.delete(mahasiswa)
        db.session.commit()
        return jsonify({'message': 'Data mahasiswa telah dihapus.'})


if __name__ == '__main__':
    app.run(debug=True)
