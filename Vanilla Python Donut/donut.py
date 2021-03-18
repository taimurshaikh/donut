# Python port of Andy Sloane's donut.c
import math
from numpy import dot, array, sin, cos, pi
WIDTH=HEIGHT=500
R1 = 1
R2 = 2
K2 = 5
THETA_SPACING = 0.07
PHI_SPACING = 0.02

def main():
    # renderFrame(45, 45)

def renderFrame(A, B):
    # Precompute sines and cosines of A and B
    cosA = cos(A)
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)

    # Sweep an angle theta to generate 2D circle cross-section of torus
    theta = 0
    while theta <= 2*pi:
        # Precompute sines and cosines of theta
        cosTheta = cos(theta)
        sinTheta = sin(theta)

        # Compute current 2D point of circle
        point = array([R2, 0, 0]) + array([R1*cosTheta,R1*sinTheta,0])

        # Sweep another angle phi to rotate cross section around y-axis to generate torus as a solid of revolution
        phi = 0
        while phi <= 2*pi:
            # Precompute sines and cosines of phi
            cosPhi = cos(phi)
            sinPhi = sin(phi)
            yRotation = array([[ cos(phi), 0,  sin(phi)],
                               [  0,       1,     0]   ,
                               [-sin(phi), 0,  cos(phi)]   ])
            point = dot(yRotation, point)
            phi += PHI_SPACING
        theta += THETA_SPACING


if __name__ == "__main__":
    main()
