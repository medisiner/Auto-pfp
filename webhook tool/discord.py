import os
import random
import time
import colorama
from discord_webhook import DiscordWebhook, DiscordEmbed

def send_embed(webhook_url, folder_name, cooldown=None):
    if cooldown is None:
        cooldown = 60 # Going back to line 65 -> if its left as "None" it'll use this.

    try:
        if not webhook_url:
            print("Webhook URL is not provided. Please set a valid webhook URL.")
            return

        colorama.init()

        print("\033[38;2;177;159;249mMaking sure everything is set up fine on your end\033[0m")

        while True:
            current_directory = os.getcwd()
            folder_path = os.path.join(current_directory, folder_name)
            files = os.listdir(folder_path)
            image_files = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

            if not image_files:
                print("\033[91mNo image files found in the specified folder.\033[0m")
                return

            random_image = random.choice(image_files)
            image_path = os.path.join(folder_path, random_image)
            _, file_extension = os.path.splitext(random_image)

            webhook = DiscordWebhook(url=webhook_url)
            embed = DiscordEmbed(color=0xFFFFFF)   
                                 # Custom embed colours
            embed.set_author(name="your_author", icon_url="")
                                                # Add a URL here with an icon you'd like to use as the author icon.
            embed.set_image(url=f"attachment://image{file_extension}")

            with open(image_path, "rb") as file:
                webhook.add_file(file=file.read(), filename=f"image{file_extension}") 
                                                   # Rename the file if you'd like
            webhook.add_embed(embed)
            response = webhook.execute()

            if response.status_code == 404:
                print("\033[91mWebhook status code 404: Not Found. Please check your webhook URL.\033[0m")
            elif response.status_code != 200:
                print(f"\033[91mError sending image '{random_image}'. Status code: {response.status_code}\033[0m")
            else:
                print(f"\033[38;2;200;157;216m'{random_image}' was sent to your webhook in an embed.\033[0m")

            time.sleep(cooldown)

    except Exception as e:
        print(f"\033[91mAn error occurred: {str(e)} \033[0m")

def main():
    # Your webhook that the embeds will send to
    webhook_url = "https://discord.com/api/webhooks/"
    # Just leave this as is -> put your images into this folder.
    folder_name = "images"
    # Set your custom cooldown or just leave it as "None" for the default 60 seconds.
    cooldown = None

    send_embed(webhook_url, folder_name, cooldown)

if __name__ == "__main__":
    main()
