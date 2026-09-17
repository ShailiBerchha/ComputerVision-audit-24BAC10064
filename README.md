<img width="800" height="493" alt="Screenshot 2026-09-17 221225" src="https://github.com/user-attachments/assets/85f0481b-09fe-4abc-8d27-e10ecf8e3a2d" />
# Real-Time Face Detection 

## 📌 Project Overview

This project implements a **real-time face detection system** using **Python and OpenCV**. The system captures live video through a webcam and detects human faces in each video frame.

When a face is detected, a rectangular bounding box is drawn around it. The project demonstrates the basic concepts of **Computer Vision, image processing, object detection, and real-time video processing**.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand the basics of Computer Vision.
* To capture real-time video using a webcam.
* To process video frames using OpenCV.
* To detect human faces automatically.
* To draw bounding boxes around detected faces.
* To understand how Haar Cascade classifiers are used for face detection.
* To implement a simple real-time Computer Vision application.

---

## 🧠 Computer Vision Concepts Used

This project uses the following concepts:

1. **Image Acquisition** – Capturing video from a webcam.
2. **Grayscale Conversion** – Converting color frames into grayscale images.
3. **Face Detection** – Detecting faces using a Haar Cascade classifier.
4. **Bounding Boxes** – Drawing rectangles around detected faces.
5. **Real-Time Processing** – Processing webcam frames continuously.

---

## 🛠️ Technologies Used

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| Python       | Programming language                 |
| OpenCV       | Computer Vision and image processing |
| NumPy        | Numerical and array operations       |
| Haar Cascade | Face detection classifier            |
| VS Code      | Development environment              |
| Git          | Version control                      |
| GitHub       | Project repository                   |

All the software and libraries used in this project are free to use.

---

## 💻 System Requirements

### Hardware

* Laptop or desktop computer
* Webcam
* Minimum 4 GB RAM recommended
* Working USB/internal camera

### Software

* Python 3.x
* OpenCV
* NumPy
* VS Code or any Python-compatible code editor
* Git (for uploading the project to GitHub)

---

## 📂 Project Structure

```text
Face-Detection-OpenCV/
│
├── README.md
├── requirements.txt
├── face_detection.py
├── haarcascade_frontalface_default.xml
├── screenshots/
│   └── output.png
└── demo/
```

---

## ⚙️ Installation

### Step 1: Install Python

Download and install Python 3 from the official Python website.

During installation, make sure to select:

```text
Add Python to PATH
```

### Step 2: Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd Face-Detection-OpenCV
```

### Step 3: Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the libraries directly:

```bash
pip install opencv-python numpy
```

---

## ▶️ How to Run the Project

Run the following command from the project directory:

```bash
python face_detection.py
```

The webcam will open automatically.

The program will:

1. Start the webcam.
2. Capture video frames.
3. Convert each frame into grayscale.
4. Detect faces.
5. Draw rectangles around detected faces.
6. Display the processed video.

To stop the program, press:

```text
Q
```

---

## 🔍 Working Principle

The project uses a **Haar Cascade Classifier** for detecting faces.

The basic process is:

```text
Webcam
   ↓
Capture Frame
   ↓
Convert to Grayscale
   ↓
Haar Cascade Classifier
   ↓
Detect Faces
   ↓
Draw Bounding Rectangle
   ↓
Display Frame
   ↓
Repeat
```

The process continues for every frame until the user presses the `Q` key.

---

## 🧩 Haar Cascade Classifier

A Haar Cascade is a machine-learning-based object detection method that can be used to detect objects such as faces.

In this project, the following classifier is used:

```text
haarcascade_frontalface_default.xml
```

The classifier contains trained information that allows OpenCV to identify patterns associated with human faces.

---

## 📸 Sample Output

When the webcam detects a face, a rectangular box appears around the detected face.

Example:

```text
+--------------------------------------+
|                                      |
|          ┌──────────────┐            |
|          │              │            |
|          │     FACE     │            |
|          │              │            |
|          └──────────────┘            |
|                                      |
|              Webcam                  |
+--------------------------------------+
```

Add your actual screenshot to:

```text
screenshots/output.png
```

Then it can be displayed in this README using:

```markdown
![Face Detection Output](screenshots/output.png)
```

---

## 📊 Algorithm

1. Start the program.
2. Initialize the webcam.
3. Load the Haar Cascade face classifier.
4. Capture a video frame.
5. Convert the frame from BGR to grayscale.
6. Apply the Haar Cascade classifier.
7. Detect the faces present in the frame.
8. Draw a rectangle around every detected face.
9. Display the processed frame.
10. Repeat until the user presses `Q`.
11. Release the webcam.
12. Close all OpenCV windows.
13. End the program.

---

## 🌟 Features

* Real-time face detection
* Webcam-based operation
* Multiple face detection
* Bounding boxes around detected faces
* Simple and easy-to-understand implementation
* No custom dataset required
* No model training required
* Lightweight application

---

## ⚠️ Limitations

* Detection accuracy can decrease in poor lighting.
* Faces turned significantly away from the camera may not be detected.
* Very small faces may be difficult to detect.
* Haar Cascade detection can produce false positives in some situations.
* The system is designed for face detection, not face recognition.

---

## 🔮 Future Scope

The project can be extended by adding:

* Face recognition
* Face counting
* Face blurring for privacy
* Attendance management
* Emotion detection
* Age and gender estimation
* Mask detection
* Multiple camera support
* Deep-learning-based face detection

---

## 🎓 Learning Outcomes

After completing this project, we can understand:

* How OpenCV works with video.
* How webcam frames are captured.
* How images are converted to grayscale.
* How Haar Cascade classifiers perform face detection.
* How bounding boxes are generated.
* How real-time Computer Vision applications are developed.
* How a Computer Vision project can be maintained using Git and GitHub.

---

## 📜 Conclusion

The **Real-Time Face Detection Using Python and OpenCV** project demonstrates a simple and practical application of Computer Vision.

By using a webcam and a Haar Cascade classifier, the system can detect human faces in real time and highlight them using bounding boxes.

The project provides a basic foundation for developing more advanced Computer Vision applications such as face recognition, attendance systems, and privacy-preserving face anonymization.

---


