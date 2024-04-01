from pytube import YouTube

def download_video():
    # prompt for the user
    video_url = input("Enter the URL of the YouTube video you want to download: ")

    try:
        # create youtube object
        yt = YouTube(video_url)

        # get high res
        stream = yt.streams.get_highest_resolution()

        # download the video
        stream.download()

        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", e)

# call the function to start downloading
download_video()