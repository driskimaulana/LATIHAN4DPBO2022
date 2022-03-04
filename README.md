# LATIHAN4DPBO2022

> Saya D'Riski Maulana 2008149 mengerjakan tugas LATIHAN4 dalam mata kuliah Desain dan Pemrograman Berbasis Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

### Petunjuk Eksekusi Program

**Python**
- Masuk ke directory project dalam CMD
- Eksekusi perintah berikut:
```
py [name].py
```

#### DESAIN & PENJELASAN

![alt text](https://github.com/driskimaulana/LATIHAN4DPBO2022/blob/main/UML_TP4.png)


> Dalam latihan ini, berikut perubahan beserta alasan dari pembuatan desain di atas
> - Desain dari kelas Vehicle, Ship, dan Airplane merupakan **Hierarchical Inheritance** dengan Vehicle sebagai *parent* dan Ship, Airplane menjadi *Child*. Alasan digunakannya desain ini adalah karena penulis memandang bahwa Ship dan Airplane merupakan object yang sama dengan Vehicle, keduanya merupakan jenis dari Vehicle, sehingga cocok digunakan hierarchical inheritance
> - Pemindahan attribut 'age' dan 'type' dari kelas Ship dan Airplane ke kelas Vehicle. Pemindahan ini didasari karena dilihat bahwa kelas Ship dan Airplane merupakan sama-sama child dari kelas Vehicle, dan atribute 'age' serta 'type' itu ada di masing-masing kelas, jadi saya mendesain age type itu naik ke parent class, sehingga kedua kelas child (ship dan airplane) cukup menggunakan derived attribute dari Vehicle class.
> - Penambahan attribute untuk kelas Ship (Length, Beam, CurrentPosition) dan Airplane(WingsLength -> WingsSpan, WingType, bodyType, Engine model). Penambahan ini merupakan akibat dari design pertama, yaitu dipindahkannya atribut age dan type sehingga kelas Ship dan Airplane masing-masing hanya mempunyai satu atribut, dan kelas dengan satu atribut itu tidak baik. Sehingga, saya memutuskan untuk menambah atribut untuk kedua kelas tersebut. Penambahan atribut untuk kedua kelas tersebut juga membuat kelas menjadi lebih lengkap
> - Kelas Job dan Driver memiliki hubungan **Hierarchical Inheritance**. Penulis memandang bahwa Driver merupakan salah satu jenis Job, sehingga merupakan objek yang sama. Oleh karena itu penulis membuat Driver sebagai child dari Job class.
> - Kelas Person, berdiri sendiri. Artinya di sini saya merasa bahwa kelas Person ini merupakan satu kelas yang objek nyatanya berbeda dengan kelas lain, sehingga tidak digunakan inheritance untuk kelas ini. Tetapi, saya memandang bahwa akan menjadi lebih baik jika kelas Person ini memiliki atribut Driver, artinya kelas Person meng-*composite* kelas Driver sebagai penanda bahwa person itu memiliki pekerjaan sebagai driver. 


**Results**

#### Ships Class (Vehicle) <br> <br>

![alt text](https://github.com/driskimaulana/LATIHAN4DPBO2022/blob/main/Screenshots/Ships_Class.png)

#### Airplane Class (Vehicle) <br> <br>

![alt text](https://github.com/driskimaulana/LATIHAN4DPBO2022/blob/main/Screenshots/Airplane_Class.png)

#### Person Class <- Driver(Job) <br> <br>

![alt text](https://github.com/driskimaulana/LATIHAN4DPBO2022/blob/main/Screenshots/Person_Class.png)



## Terima Kasih




