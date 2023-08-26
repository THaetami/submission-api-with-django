1. download repository

```sh
git clone https://github.com/THaetami/submission-api-with-django.git
```

2. buat virtual environment

```sh
python -m venv myenv
```

3. aktifkan virtual environment

```sh
myenv\Scripts\activate
```

4. pindah folder

```sh
cd server
```

5. install pip

```sh
python.exe -m pip install --upgrade pip
```

6. install semua dependensi project

```sh
pip install -r requirements.txt
```

7. edit database credential [disini](https://github.com/THaetami/submission-api-with-django/blob/master/server/server/settings.py)

8. jalankan project dan lihat overview api [disini](http://127.0.0.1:8000/)

```sh
python manage.py runserver
```
