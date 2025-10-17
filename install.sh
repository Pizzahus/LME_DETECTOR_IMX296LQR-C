#!/bin/bash
set -e  # หยุดการทำงานทันทีถ้ามี error

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
echo "📦 Updating system and installing base packages..."
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y tesseract-ocr
sudo apt install -y python3 python3-venv python3-pip git curl

# --- 3️⃣ ติดตั้งเครื่องมือ build และ dependencies ที่จำเป็น ---
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
    libcap-dev \
    libatlas-base-dev \
    libopenblas-dev \
    libtiff5-dev

# --- 4️⃣ ติดตั้ง libcamera และเครื่องมือที่เกี่ยวข้อง (สำหรับ Raspberry Pi) ---
echo "📷 Installing libcamera utilities..."
sudo apt install -y \
    libcamera-apps \
    python3-picamera2

# --- 5️⃣ สร้าง Virtual Environment ---
echo "🐍 Creating Python virtual environment..."
python3 -m venv --system-site-packages detection_venv

# --- 6️⃣ เปิดใช้งาน Virtual Environment ---
echo "⚙️ Activating virtual environment..."
source detection_venv/bin/activate

# --- 7️⃣ อัปเดต pip และ wheel ---
echo "⬆️ Updating pip and wheel..."
pip install --upgrade pip setuptools wheel

# --- 8️⃣ ติดตั้ง dependencies จาก requirements.txt ---
echo "📚 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install --no-cache-dir -r requirements.txt
else
    echo "⚠️ ไม่พบไฟล์ requirements.txt — จะข้ามขั้นตอนนี้"
fi

# --- 9️⃣ ติดตั้ง simplejpeg แยก (เผื่อมีปัญหาการ build) ---
echo "🧩 Installing simplejpeg (manual build fallback)..."
pip install --no-cache-dir simplejpeg || {
    echo "⚠️ simplejpeg build failed, retrying with source build..."
    pip install --no-binary :all: simplejpeg
}

# --- 🔟 เสร็จสิ้น ---
echo "✅ ติดตั้งสำเร็จทั้งหมด!"
echo "--------------------------------------"
echo "🎯 เปิดใช้งาน environment ได้ด้วย:"
echo "cd LME_DETECTOR_IMX296LQR-C"
echo "source detection_venv/bin/activate"
echo "python3 main.py"
echo "--------------------------------------"
