#version 330 core

layout(triangles) in;
layout(line_strip, max_vertices = 12) out;

uniform vec4 g_pos;

void main()
{
    gl_Position = gl_in[0].gl_Position + g_pos;
    EmitVertex();
    EndPrimitive();
}
