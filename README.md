# Garage Camera System

## Overview

This project sets up a garage camera system that captures images of your garage. The system is integrated with a Discord bot, allowing you to trigger image captures and receive them in a specified Discord channel.
## Features

- Capture images of the garage
- Retrieve the latest image via a Discord bot
- Image sent to a specified Discord channel
- Acess image with a swift app or website
- Works also with Home Assistant
 
## Requirements

- Raspberry Pi (recommended)
- Camera module compatible with your device
- Python 3.10+
- Discord bot (not necessary)

## Installation
### Using setup.sh

1. Clone the repository:

    ```
    git clone https://github.com/BennoCrafter/GargeCamera.git
    ```

2. Execute setup.sh:
    ```
    sh scripts/sh/setup.sh
    ```

Make sure you’re running the setup.sh script from the main directory of the project to cause to path conflicts.

## Setup Discord Bot

1. Create a Discord bot and get the bot token.
2. Add the bot to your Discord server.
3. Make sure the bot has permissions to send messages in the specified channel.

## Usage

1. Connect your camera module to the Raspberry Pi or your chosen device.
2. Run the `run.sh` script:

    ```
    ./run.sh
    ```

3. Use the `/setup` slash command in Discord to configure the destination channel for the images and other important configs.
4. Press the button in Discord to capture an image. The image will be sent to the specified channel.


## Troubleshooting

If you're having problems with running setup.sh just install it yourself.
1. Install required Python packages:

    ```
    pip install -r scripts/sh/requirements.txt
    ```

2. Install fswebcam module
    ```
    sudo apt-get install fswebcam
    ```

3. Make `run.sh` executable:

    ```
    chmod +x run.sh
    ```

4. Run setup.py file:

    ```
    python setup/setup.py
    ```

## Contributing

Feel free to fork the repository and submit pull requests or open issues if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
