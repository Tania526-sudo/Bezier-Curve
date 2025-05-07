import numpy as np

def bezier_quad(P0, P1, P2, t):
    P0 = np.tile(P0, (len(t), 1))
    P1 = np.tile(P1, (len(t), 1))
    P2 = np.tile(P2, (len(t), 1))
    t = t[:, np.newaxis]
    return (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2

def translate(points, dx, dy):
    return points + np.array([dx, dy])

def rotate(points, angle_deg):
    theta = np.radians(angle_deg)
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta),  np.cos(theta)]])
    return points @ R.T

def scale(points, sx, sy):
    S = np.array([[sx, 0], [0, sy]])
    return points @ S.T