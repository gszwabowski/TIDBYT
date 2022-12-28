"""
This .star file serves as a template from which to create animations to display on a Tidbyt device.
Once each image in an image sequence is base64 encoded, the encoded images can be pasted onto line
19. After pasting the frames and saving the file, use 'pixlet render <this file>' to render this file
as a .webp animation and 'pixlet push <tidbyt-device-id> <.webp file>' to view it on your Tidbyt.
"""

load("encoding/base64.star", "base64")
load("render.star", "render")
load("schema.star", "schema")
load("time.star", "time")

def main(config):
    seed = int(time.now().unix)
    seed = [seed]


    # FRAMES
    FRAMES = [
		# add base64 encoded frames here	
        ]

   
    return render.Root(
        child = render.Animation(
            children = [render.Image(src = base64.decode(f)) for f in FRAMES],
        ),
        delay = 30,
    )