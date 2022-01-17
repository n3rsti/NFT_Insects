import numpy
from PIL import Image
import numpy as np
from colors import colors


class InsectGenerator:
    def __init__(self, background, outline, c1, c2, c3, eyes=None):
        self.background = background
        self.outline = outline
        self.eyes = outline
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

        if eyes is not None:
            self.eyes = eyes

    def generate_basic_png(self, name):
        # multiply
        def m(color, count=1):
            return [color for x in range(count)]

        bg = self.background
        o = self.outline
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        e = self.eyes

        patterns = {
            "horizontal_fade": [m(bg, 10) + m(o) + m(c1, 2) + m(c2, 6) + m(c1, 2) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c1, 1) + m(c2, 2) + m(c3, 4) + m(c2, 2) + m(c1, 1) + m(o) + m(bg,
                                                                                                                 10),
                              m(bg, 9) + m(o, 2) + m(c1, 1) + m(c2, 2) + m(c3, 1) + m(bg, 2) + m(c3, 1) + m(c2, 2) + m(
                                  c1, 1) + m(o, 2) + m(bg, 9),
                              m(bg, 8) + m(o) + m(bg) + m(o) + m(c1, 1) + m(c2, 2) + m(c3, 1) + m(bg, 2) + m(c3, 1) + m(
                                  c2, 2) + m(c1, 1) + m(o) + m(bg) + m(o) + m(bg, 8),
                              m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c1, 1) + m(c2, 2) + m(c3, 4) + m(c2, 2) + m(c1,
                                                                                                                1) + m(
                                  o) + m(bg, 2) + m(o) + m(bg, 7),
                              m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c1, 1) + m(c2, 1) + m(c2, 6) + m(c2, 1) + m(c1, 1) + m(o) + m(bg, 2) + m(
                                  o) + m(bg, 7),
                              m(bg, 10) + m(o) + m(c1, 1) + m(c2, 1) + m(o, 6) + m(c2, 1) + m(c1, 1) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c1, 1) + m(c2, 1) + m(o) + m(bg, 4) + m(o) + m(c2, 1) + m(c1, 1) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c1, 2) + m(o) + m(bg, 4) + m(o) + m(c1, 2) + m(o) + m(bg, 10)],

            "vertical_fade": [m(bg, 10) + m(o) + m(c2, 10) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c3, 10) + m(o) + m(bg, 10),
                              m(bg, 9) + m(o, 2) + m(bg, 10) + m(o, 2) + m(bg, 9),
                              m(bg, 8) + m(o) + m(bg) + m(o) + m(bg, 10) + m(o) + m(bg) + m(o) + m(bg, 8),
                              m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c3, 10) + m(o) + m(bg, 2) + m(o) + m(bg, 7),
                              m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c2, 10) + m(o) + m(bg, 2) + m(
                                  o) + m(bg, 7),
                              m(bg, 10) + m(o) + m(c1, 2) + m(o, 6) + m(c1, 2) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c1, 2) + m(o) + m(bg, 4) + m(o) + m(c1, 2) + m(o) + m(bg, 10),
                              m(bg, 10) + m(o) + m(c1, 2) + m(o) + m(bg, 4) + m(o) + m(c1, 2) + m(o) + m(bg, 10)],
            "inner_fade": [m(bg, 10) + m(o) + m(c1) + m(c2, 3) + m(c3, 2) + m(c2, 3) + m(c1) + m(o) + m(bg, 10),
                           m(bg, 10) + m(o) + m(c1) + m(c2) + m(c3, 2) + m(bg, 2) + m(c3, 2) + m(c2) + m(c1) + m(o) + m(bg, 10),
                           m(bg, 9) + m(o, 2) + m(c1) + m(c2) + m(c3) + m(bg) + m(o, 2) + m(bg) + m(c3) + m(c2) + m(c1) + m(o, 2) + m(bg, 9),
                           m(bg, 8) + m(o) + m(bg) + m(o) + m(c1) + m(c2) + m(c3) + m(bg) + m(o, 2) + m(bg) + m(c3) + m(c2) + m(c1) + m(o) + m(bg) + m(o) + m(bg, 8),
                           m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c1) + m(c2) + m(c3, 2) + m(bg, 2) + m(c3, 2) + m(c2) + m(c1) + m(o) + m(bg, 2) + m(o) + m(bg, 7),
                           m(bg, 7) + m(o) + m(bg, 2) + m(o) + m(c1) + m(c2, 3) + m(c3, 2) + m(c2, 3) + m(c1) + m(o) + m(bg, 2) + m(o) + m(bg, 7),
                           m(bg, 10) + m(o) + m(c1, 2) + m(o, 6) + m(c1, 2) + m(o) + m(bg, 10),
                           m(bg, 10) + m(o) + m(c1, 2) + m(o) + m(bg, 4) + m(o) + m(c1, 2) + m(o) + m(bg, 10),
                           m(bg, 10) + m(o) + m(c1, 2) + m(o) + m(bg, 4) + m(o) + m(c1, 2) + m(o) + m(bg, 10)],


        }
        pattern_name = numpy.random.choice(["horizontal_fade", "vertical_fade", "inner_fade"], p=[1/3, 1/3, 1/3])
        pixels_list = [
            m(bg, 32),
            m(bg, 32),
            m(bg, 32),
            m(bg, 32),
            m(bg, 8) + m(o, 2) + m(bg, 12) + m(o, 2) + m(bg, 8),
            m(bg, 10) + m(o) + m(bg, 10) + m(o) + m(bg, 10),
            m(bg, 11) + m(o) + m(bg, 8) + m(o) + m(bg, 11),
            m(bg, 11) + m(o) + m(bg, 2) + m(o, 4) + m(bg, 2) + m(o) + m(bg, 11),
            m(bg, 9) + m(o, 5) + m(c1, 4) + m(o, 5) + m(bg, 9),
            m(bg, 8) + m(o) + m(c1, 14) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3, 10) + m(c2) + m(c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3) + m(bg, 8) + m(c3) + m(c2) + m(c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3) + m(bg) + m(e, 2) + m(bg, 2) + m(e, 2) + m(bg) + m(c3) + m(c2) + m(
                c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3) + m(bg) + m(e, 2) + m(bg, 2) + m(e, 2) + m(bg) + m(c3) + m(c2) + m(
                c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3) + m(bg, 3) + m(e, 2) + m(bg, 3) + m(c3) + m(c2) + m(c1) + m(o) + m(
                bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3) + m(bg, 8) + m(c3) + m(c2) + m(c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2) + m(c3, 10) + m(c2) + m(c1) + m(o) + m(bg, 8),
            m(bg, 8) + m(o) + m(c1) + m(c2, 12) + m(c1) + m(o) + m(bg, 8),
            m(bg, 9) + m(o) + m(c1, 12) + m(o) + m(bg, 9),
            patterns[pattern_name][0],
            patterns[pattern_name][1],
            patterns[pattern_name][2],
            patterns[pattern_name][3],
            patterns[pattern_name][4],
            patterns[pattern_name][5],
            patterns[pattern_name][6],
            patterns[pattern_name][7],
            patterns[pattern_name][8],
            m(bg, 11) + m(o, 2) + m(bg, 6) + m(o, 2) + m(bg, 11),
            m(bg, 32),
            m(bg, 32),
            m(bg, 32),

        ]
        avatar_array = np.array(pixels_list, dtype=np.uint8)
        avatar_image = Image.fromarray(avatar_array)
        avatar_image = avatar_image.resize((32 * 12, 32 * 12), resample=Image.NEAREST)
        avatar_image.save(f"img/{name}.png")


for x in range(len(colors)):
    if len(colors[x]) == 5:
        insect = InsectGenerator(colors[x][0], colors[x][1], colors[x][2], colors[x][3], colors[x][4])
        reverse_insect = InsectGenerator(colors[x][4], colors[x][3], colors[x][2], colors[x][1], colors[x][0])
    else:
        insect = InsectGenerator(colors[x][0], colors[x][1], colors[x][2], colors[x][3], colors[x][4], colors[x][5])
        reverse_insect = InsectGenerator(colors[x][5], colors[x][4], colors[x][3], colors[x][2], colors[x][1],
                                         colors[x][0])
    insect.generate_basic_png(f"{x}")
    reverse_insect.generate_basic_png(f"{len(colors) + x}")
