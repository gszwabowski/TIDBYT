'''
Author: Gregory Szwabowski

Input: a directory containing a sequence of .png images that resulted from exporting a .gif to an image sequence in Photoshop
Output: a .star file called  <output> that contains each image encoded with base64 on its own line of the text file.

Once the .star file is created, use 'pixlet render <this file>' to render the resulting .star file as a .webp animation and
use 'pixlet push <tidbyt-device-id> <.webp file>' to view it on your Tidbyt. The .webp file resulting from the 'pixlet render'
command may need to be compressed to avoid errors when pushing it to your Tidbyt.

Example command from Windows CMD: python encode_image_seq_to_star_file.py GBA_anims\MonkeyBall\ smb_anim.star
'''
def main():
    import os
    import sys
    import base64
    
    directory = sys.argv[1]
    output = sys.argv[2]
    
    # get list of files in provided directory
    files = os.listdir(directory)
    
    # loop through each file and encode it to base64
    imgs = []
    encoded_imgs = []
    i = 0
    
    # get .png files
    for file in files:
        if '.png' in file:
            imgs.append(file)
    
    # loop through png files and convert to base64
    for img in imgs:
        i+=1
        with open(directory + img, "rb") as img_file:
            img_string = base64.b64encode(img_file.read())
        img_string = img_string.decode('utf-8')
        if i == 1:
            encoded_imgs.append('"""' + img_string + '""",')
        else:
            encoded_imgs.append('\t\t\t"""' + img_string + '""",')
        print('Encoded image', str(i), 'of', str(len(imgs)) + '.')
        
    # write encoded strings to file
    with open(directory + 'frames.txt', 'w') as f:
        f.write('\n'.join(encoded_imgs))
        
    # A Simple Python template example
    from string import Template

    
    starfile_templatedata = 'load("encoding/base64.star", "base64")\nload("render.star", "render")\nload("schema.star", "schema")\nload("time.star", "time")\n\ndef main(config):\n    seed = int(time.now().unix)\n    seed = [seed]\n\n\n    # FRAMES\n    FRAMES = [\n\t\t\t$frames\n            ]\n\n   \n    return render.Root(\n        child = render.Animation(\n            children = [render.Image(src = base64.decode(f)) for f in FRAMES],\n        ),\n        delay = 30,\n    )'

    with open(directory + 'frames.txt', 'r') as frames_file:
        framedata = frames_file.read()

    t = Template(starfile_templatedata)

    sub_t = t.substitute({'frames' : framedata})

    with open(directory + output, 'w') as f:
        f.write(sub_t)
        
    print('\nImage sequence written to', directory + output + '.')


if __name__ == '__main__':
   main()
