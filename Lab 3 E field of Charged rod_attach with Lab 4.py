#The Electric Field of a Uniformly Charged Rod

from __future__ import division
from visual import *

# Define Constants
e      = 1.6e-19             # (Coulombs)    Charge of a proton
oofpez = 9e9                 # (Nm^2 / C^2)  Electric constant
scalefactor = 0.5/619.630133 # (unitless)    Desired magnitude / actual magnitude

L = 2                      # (meters)      The length of the rod
N = 100                     # (unitless)    The number of sections of the rod, 100 makes it look like a line of charge
Q = 3e-8                   # (Coulombs)    The charge of the rod
deltax = L/N               # (meters)      The length of each segment
deltaq = Q/N               # (Coulombs)    The charge of each segment
deltat = 0.001              #(s)    The time interval. It's a trade of between accuracy and runtime
obslocation = vector(0.3,0.4,0)  # (meters) The observation location


# Set Initial Values
x =  -0.5 * L + 0.5 * deltax              # Component of the location of the leftmost piece
Enet = vector(0, 0, 0)                    # The net electric field at obslocation
t = 0
deltaVtotal = 0
# Create objects
Vgraph = gcurve(color = color.cyan)
marker = sphere(color = color.red, pos = vector(0,0.15,0),radius = 0.05)
while x < L/2 :                           # Loop over the creation of many spheres to be the rod
    sphere(pos = vector(x, 0, 0), radius = 0.1, color = color.cyan) # Make a sphere
    x = x + deltax                        # Loop update

#Calculations

while marker.pos.y<1.15:
    maker.v = vector(0,0.5,0)
    x =  -0.5 * L + 0.5 * deltax   # Reset for new loop
    Enet = vector(0,0,0)
    while x < L/2 :
        r = marker.pos - vector(x, 0, 0)      # Displacement vector to obslocation
        rmag = mag(r)                          # Magnitude
        rhat = r / rmag                        # Unit vector
        E = (oofpez * deltaq / rmag**2) * rhat # Electric field at obslocation due to current sphere
        Enet = Enet + E                        # Update Enet
        x = x + deltax                         # Loop update
        deltaV = dot(E,marker.v*deltat)
        deltaVtotal+=deltaV
        t+=deltat
        marker.pos += marker.v*deltat

        Vgraph.plot(pos=(t,deltaVtotal))

print(deltaVtotal)
#Earrow = arrow(pos = obslocation, axis = Enet * scalefactor, color = color.orange) # Display arrow

# print "The net E field is: ", Enet, "N/C"  # Print result
#print ("N \t= ", N, "\n|Enet|  = ", mag(Enet), "N/C")



