

import gc
import glm
import glm_typing
import struct
import copy
import pickle
import typing
import ctypes
import operator
import time
from datetime import timedelta
from gamut import *
from gamut.event import *
from gamut.graphics import *
from gamut.peripheral import *
from gamut.text import *
from typing import *
import inspect
from gamut.audio import *
import wave
from openal.al import alIsExtensionPresent
from openal.alc import alcGetString, ALC_CAPTURE_DEVICE_SPECIFIER
from openal.al_lib import lib
from gamut.audio._alcontext import require_al_context, get_al_context
import math
import numpy as np
import matplotlib.pyplot as plt
import PIL

import uharfbuzz as hb
from icu import Char as IcuChar

z = ord('←')
print(z)
print(chr(z))

vertex = b'''
#version 140
in vec2 pos;
in vec2 uv;
uniform mat4 transform;
out vec2 vertex_uv;
void main()
{
    vertex_uv = uv;
    gl_Position = transform * vec4(pos, 0, 1.0);
}
'''

fragment = b"""
#version 140
in vec2 vertex_uv;
uniform vec4 color;
uniform sampler2D tex;
out vec4 output_color;
void main()
{
    output_color = vec4(color.rgb, texture(tex, vertex_uv).r);
}
"""

class App(Application):

    async def main(self):
        w = Window()
        w.resize(800, 800)
        w.recenter()
        w.is_visible = True
        rt = WindowRenderTarget(w)
        clear_render_target(rt, color=Color(1, 1, 1))
        
        shader = Shader(vertex=vertex, fragment=fragment)
        quad_pos = BufferView(
            Buffer(glm.array(
                glm.vec2(0, 0),
                glm.vec2(0, 1),
                glm.vec2(1, 1),
                glm.vec2(1, 1),
                glm.vec2(0, 0),
                glm.vec2(1, 0),
            ).to_bytes()),
            glm.vec2,
        )
        
        face = Face('Roboto-Regular.ttf')
        size = face.request_pixel_size(height=64)
        font = AtlasFont(size, RenderedGlyphFormat.ALPHA)
        
        ortho = glm.ortho(0, 800, 800, 0, -1000, 1000)

        for g in font.layout_text(
            'hello ← world',
            break_method=break_line_icu,
            max_line_size=400,
        ):
            if not character_normally_rendered(g.character):
                print(repr(g.character))
                continue
            ag = font[g.glyph_index]
            top_left, bottom_right = ag.uv
            ag_uv = BufferView(
                Buffer(glm.array(
                    glm.vec2(top_left[0], top_left[1]),
                    glm.vec2(top_left[0], bottom_right[1]),
                    glm.vec2(bottom_right[0], bottom_right[1]),
                    glm.vec2(bottom_right[0], bottom_right[1]),
                    glm.vec2(top_left[0], top_left[1]),
                    glm.vec2(bottom_right[0], top_left[1]),
                ).to_bytes()),
                glm.vec2,
            )
            ag_transform = (
                ortho *
                glm.scale(
                    glm.translate(
                        glm.mat4(1),
                        glm.vec3(*g.position, 0) + glm.vec3(*ag.bearing, 0)
                    ), 
                    glm.vec3(*ag.size, 1)
                )
            )
            execute_shader(
                rt,
                shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": quad_pos,
                    "uv": ag_uv,
                }),
                {
                    "transform": ag_transform,
                    "tex": ag.texture,
                    "color": glm.vec4(1, 0, 0, 1),
                },
                index_range=(0, 6),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )
        w.flip_buffer()
            
        await w.Close

app = App()
app.run()


'''
z = ord('←')
print(z)
print(chr(z))


face = Face('Roboto-Regular.ttf')
size = face.request_pixel_size(height=21)
font = AtlasFont(size, RenderedGlyphFormat.ALPHA)
canvas = PIL.Image.new('L', (200, 200), color=0)
for g in font.layout_text(
    'hello ←\nworld',
    break_method=break_line_icu,
    max_line_size=20,
):
    if not character_normally_rendered(g.character):
        print(repr(g.character))
        continue
    ag = font[g.glyph_index]
    print(ag)
    """
    render = font.render_glyph(g.glyph_index)
    if render._size != (0, 0):
        i = PIL.Image.frombytes('L', render._size, render._data)
        canvas.paste(
            i,
            (
                int(g.position[0] + render.bearing[0]),
                int(g.position[1] + render.bearing[1])
            )
        )
    """
#canvas.show()
'''

