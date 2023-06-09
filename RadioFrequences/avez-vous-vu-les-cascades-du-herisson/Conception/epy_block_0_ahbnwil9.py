"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from PIL import Image, ImageDraw, ImageFont, ImageOps
import pmt



class image_source(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    image_flip = False
    bt709_map = True
    image_invert = False
    autocontrast = False
    repeatmode = 1
    image_data = None
    eof = False
    size = 85

    def __init__(self, image_file="C:/Users/morom/Desktop/404/dumas.jpg", flag='404CTF{}', image_flip=False, bt709_map=True, image_invert=False, autocontrast=False, repeatmode=1, size=85):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(self,
            name='Create flag',   # will show up in GRC
            in_sig=[],
            out_sig=[np.uint8])
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.image_file = image_file
        self.flag = flag
        self.image_flip = image_flip
        self.bt709_map = bt709_map
        self.image_invert = image_invert
        self.autocontrast = autocontrast
        self.repeatmode = repeatmode
        self.size = size
        self.load_image()


    def load_image(self):
        """decode the image into a buffer"""
        self.image_data = Image.open(self.image_file)
        font=ImageFont.truetype('C:/Users/morom/Desktop/404/polic.ttf',self.size)
        w,h = self.image_data.size
        draw = ImageDraw.Draw(self.image_data)
        text_w, text_h = draw.textsize(self.flag, font)
        draw.text(((w-text_w) // 2,0),self.flag, font=font, fill=(255,255,255))
        self.image_data = ImageOps.grayscale(self.image_data)

        if self.autocontrast:
            # may improve the look of the transmitted spectrum
            self.image_data = ImageOps.autocontrast(self.image_data)

        if self.image_invert:
            # may improve the look of the transmitted spectrum
            self.image_data = ImageOps.invert(self.image_data)

        if self.image_flip:
            # set to true for waterfalls that scroll from the top
            self.image_data = ImageOps.flip(self.image_data)

        (self.image_width, self.image_height) = self.image_data.size
        max_width = 4096.0

        if self.image_width > max_width:
            scaling = max_width / self.image_width
            newsize = (int(self.image_width * scaling), int(self.image_height * scaling))
            (self.image_width, self.image_height) = newsize
            self.image_data = self.image_data.resize(newsize)
        self.set_output_multiple(self.image_width)

        self.image_data = list(self.image_data.getdata())
        if self.bt709_map:
            # scale brightness according to ITY-R BT.709
            self.image_data = map(lambda x: x*219 / 255 +16, self.image_data)
            self.image_data = list(self.image_data)
        self.image_len = len(self.image_data)

        if self.repeatmode != 2:
            print("paint.image_source: %d bytes, %dpx width" % (self.image_len, self.image_width))
        self.line_num = 0


    def work(self, input_items, output_items):
        if self.eof:
                return -1
        out = output_items[0]
        self.add_item_tag(0, self.nitems_written(0), pmt.intern("image_width"), pmt.from_long(self.image_width))
        self.add_item_tag(0, self.nitems_written(0), pmt.intern("line_num"), pmt.from_long(self.line_num))
        out[:self.image_width] = self.image_data[self.image_width*self.line_num: self.image_width*(1+self.line_num)]

        self.line_num +=1
        if self.line_num >= self.image_height:
            self.line_num = 0
            if self.repeatmode == 0:
                self.eof = True
            if self.repeatmode == 2:
                self.load_image()
        return self.image_width
