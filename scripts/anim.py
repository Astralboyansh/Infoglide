import pygame
import numpy as np
import moviepy.editor as mp
import os
def anim():
    pygame.init()

    # Screen dimensions
    width, height = 800, 600

    # Load background image
    background = pygame.image.load("class.jpeg")
    background = pygame.transform.scale(background, (width, height))
    background = pygame.transform.rotate(background, 180)

    # Load images for overlay
    image_directory = "images"  # Replace with your directory path
    image_files = os.listdir(image_directory)
    num_images = len(image_files)

    # Load man sprites
    man_stand = pygame.image.load("man_stand.png")
    man_talk = pygame.image.load("man_talk.png")
    man_move = pygame.image.load("man_move.png")

    # Load audio
    audio = mp.AudioFileClip("output2.mp3")
    total_duration = int(audio.duration)

    # Define the function to create frames
    def make_frame(t):
        sprite_duration = 3  # Duration for each sprite in seconds

        current_image_index = int((t * num_images / total_duration) % num_images)
        current_image = pygame.image.load(os.path.join(image_directory, image_files[current_image_index]))
        current_image = pygame.transform.scale(current_image, (width // 2 , height // 2))  # Adjust the scaling as needed
        current_image=pygame.transform.rotate(current_image, 180)

        man_t = t % 3
        if 0 <= man_t < 1:
            man_frame = pygame.transform.rotate(man_stand, 180)
        elif 1 <= man_t < 2:
            man_frame = pygame.transform.rotate(man_talk, 180)
        else:
            man_frame = pygame.transform.rotate(man_move, 180)

        frame = pygame.Surface((width, height))
        frame.blit(background, (0, 0))
        frame.blit(current_image, (width // 6, height // 3))  # Adjust the position of the overlay image as needed
        frame.blit(man_frame, (width - man_frame.get_width(), height - man_frame.get_height()))  # Adjust the position of the man

        return np.rot90(pygame.surfarray.array3d(frame))

    # Create a new MoviePy video clip
    video = mp.VideoClip(make_frame, duration=audio.duration)

    # Set the audio of the video clip
    video = video.set_audio(audio)

    # Save the video to a file
    video.write_videofile("output.mp4", fps=24, codec="mpeg4")

    pygame.quit()
