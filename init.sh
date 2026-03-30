#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
set -e

echo "Installing Java 21 (Amazon Corretto)..."

sudo apt-get update -y
sudo apt-get install -y ca-certificates apt-transport-https gnupg wget

wget -q -O - https://apt.corretto.aws/corretto.key | \
  sudo gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | \
  sudo tee /etc/apt/sources.list.d/corretto.list

sudo apt-get update -y
sudo apt-get install -y java-21-amazon-corretto-jdk libxi6 libxtst6 libxrender1

echo "Java installed: $(java -version 2>&1 | head -1)"


echo "Installing Python 3 + pip..."

sudo apt-get install -y python3 python3-pip

echo "Python installed: $(python3 --version)"
echo "pip installed: $(pip3 --version)"

echo "Installing Flask + dependencies..."

pip3 install flask flask-cors requests mcrcon --break-system-packages --ignore-installed blinker

echo "Flask installed"

echo "Downloading Minecraft Server (PaperMC 1.21.1)..."

source "$SCRIPT_DIR/config.conf"

mkdir -p minecraft
cd minecraft



PAPER_URL="https://fill.papermc.io/v3/projects/paper/versions/${PAPER_VERSION}/builds/${PAPER_BUILD}"
echo "Calling parser with: $PAPER_URL"
DOWNLOAD_URL=$(python3 "$SCRIPT_DIR/paper-request-parser.py" "$PAPER_URL")
echo "Download URL: $DOWNLOAD_URL"

wget -q --show-progress -O server.jar "$DOWNLOAD_URL"

# Accept the EULA automatically
echo "eula=true" > eula.txt

echo "PaperMC downloaded as server.jar"
echo "EULA accepted"

cd ..

echo "Setup systemd service for Minecraft server..."

SERVICE_FILE="/etc/systemd/system/minecraft.service"
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Minecraft Server
After=network.target

[Service]
WorkingDirectory=$SCRIPT_DIR/minecraft
ExecStart=/usr/bin/java -Xmx3G -Xms3G -jar $SCRIPT_DIR/minecraft/server.jar nogui
Restart=always

[Install]
WantedBy=multi-user.target
EOL
sudo systemctl daemon-reload
sudo systemctl enable minecraft.service
echo "Minecraft service created and enabled"

echo "Initialization complete. You can start the server with: sudo systemctl start minecraft.service"