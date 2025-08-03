#!/bin/bash
mkdir -p ~/jetstreamin/{config,logs,promptbooks}
cp -n ./defaults/.jetconfig.json ~/jetstreamin/config/.jetconfig.json
pip install flask flask_cors
npm install -g http-server
echo "[NETA] Jetstreamin IDE ready."
