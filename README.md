# Discord webhook tool

## Overview

This Tool uses discord webhooks to send images from inside a folder to discord webhooks.
It's an easy way to send avatars, banners & what not to a channel for your servers.

## Requirements

- Python 3.x
- Library: `discord_webhook`

## How to Use

1. **Discord Webhook Setup:**
   - Create a Discord webhook URL and replace the placeholder in the `webhook_url` variable.

2. **Prepare Image Folder:**
   - Put the images you want to send in the 'images' folder.

3. **Run the file:**
   - Run the file, and it will send random images to your Discord channel continuously.

## Configuration

- `webhook_url`: Replace with your Discord webhook URL.
- `folder_name`: Name of the folder containing the images.
- `cooldown`: Cooldown time between sending images (default is 60 seconds).

## Important Note

- Supported image formats: `.png`, `.jpg`, `.jpeg`, and `.gif`. Ensure your images have these extensions.

## Example

python discord.py // or just run the file.
