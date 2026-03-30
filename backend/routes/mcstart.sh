#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting Minecraft server..."
sudo systemctl start minecraft.service
echo "Minecraft server started"