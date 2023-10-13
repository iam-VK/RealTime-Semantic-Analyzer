#!/bin/bash
source venv/bin/activate
echo
echo "<-----Starting Local Servers----->"
echo
echo API server ........ localhost:5000
x-terminal-emulator -e "python3 API.py" &
echo Web app server .... localhost:5050
x-terminal-emulator -e "cd frontend && npm run dev -- --host" &
echo
echo Launching Webpage...
xdg-open http://localhost:5050
echo "-------------------It may take some time to load the servers-------------------"
read a