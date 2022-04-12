#version 140
#include <shader.include.glsl>
in vec2 pos;

void main()
{
    gl_Position = vec2_to_4(pos);
}