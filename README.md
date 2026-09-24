# Smart Traffic Management System 🚦📊

An AI-powered traffic monitoring and analytics system built using **YOLOv8**, **OpenCV**, and **Flask**. This project detects and classifies vehicles in real-time, calculates traffic density, and displays a live dashboard with actionable insights for smarter traffic control.

---

## 🔧 Features

- 🚗 Vehicle detection and classification (e.g., cars, trucks, buses, motorbikes)
- 📈 Real-time traffic density and vehicle count tracking
- 🎨 Color-coded visualizations per vehicle type
- 🧠 YOLOv8 integration for object detection
- 🌐 Flask web dashboard for monitoring
- 🔁 Video stream processing with DeepSORT object tracking
- ✅ Non-redundant counting logic to avoid double counts

---

## 📦 Technologies Used

- Python 3.x
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- Flask
- DeepSORT
- NumPy
- MySQL Connector

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/riturajkumar2002/Smart-Traffic-Management-System-.git
cd Smart-Traffic-Management-System-
```

### 2. Set Up a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python traffic_detection.py
```
Then open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📂 Project Structure
```text
├── traffic_detection.py          # Main Flask & detection script
├── coco.names                    # COCO dataset class labels
├── datasets/                     # Dataset configurations
├── static/                       # Styling, scripts, and image assets
├── templates/
│   └── index.html                # Flask dashboard UI
├── video/                        # Sample traffic video files
├── requirements.txt              # Python dependencies
├── yolov8n.pt                    # YOLOv8 nano pre-trained weights
└── README.md                     # Project documentation
```

---

## 🧠 Future Enhancements

- Live camera feed support (e.g., IP/RTSP)
- Historical traffic data logging and analytics
- Interactive charts (traffic patterns over time)
- Integration with traffic lights and automated signal control systems

---

## 👤 Author

**Rituraj Kumar**
- GitHub: [@riturajkumar2002](https://github.com/riturajkumar2002)
- Email: [riturajkumar9827@gmail.com](mailto:riturajkumar9827@gmail.com)

---

## 📘 License

This project is open-source and free to use under the MIT License.
