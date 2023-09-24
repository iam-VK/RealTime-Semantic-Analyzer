#!/bin/bash
python3 -m venv venv
source venv/bin/activate
install ./setup_dependencies/git-lfs-3.4.0/install.sh
git clone https://huggingface.co/SamLowe/roberta-base-go_emotions