#!/bin/bash
set -e  # หยุดการทำงานทันทีถ้ามี error

USER_HOME="/home/$USER"
PROJECT_DIR="$USER_HOME/LME_DETECTOR_IMX296LQR-C"
TESSERACT_MODEL_SRC="$PROJECT_DIR/tesseract_model"
TESSERACT_MODEL_DST="/usr/share/tesseract-ocr/5/tessdata"
DESKTOP_FILE_SRC="$PROJECT_DIR/sys/LME_Detector.desktop"
DESKTOP_DIR="$USER_HOME/Desktop"
AUTOSTART_DIR="$USER_HOME/.config/autostart"

GITHUB_EMAIL="pizzahus5678@gmail.com"
GITHUB_USERNAME="Pizzahus"

echo "======================================"
echo "🚀 เริ่มติดตั้งระบบสำหรับ LME_DETECTOR_IMX296LQR-C"
echo "======================================"

# --- 1️⃣ ตรวจสอบพื้นที่ใน SD card ---
echo "🔍 Checking available disk space..."
df -h /
FREE_SPACE=$(df --output=avail / | tail -n 1)
if [ "$FREE_SPACE" -lt 500000 ]; then
    echo "❌ พื้นที่ไม่เพียงพอ (ต้องมีอย่างน้อย 500MB)"
    exit 1
else
    echo "✅ พื้นที่เพียงพอ"
fi

# --- 2️⃣ อัปเดตและติดตั้งเครื่องมือพื้นฐาน ---
git config --global user.email "$GITHUB_EMAIL"
git config --global user.name "$GITHUB_USERNAME"
git config --list

echo "📦 Updating system and installing base packages..."
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y tesseract-ocr
sudo apt install -y python3 python3-venv python3-pip git curl

# --- 3️⃣ คัดลอกโมเดล Tesseract ---
echo "🧠 Copying custom Tesseract models..."
if [ -d "$TESSERACT_MODEL_SRC" ]; then
    sudo mkdir -p "$TESSERACT_MODEL_DST"
    sudo cp -v "$TESSERACT_MODEL_SRC"/* "$TESSERACT_MODEL_DST"/
    echo "✅ คัดลอกโมเดล Tesseract สำเร็จ"
else
    echo "⚠️ ไม่พบโฟลเดอร์ $TESSERACT_MODEL_SRC — ข้ามขั้นตอนนี้"
fi

# --- 4️⃣ ติดตั้งเครื่องมือ build และ dependencies ที่จำเป็น ---
echo "🔧 Installing build tools and dependencies..."
sudo apt install -y \
    build-essential \
    cmake \
    ninja-build \
    autoconf \
    automake \
    libtool \
    pkg-config \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    libcamera-dev \
    libcap-dev
    # libatlas-base-dev \
    # libopenblas-dev \
    # libtiff5-dev

# --- 5️⃣ ติดตั้ง libcamera และเครื่องมือที่เกี่ยวข้อง (สำหรับ Raspberry Pi) ---
echo "📷 Installing libcamera utilities..."
sudo apt install -y \
    libcamera-apps \
    python3-picamera2

# --- 6️⃣ สร้าง Virtual Environment ---
echo "🐍 Creating Python virtual environment..."
python3 -m venv --system-site-packages "$PROJECT_DIR/detection_venv"

# --- 7️⃣ เปิดใช้งาน Virtual Environment ---
echo "⚙️ Activating virtual environment..."
source "$PROJECT_DIR/detection_venv/bin/activate"

# --- 8️⃣ อัปเดต pip และ wheel ---
echo "⬆️ Updating pip and wheel..."
pip install --upgrade pip setuptools wheel

# --- 9️⃣ ติดตั้ง dependencies จาก requirements.txt ---
echo "📚 Installing Python dependencies..."
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    pip install --no-cache-dir -r "$PROJECT_DIR/requirements.txt"
else
    echo "⚠️ ไม่พบไฟล์ requirements.txt — จะข้ามขั้นตอนนี้"
fi

# --- 🔟 ติดตั้ง simplejpeg แยก (เผื่อมีปัญหาการ build) ---
echo "🧩 Installing simplejpeg (manual build fallback)..."
pip install --no-cache-dir simplejpeg || {
    echo "⚠️ simplejpeg build failed, retrying with source build..."
    pip install --no-binary :all: simplejpeg
}

# --- 11️⃣ คัดลอก Desktop Shortcut และตั้งค่า Autostart ---
echo "🖥️ Setting up Desktop shortcut and autostart..."
mkdir -p "$DESKTOP_DIR" "$AUTOSTART_DIR"
if [ -f "$DESKTOP_FILE_SRC" ]; then
    cp -v "$DESKTOP_FILE_SRC" "$DESKTOP_DIR/"
    chmod +x "$DESKTOP_DIR/LME_Detector.desktop"
    cp -v "$DESKTOP_FILE_SRC" "$AUTOSTART_DIR/"
    chmod +x "$AUTOSTART_DIR/LME_Detector.desktop"
    echo "✅ สร้าง Desktop shortcut และ autostart สำเร็จ"
else
    echo "⚠️ ไม่พบไฟล์ $DESKTOP_FILE_SRC — ข้ามขั้นตอนนี้"
fi

# --- ✅ เสร็จสิ้น ---
echo "✅ ติดตั้งสำเร็จทั้งหมด!"
echo "--------------------------------------"
echo "🎯 เปิดใช้งาน environment ได้ด้วย:"
echo "cd $PROJECT_DIR"
echo "source detection_venv/bin/activate"
echo "python3 main.py"
echo "--------------------------------------"
