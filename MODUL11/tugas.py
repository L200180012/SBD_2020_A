#Nomor 1a
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
tambah_transaksi = ("INSERT INTO transaksi(id_nasabahFK, no_rekeningFK, jenis_transaksi, tanggal, jumlah) VALUES(%s,%s,%s,%s,%s)")
data_transaksi = ('16','122','dedit','2019-09-09','100000')
cursor.execute(tambah_transaksi, data_transaksi)

cnx.commit()
cursor.close()
cnx.close()

#Nomor 1b
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
update_transaksi=("UPDATE transaksi SET jumlah=100000 WHERE no_transaksi=52")
cursor.execute(update_transaksi)

cnx.commit()
print(cursor.rowcount,'record(s) affected')
cursor.close()
cnx.close()

#Nomor 1c
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
delete_transaksi=("DELETE FROM transaksi WHERE no_transaksi=50")
cursor.execute(delete_transaksi)

cnx.commit()
print(cursor.rowcount, 'record(s) deleted')
cursor.close()
cnx.close()


#Nomor 2a
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
query = ("SELECT * FROM nasabah")
cursor.execute(query)
for (id_nasabah,nama_nasabah,alamat_nasabah) in cursor:
    print ("ID nasabah: {}. Nama: {}. Alamat: {}.".format(id_nasabah,nama_nasabah,alamat_nasabah))
cursor.close()
cnx.close()

#Nomor 2b
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
query = ("""SELECT * FROM nasabah
         WHERE nasabah.id_nasabah IN (SELECT transaksi.id_nasabahFK
         FROM transaksi WHERE transaksi.tanggal BETWEEN '2009-11-1' AND '2009-12-31')""")
cursor.execute(query)
for (id_nasabah,nama_nasabah,alamat_nasabah) in cursor:
    print ("ID nasabah: {}. Nama: {}. Alamat: {}.".format(id_nasabah,nama_nasabah,alamat_nasabah))
cursor.close()
cnx.close()
