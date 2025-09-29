#!/bin/bash
cd /home/polipharm/LME_DETECTOR_IMX296LQR-C || exit
source detection_venv/bin/activate
python3 ./main.py
