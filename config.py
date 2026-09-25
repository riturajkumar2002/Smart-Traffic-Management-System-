"""
Configuration module for Smart Traffic Management System.
Supports environment variables with sensible local defaults.
"""

import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent

# YOLO Model Configuration
MODEL_PATH = os.getenv("YOLO_MODEL_PATH", str(BASE_DIR / "yolov8n.pt"))
CONFIDENCE_THRESHOLD = float(os.getenv("CONF_THRESHOLD", "0.3"))
MAX_TRACK_AGE = int(os.getenv("MAX_TRACK_AGE", "30"))
SMOOTHING_WINDOW = int(os.getenv("SMOOTHING_WINDOW", "10"))

# Video Input Source (can be a local file path, RTSP stream URL, or webcam index)
VIDEO_SOURCE = os.getenv("VIDEO_SOURCE", str(BASE_DIR / "video" / "traffic.mp4"))

# Database Configuration (MySQL)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "newpassword123")
DB_NAME = os.getenv("DB_NAME", "traffic_management")
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "5"))

# Flask Application Settings
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")

# Upload Configuration
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", str(BASE_DIR / "uploads"))
