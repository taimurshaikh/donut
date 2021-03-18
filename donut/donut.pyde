  # Python Processing port of Andy Sloane's donut.c
from matrix import *

WIDTH=HEIGHT=800

R1 = 50
R2 = 100
THETA_SPACING = 0.5
PHI_SPACING = 0.07
yOff= HEIGHT/2
xOff = WIDTH/2
A = 0
B = 0

def setup():
    size(WIDTH, HEIGHT)
    background(255)

def renderFrame(A, B):
    """ Computes points of 2D Circle (cross section of donut) """
    # Precompute sines and cosines of A and B
    cosA = cos(A)
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)
    
    # Sweep an angle theta to generate 2D circle cross-section of torus
    theta = 0
    while theta <= 2*PI:
        # Precompute sines and cosines of theta
        cosTheta = cos(theta)
        sinTheta = sin(theta)
        
        # Sweep angle phi around y-axis to generate torus
        phi = 0
        while phi <= 2*PI:
            # Precompute sines and cosines of phi
            cosPhi = cos(phi)
            sinPhi = sin(phi)
            
            yRotation = [[cosPhi, 0, sinPhi], [0, 1, 0], [-sinPhi, 0, cosPhi]]
            xRotation = [[1, 0, 0], [0, cosA, sinA], [0, -sinA, cosA]]
            zRotation = [[cosB, sinB, 0], [-sinB, cosB, 0], [0, 0, 1]] 
            
            # Rotate about X and Z axes to obtain final result
            currPoint = vecMatMul(zRotation ,vecMatMul(xRotation, vecMatMul(yRotation, PVector(R2+R1*cosTheta, R1*sinTheta, 0))))
            point(currPoint.x + xOff, currPoint.y + yOff)
            phi += PHI_SPACING
        theta += THETA_SPACING
        strokeWeight(2.5)
        stroke(255)
        fill(175)

def draw():
    global A
    global B
    global rev

    background(0)
    
    renderFrame(A, B)
    # if rev:
    #     A -= 0.1
    #     B -= 0.1
    # else:
    A += 0.08
    B += 0.08
    
