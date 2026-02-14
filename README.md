# ⚽ Σύστημα Διαχείρισης Καταστήματος Ποδοσφαίρου

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://football-shop-site.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-2D9F2D?style=for-the-badge)](https://opensource.org/licenses/MIT)

Η εφαρμογή **ΚΑΤΑΣΤΗΜΑ ΠΟΔΟΣΦΑΙΡΟΥ** είναι ένα ολοκληρωμένο σύστημα διαχείρισης βάσης δεδομένων που δημιουργήθηκε στο πλαίσιο του μαθήματος «Βάσεις Δεδομένων Ι». Επιτρέπει την πλήρη εποπτεία ενός καταστήματος αθλητικών ειδών, προσφέροντας λειτουργίες για:

* **Διαχείριση Πελατών & Προϊόντων**: Προβολή, προσθήκη και διαγραφή εγγραφών.
* **Σύστημα Παραγγελιών**: Δημιουργία νέων παραγγελιών μέσω δυναμικού καλαθιού αγορών.
* **Στατικά SQL Reports**: Εκτέλεση 7 προκαθορισμένων ερωτημάτων για την άντληση συγκεκριμένων πληροφοριών από τη βάση.

Η εφαρμογή χρησιμοποιεί τη βιβλιοθήκη **SQLite** για την τοπική αποθήκευση και διαχείριση των δεδομένων σε αρχείο `.db`.

### [🌐 Η εφαρμογή online στο Streamlit](https://football-shop-site.streamlit.app/)

---

## 💻 Οδηγίες Εκτέλεσης Τοπικά

### 🔧 Απαιτήσεις

- [Python 3.8 ή νεότερη](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)
  

> [!IMPORTANT]
> Για τη σωστή λειτουργία της εφαρμογής, τα αρχεία `create.py` και `insert.py` πρέπει να βρίσκονται στον ίδιο κατάλογο με το κύριο αρχείο (`app.py`), καθώς είναι υπεύθυνα για τη δημιουργία και την αρχικοποίηση της βάσης δεδομένων.

Για να εκτελέσετε την εφαρμογή στον υπολογιστή σας τοπικά:

### 1. Κλωνοποίηση του Repository

```bash
git clone https://github.com/georgekrds/football-shop
cd football-shop
```

### 2. Εγκατάσταση των Απαραίτητων Βιβλιοθηκών

```bash
pip install -r requirements.txt
```

### 3. Εκκίνηση της Εφαρμογής

```bash
streamlit run app.py
```

> [!NOTE]
> Η εφαρμογή θα ανοίξει αυτόματα στον προεπιλεγμένο browser στη διεύθυνση: `http://localhost:8501`

---

## 👥 Η ομάδα 99

### Φοιτητές Τμήματος Πληροφορικής του Ιονίου Πανεπιστημίου

* **Βαν Σλότεν Σταυρούλα** (inf2024025)
* **Καρύδης Γεώργιος Εδουάρδος** (inf2024072)
* **Τζώρτζη Όλγα** (inf2024167)
* **Τζώρτζης Κωνσταντίνος** (inf2024168)

**Μάθημα:** Βάσεις Δεδομένων Ι 

**Διδάσκοντες:** Άνια Σωτηροπούλου, Ανδρέας Καναβός 

---

## 📄 Άδεια Χρήσης

Αυτό το έργο διανέμεται υπό την [MIT License](https://opensource.org/licenses/MIT).
