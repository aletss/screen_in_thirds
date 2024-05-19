from PIL import Image, ImageDraw, ImageTk
import screeninfo
import tkinter
import sys

WINDOW_NAME = 'image'
IMAGE_PATH = 'thirds.png'
LINE_COLOR = 'white'
LINE_COLOR_ALPHA_DEFAULT = 0.8

if len(sys.argv) > 1:
    line_color_alpha = sys.argv[1]
else:
    line_color_alpha = LINE_COLOR_ALPHA_DEFAULT

def get_screen_size():
    screen_id = 0
    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height

    return width, height

def create_image_thirds(width, height):
    background_color = (0, 0, 0, 0) # black transparent (alpha 0)
    line_width = 3

    # Create black image
    im = Image.new('RGBA', (width, height), background_color)
    draw = ImageDraw.Draw(im)

    # horizontal lines
    x1,y1,x2,y2 = (0, height*1/3) + (width, height*1/3)
    draw.line((x1,y1,x2,y2), fill=LINE_COLOR, width=line_width)

    x1,y1,x2,y2 = (0, height*2/3) + (width, height*2/3)
    draw.line((x1,y1,x2,y2), fill=LINE_COLOR, width=line_width)

    # vertical lines
    x1,y1,x2,y2 = (width*1/3, 0) + (width*1/3, height)
    draw.line((x1,y1,x2,y2), fill=LINE_COLOR, width=line_width)

    x1,y1,x2,y2 = (width*2/3, 0) + (width*2/3, height)
    draw.line((x1,y1,x2,y2), fill=LINE_COLOR, width=line_width)

    return im

def show_image(img, width, height):
    #Create an instance of tkinter frame
    win = tkinter.Tk()

    # Create transparent window
    win.attributes('-fullscreen', True)
    win.attributes('-alpha', line_color_alpha)

    #Create a canvas
    canvas= tkinter.Canvas(win, bg='black', width=width, height=height)
    canvas.pack()

    #Load an image in the script
    img= ImageTk.PhotoImage(img)

    #Add image to the Canvas Items
    canvas.create_image(10,10,anchor=tkinter.NW,image=img)
    canvas.config(highlightthickness=0)
    canvas.config(borderwidth=1)

    # Create a transparent window
    win.wm_attributes('-transparentcolor','black')

    # Set window on top of the others
    win.attributes('-topmost', True)

    win.mainloop()

def main():
    width, height = get_screen_size()

    img = create_image_thirds(width, height)
    img.save(IMAGE_PATH)

    #Load an image in the script
    img = Image.open(IMAGE_PATH)

    show_image(img, width, height)

main()
