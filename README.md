# YouTube Video Downloader

This is a simple web application for downloading YouTube videos. It is built using Flask for the web framework and `pytube` for handling the video downloading.

## Features
- Download YouTube videos in various formats and resolutions.
- Simple and user-friendly web interface.

## Requirements
- Python 3.x
- Flask
- pytube

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sikander2703/youtube_video_downloder.git
    ```
2. Navigate to the project directory:
    ```bash
    cd youtube_video_downloder
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Enter the URL of the YouTube video you want to download.
4. Choose the format and resolution.
5. Click the download button and wait for the video to be processed and downloaded.

## File Descriptions

- `app.py`: The main application script.
- `templates/home.html`: The homepage for entering the video URL.
- `templates/downlode_status.html`: Page showing the download status.
- `templates/downloded.html`: Page displayed after the video is successfully downloaded.
