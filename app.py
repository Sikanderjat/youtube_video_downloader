"""
### `app.py`

The `app.py` file serves as the main script for the YouTube Video Downloader web application. It is responsible for handling web requests, interfacing with the YouTube video downloading library, and rendering the HTML templates.

#### Key Sections:

1. **Imports:**
   ```python
   from flask import Flask, render_template, request
   from pytube import YouTube
   import os
   ```
   - `Flask` for creating the web application.
   - `render_template` for rendering HTML templates.
   - `request` to handle form submissions.
   - `YouTube` from `pytube` to download videos.
   - `os` for file operations.

2. **App Initialization:**
   ```python
   app = Flask(__name__)
   ```
   - Initializes the Flask application.

3. **Routes:**
   - **Homepage:**
     ```python
     @app.route('/')
     def home():
         return render_template('home.html')
     ```
     - Renders the `home.html` template where users can input the YouTube video URL.

   - **Download Status:**
     ```python
     @app.route('/downlode_status', methods=['POST'])
     def downlode_status():
         url = request.form['url']
         yt = YouTube(url)
         stream = yt.streams.get_highest_resolution()
         stream.download()
         return render_template('downlode_status.html', title=yt.title)
     ```
     - Handles the form submission from the homepage.
     - Extracts the YouTube video URL from the form.
     - Uses `pytube` to get the highest resolution stream and downloads the video.
     - Renders the `downlode_status.html` template with the video title.

   - **Download Complete:**
     ```python
     @app.route('/downloded')
     def downloded():
         return render_template('downloded.html')
     ```
     - Renders the `downloded.html` template to indicate the download is complete.

4. **Running the App:**
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```
   - Runs the Flask application in debug mode.

"""

from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("home.html")

@app.route("/downloded", methods=["POST"])
def downloded():
    url = request.form.get("url")
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=False).first()
        stream.download(output_path="C:/Users/sikan/Downloads/Sikander")
        return render_template("downloded.html", message="Video downloaded successfully!")
    except Exception as e:
        return render_template("downloded.html", message=f"Error: {str(e)}")
    


app.run(debug=True, host="localhost", port=5500)
