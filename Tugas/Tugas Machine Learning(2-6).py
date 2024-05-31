{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f54ffcd3-02fa-48d3-8205-2abd11fa7a60",
   "metadata": {},
   "source": [
    "TUGAS MACHINE LEARNING"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9d0ff63-82ab-4bde-a66f-ea438e2452a8",
   "metadata": {},
   "source": [
    "SOAL 1 Buatlah identitas diri menggunakan pemograman python sederhana"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e55dc4cb-ad1a-4132-ab3a-3a901b1258bf",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DATA DIRI\n",
      "Nama :  Zaidan Jainul Insan\n",
      "NIM :  20230801421\n",
      "Program Studi :  Teknik Informatika\n",
      "Fakultas : Ilmu Komputer\n"
     ]
    }
   ],
   "source": [
    "nama = \"Zaidan Jainul Insan\"\n",
    "nomor_induk_mahasiswa = \"20230801421\"\n",
    "program_studi = \"Teknik Informatika\"\n",
    "fakultas = \"Ilmu Komputer\"\n",
    "\n",
    "print(\"DATA DIRI\")\n",
    "print(\"Nama : \", nama)\n",
    "print(\"NIM : \", nomor_induk_mahasiswa)\n",
    "print(\"Program Studi : \", program_studi)\n",
    "print(\"Fakultas :\", fakultas)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7373346-75c8-4769-ab69-ce6c5ec79edd",
   "metadata": {},
   "source": [
    "SOAL 2 Buatlah matriks C dengan orde 2x3, dan nilai yang diberikan pada matriks C adalah sebagai berikut :"
   ]
  },
  {
   "cell_type": "raw",
   "id": "19d47da5-3cd4-4a0c-a98b-92cfc1efa884",
   "metadata": {},
   "source": [
    "Baris 1 Kolom 1, nilai = 1\n",
    "Baris 1 Kolom 2, nilai = 2\n",
    "Baris 1 Kolom 3, nilai = 3\n",
    "Baris 2 Kolom 1, nilai = 4\n",
    "Baris 2 Kolom 2, nilai = 5\n",
    "Baris 2 Kolom 3, nilai = 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5f2fe209-1120-4072-abbb-672a541fd362",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 2, 3], [4, 5, 6]]\n"
     ]
    }
   ],
   "source": [
    "matriksC= [[1,2,3],[4,5,6]]\n",
    "print(matriksC)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5e87a5c-00c3-4894-8bb6-78ee46698ed8",
   "metadata": {},
   "source": [
    "SOAL 3 Buatlah matriks dengan orde 3x2, dengan nilai adalah :"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b157ce5-97e7-4125-bb2d-e8e3db82a9d0",
   "metadata": {},
   "source": [
    "Baris 1 Kolom 1, nilai = 2\n",
    "Baris 1 Kolom 2, nilai = 2\n",
    "Baris 2 Kolom 1, nilai = 2\n",
    "Baris 2 Kolom 2, nilai = 2\n",
    "Baris 3 Kolom 1, nilai = 2\n",
    "Baris 3 Kolom 2, nilai = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d95b8f71-24b6-447b-8590-f3bc52028644",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2, 2], [2, 2], [2, 2]]\n"
     ]
    }
   ],
   "source": [
    "matriks = [[2,2],[2,2],[2,2]]\n",
    "print(matriks)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b507d0f-a49d-4236-83ed-f1a0689fa3a9",
   "metadata": {},
   "source": [
    "SOAL 4 Importlah library Numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "537cceb0-4ac1-42d1-96e3-bc58649ba928",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6308250d-1888-46d3-83e5-1095340d46b1",
   "metadata": {},
   "source": [
    "SOAL 5 Dengan memanfaatkan library numpy Buatlah matriks dengan menggunakan Library Numpy dengan panjang elemen adalah 32 dan matriks memiliki orde 4x8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dd5ca2f7-0bdc-4707-b35e-c6dc9f5883cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4  5  6  7]\n",
      " [ 8  9 10 11 12 13 14 15]\n",
      " [16 17 18 19 20 21 22 23]\n",
      " [24 25 26 27 28 29 30 31]]\n"
     ]
    }
   ],
   "source": [
    "from numpy import *\n",
    "matriks = range(32)\n",
    "matriks = reshape(matriks, (4,8))\n",
    "print(matriks)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9e18626-d040-43c3-acca-d7a375df12c8",
   "metadata": {},
   "source": [
    "SOAL 6 Buatlah matriks dengan menggunakan Library Numpy dengan orde 3x30, dan nilai elemen dimulai dari indeks 1 sampai dengan 5 secara random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "df135b37-ce51-47d7-b861-9e6f1131a33b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3 2 1 4 4 1 4 4 4 3 2 1 4 4 1 4 4 3 1 2 1 3 3 1 2 4 4 2 3 4]\n",
      " [4 1 4 1 2 2 2 4 3 3 4 2 3 2 1 4 4 1 1 4 4 4 4 4 2 1 1 4 4 3]\n",
      " [4 4 2 1 3 2 3 3 3 2 3 4 3 3 1 4 2 2 3 2 3 1 1 4 3 2 1 2 1 2]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from numpy import *\n",
    "\n",
    "matriks = np.random.randint(1,5,(3,30))\n",
    "print(matriks)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
