I have started this task by writing main.cpp by referring vulkan website <br>
then I learnt that for a basic 2d figure, main.cpp remains constant. only thing that changes is shader.vert where
the coordinates is given.<br>
so for this task, since understanding how main.cpp is hard to understand in the time that is left, I have decided to concentrate on the part where the coordinates are given<br>


here is the shader.vert when we need to render a triangle
```
#version 450

layout(location = 0) out vec3 fragColor;

vec2 positions[3] = vec2[](
    vec2(0.0, -0.5),
    vec2(0.5, 0.5),
    vec2(-0.5, 0.5)
);

vec3 colors[3] = vec3[](
    vec3(1.0, 0.0, 0.0),
    vec3(0.0, 1.0, 0.0),
    vec3(0.0, 0.0, 1.0)
);

void main() {
    gl_Position = vec4(positions[gl_VertexIndex], 0.0, 1.0);
    fragColor = colors[gl_VertexIndex];
}
```


and this is when a square is to be rendered
```
vec2 positions[4]=vec2[](
    vec2(-0.5,-0.5)
    vec2(0.5,-0.5)
    vec2(0.5,0.5)
    vec2(-0.5,0.5)
)

vec2 texCoords[4]=vec2[](
    vec2(0.0,0.0)
    vec2(1.0,0.0)
    vec2(1.0,1.0)
    vec2(0.0,1.0)
)
```