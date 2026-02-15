# ⚽ Σύστημα Διαχείρισης Καταστήματος Ποδοσφαίρου

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://football-shop-site.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://custom-icon-badges.demolab.com/badge/License-MIT-2D9F2D.svg?logo=law&logoColor=white)](https://opensource.org/licenses/MIT)

Η εφαρμογή **Κατάστημα Ποδοσφαίρου** είναι ένα σύστημα διαχείρισης της βάσης δεδομένων που δημιουργήθηκε για την εργασία εξαμήνου του μαθήματος «Βάσεις Δεδομένων Ι». Επιτρέπει την πλήρη εποπτεία ενός καταστήματος αθλητικών ειδών, προσφέροντας λειτουργίες για:

* **Διαχείριση Πελατών & Προϊόντων**: Προβολή, προσθήκη και διαγραφή εγγραφών.
* **Σύστημα Παραγγελιών**: Δημιουργία νέων παραγγελιών μέσω δυναμικού καλαθιού αγορών.
* **Στατικά SQL Reports**: Εκτέλεση 7 προκαθορισμένων ερωτημάτων για την άντληση συγκεκριμένων πληροφοριών από τη βάση.

Η εφαρμογή δημιουργεί και χρησιμοποιεί τη βάση δεδομένων **SQLite** για την τοπική αποθήκευση και διαχείριση των δεδομένων στο αρχείο `sport_store.db`.

### [🌐 Η εφαρμογή online στο Streamlit](https://football-shop-site.streamlit.app/)

---

## 💻 Οδηγίες Εκτέλεσης Τοπικά

### 🔧 Απαιτήσεις

- [Python 3.8 ή νεότερη](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
  

> [!IMPORTANT]
> Για τη σωστή λειτουργία της εφαρμογής, τα αρχεία `create.py` και `insert.py` πρέπει να βρίσκονται στον ίδιο κατάλογο με το κύριο αρχείο `app.py`, καθώς είναι υπεύθυνα για τη δημιουργία και την αρχικοποίηση της βάσης δεδομένων `sport_store.db`.

Για να εκτελέσετε την εφαρμογή στον υπολογιστή σας τοπικά:

### 1. Κλωνοποίηση του Αποθετηρίου

Αν έχετε εγκατεστημένο το [Git](https://git-scm.com/downloads), μπορείτε να κατεβάσετε το αποθετήριο με:

```bash
git clone https://github.com/georgekrds/football-shop
cd football-shop
```

Αν δεν έχετε Git, μπορείτε να κατεβάσετε το αποθετήριο σε μορφή ZIP και να κάνετε αποσυμπίεση: [Λήψη](https://github.com/georgekrds/football-shop/archive/refs/heads/main.zip)

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
