#!/bin/bash
# setup.sh — Quick setup script for running Flask on Tor

echo "[*] Starting Flask app..."
python3 runner.py &

echo "[*] Setting up Tor hidden service..."
tor -f tor_config.ini
