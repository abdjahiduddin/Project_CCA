# Project_CCA
Project Cloud Computing Kelas - A
Project_CCA merupakan project akhir dari pelatihan DTS FGA Cloud Computing. Sistem yang dibuat pada project ini adalah sistem berbasis IoT.
Sistem ini mendeteksi insensitas sampah dalam jangka waktu tertentu menggunakan sensor ketinggian (Sensor Dummy) kemudian memberikan informasi tersebut ke petugas sampah.
Sistem ini diterapkan di infrastruktur AWS. Services yang digunakan antara lain API Gateway, Lambda dan DynamoDB.
Pada repository ini hanya berisi beberapa source code dari kesuluruhan sistem yang dibangun.
Seluruh file python yang ada pada repository ini dijalankan di service Lambda.

# File api_lambda_dynamo.py
File ini berisi code untuk mengambil data dari service DynamoDB kemudian disajikan dalam bentuk API melalui service API Gateway.

# File iot_lambda_dynamo.py
File ini berisi code untuk menerima data dari service API Gateway kemudian disimpan di database DynamoDB

# File lambda_function.py
File ini berisi code untuk melakukan analisis intensitas sampah dalam jangka waktu tertentu. Hasil analisis akan disimpan di database DynamoDB
