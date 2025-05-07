from pythreejs import *
import numpy as np
from IPython.display import display

# Bezier curve in 3D (z = 0)
def bezier_curve_3d(P0, P1, P2, t):
    return (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2

t = np.linspace(0, 1, 100)
P0 = np.array([0, 0, 0])
P1 = np.array([1, 2, 1])
P2 = np.array([2, 0, 0])
curve = np.array([bezier_curve_3d(P0, P1, P2, ti) for ti in t])

geometry = BufferGeometry(attributes={
    'position': BufferAttribute(curve.astype(np.float32), normalized=False)
})

material = LineBasicMaterial(color='blue')
line = Line(geometry=geometry, material=material)

# Axle and camera
axes = AxesHelper(size=2)
camera = PerspectiveCamera(position=[4, 3, 3], up=[0, 0, 1], children=[DirectionalLight(color='white', position=[3, 5, 1], intensity=0.5)])
scene = Scene(children=[line, axes, camera, AmbientLight(intensity=0.3)], background='#ffffff')

renderer = Renderer(camera=camera, scene=scene, controls=[OrbitControls(controlling=camera)], width=600, height=400)
display(renderer)