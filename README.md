
---

# 🧠 Exam Grader

A modular Python-based MCQ exam grading system designed to **automate the marking of student answer sheets** without the need for expensive OCR scanners or specialized OMR papers.

This tool reads **scanned or text-based exam submissions**, compares them to an uploaded **answer key**, generates **marked scripts**, displays results neatly in a **table**, and exports them to **CSV** for easy analysis or upload to school portals.

---

## 🚀 Vision

Traditional grading systems often depend on **costly OCR hardware** and pre-printed OMR sheets.
**Exam Grader** eliminates this dependency by using **AI handwriting recognition (TensorFlow)** to interpret students’ handwritten responses directly from scanned A4 sheets.

Students can simply write their answers on standard paper, examiners scan them with **phones or multifunction printers**, and the system:

* Extracts student details and answers automatically.
* Grades them against the provided answer key.
* Generates marked scripts with correct answers for failed questions.
* Produces a full CSV report of all results for easy upload and sharing.

This approach **reduces cost**, **improves accessibility**, and **simplifies large-scale grading**—making digital assessment available to every institution.

---

## 🧩 Features

✅ Grade unlimited questions automatically
✅ Compare each student’s answer to the official key
✅ Generate corrected answer scripts for feedback
✅ Display summarized results in a clean table
✅ Export results as a `.csv` file
✅ Modular structure for easy updates and extensions
✅ Future-ready for **AI handwriting recognition** with TensorFlow integration

---

## 📁 Project Structure

```
exam-grader/
│
├── main.py               # Entry point - orchestrates the process
├── file_selector.py      # Handles student file selection
├── answer_sheet.py       # Loads and parses the answer key
├── file_processor.py     # Grades and generates marked scripts
├── csv_handler.py        # Exports final results
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

---

## 🧪 Usage

1. Place student answer `.txt` files in a folder.
   Each file should follow this format:

   ```
   Name: John Doe
   Matricule: SWE90ITY
   1) A
   2) C
   3) B
   ...
   ```

2. Prepare an **answer sheet** `.txt` file in this format:

   ```
   Answers.
   1) A
   2) B
   3) C
   ...
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

4. Follow the prompts to:

   * Select the folder containing student submissions.
   * Choose the answer sheet file.
   * View your grading report and export the results.

---

## ⚙️ Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/Ivelandry1010/smart_mark.git
pip install -r requirements.txt
cd exam-grader
```

Then simply run:

```bash
python main.py
```

---

## 🧠 Future Enhancements

* 📝 **AI Handwriting Recognition** using TensorFlow or OpenCV to extract answers from scanned handwritten sheets.
* 📷 **Camera/Phone Integration** for direct image upload and auto-processing.
* 🌐 **Web-based dashboard** for result management and sharing.
* 💬 **Multi-language support** for international schools.

---

## 🤝 Contributing

Contributions are welcome!
If you’d like to improve **Exam Grader**, add AI capabilities, or integrate with new grading formats:

1. Fork this repository
2. Create your feature branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch

   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request 🎉

---

## 📬 Collaboration & Contact

I’m always open to collaborations, feedback, or partnerships to take this system further — especially in the area of **AI-powered education technology**.

* **Email:**  [sicoidentifcation@gmail.com](mailto:sicoidentifcation@gmail.com)
* **Portfolio:** [loading](#)
* **GitHub:** [@ivelandry1010](https://github.com/Ivelandry1010)
* **WhatsApp:** [+237 686381866](https://wa.me/237686381866?text=Hello%20I%20found%20you%20through%20your%20portfolio)
* **Instagram:** [@sico_lm10](https://www.instagram.com/sico_lm10?igsh=cHdqYmp5enZwYjBy&utm_source=qr)


---

## 📜 License

This project is released under the **MIT License** — feel free to use, modify, and distribute it with attribution.

---

### ✨ *“Empowering accessible education through intelligent grading systems.”*

---


