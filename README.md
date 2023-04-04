# Transcript-summarizer



## Setup

install open-whisper can also see the setup here : https://github.com/openai/whisper

```bash
pip install -U openai-whisper
```

install ffmpeg

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

clone the project

```bash
git clone https://github.com/wsenn/transcript-summarizer
```

install dependencies

```bash
pip install -r requirements.txt
```

replace your Webhook by zapier in the app.py file
```python
webhook_url = "YOUR_URL_WEBHOOK_ZAPIER"
```


