from bibliopixel.animation import BaseStripAnim
import bibliopixel.colors as colors

class ColorFade(BaseStripAnim):
    """Fill the dots progressively along the strip."""

    def wave_range(self, start, peak, step):
        main = [i for i in range(start, peak+1, step)]
        return main + [i for i in reversed(main[0:len(main)-1])]

    def __init__(self, led, colors, step = 5, start=0, end=-1):
        super(ColorFade, self).__init__(led, start, end)
        self._colors = colors
        self._levels = self.wave_range(30, 255, step)
        self._level_count = len(self._levels)
        self._color_count = len(colors)

    def step(self, amt = 1):
        if self._step > self._level_count * self._color_count:
            self._step = 0

        c_index = (self._step / self._level_count) % self._color_count
        l_index = (self._step % self._level_count)
        color = self._colors[c_index];
        self._led.fill(colors.color_scale(color, self._levels[l_index]), self._start, self._end)

        self._step += amt


#Needs color list input on UI
# MANIFEST = [
#     {
#         "class": ColorFade,
#         "controller": "strip",
#         "desc": None,
#         "display": "ColorFade",
#         "id": "ColorFade",
#         "params": [
#             {
#                 "default": -1,
#                 "help": "",
#                 "id": "end",
#                 "label": "End Pixel",
#                 "type": "int"
#             },
#             {
#                 "default": 0,
#                 "help": "",
#                 "id": "start",
#                 "label": "Start Pixel",
#                 "type": "int"
#             },
#             {
#                 "default": 5,
#                 "help": "Amount to change brightness by. 0-255",
#                 "id": "step",
#                 "label": "Step",
#                 "type": "int"
#             },
#             {
#                 "default": None,
#                 "help": "",
#                 "id": "colors",
#                 "label": "",
#                 "type": ""
#             }
#         ],
#         "type": "animation"
#     }
# ]
