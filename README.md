# RandomQueue

RandomQueue is a Python application that allows Spotify users to add random tracks to their queue. The application uses the Spotify API to search for tracks from a wide range of genres and add them to the user's queue.

## Features

- Add a specified number of random tracks to the user's Spotify queue
- Tracks are selected from a wide range of genres

## Before you install

Before you can use RandomQueue, you need to create a Spotify Developer application to get your `client_id`, `client_secret`, and `redirect_uri`. Here's how you can do it:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on 'Create an App'.
4. Fill in the 'Name', 'Description' and redirect_uri (I recommend using http://localhost:3000/) for your new app, then click 'Create'.
5. On the next page, you will see your `client_id` and `client_secret`. You will need these to authenticate your application.
6. Click on 'Edit Settings'.
7. In the 'Redirect URIs' field, enter the URI where you want Spotify to redirect you after a successful login.
8. Click 'Save'.

## Installation

1. Go to the release section of this repository. [Current release.](https://github.com/PanPeryskop/RandomQueue/releases/tag/v1.0)
2. Click on **RandomQueue.zip**. Download will start automatically.
3. Extract the zip file.
4. Open the extracted folder and run `RandomQueue.exe`.

## Usage

1. Run the `RandomQueue.exe` to start the application.
2. The application will ask you to enter your `client_id`, `client_secret`, and `redirect_uri`. Enter the values from the Spotify Developer Dashboard.
3. The application will ask you how many tracks you want to add to the queue. You can enter a number using the slider or the input field.
4. The application will then add the specified number of random tracks to your queue.
5. Once the tracks are added, a message will be displayed confirming the successful addition of the tracks to the queue.

Enjoy your music!

# Warning
 When you use it for the first time it may require rerun after providing Spotify Dashboard info.
