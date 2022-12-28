load("encoding/base64.star", "base64")
load("render.star", "render")
load("schema.star", "schema")
load("time.star", "time")

def main(config):
    seed = int(time.now().unix)
    seed = [seed]


    # FRAMES
    FRAMES = [
			$frames
            ]

   
    return render.Root(
        child = render.Animation(
            children = [render.Image(src = base64.decode(f)) for f in FRAMES],
        ),
        delay = 30,
    )