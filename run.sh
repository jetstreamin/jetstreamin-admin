#!/bin/bash
python3 jet_backend.py &> ~/jetstreamin/logs/backend.log &
http-server ./ide -p 3000 -a 0.0.0.0 &> ~/jetstreamin/logs/frontend.log &
wait
