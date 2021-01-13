# Import Libraries
import math
import plotly.graph_objects as pg
import numpy as np

# Plot of a 2D-gaussian landscape

def gaussiannet(nn_list, plot_m, plot_s):
    # import plotly.graph_objects as gob
    #plot_m = 20
    #plot_s = .1
    m = int(plot_m/plot_s)

    # print(m)
    x = []
    y = []
    z = []
    sigma = []
    mux = []
    muy = []
    amp = []

    for i in range(0, m):
        j = i*plot_s
        x.append(j)
        y.append(j)

    for i in nn_list:
        # print(i)
        mux.append(i[0])
        muy.append(i[1])
        sigma.append(i[2])
        amp.append(i[3])
    
    # print('X     : ',mux)
    # print('Y     : ',muy)
    # print('sigma : ',sigma)
    # print('Ampli : ',amp)
    
    la = len(amp)
    mx = plot_m
    my = plot_m
    pi = math.pi
    bmax = 0
    
    # print(la) 
    
    for j in range(0, m):
        a = []
        for i in range(0,m):
            b = 0
            for k in range(0, la):
            
                xi = x[i]
                if (mux[k]-x[i]>=mx/2):
                    xi=x[i]+mx
                if (x[i]-mux[k]>=mx/2):
                    xi=x[i]-mx
                
                yj = y[j]
                if (muy[k]-y[j]>=my/2):
                    yj=y[j]+my
                if (y[j]-muy[k]>=my/2):
                    yj=y[j]-my
                
                b = amp[k] * (1/(2*pi*pow(sigma[k],2))) * math.exp( -(pow((xi-mux[k]),2) + pow((yj-muy[k]),2))/(2*pow(sigma[k],2))) + b    
         
            bmax = max(b, bmax)
            a.append(b)
        z.append(a)
  
    # print(z)

    fig = pg.Figure(pg.Surface(cmin = 0, cmax = bmax,
        contours = {
            # "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
            "z": {"show": True, "start": 0.1, "end": bmax, "size": 0.1}
        },
        x = x, y = y, z = z))
    fig.update_layout(
            scene = {
                "xaxis": {"nticks": 20},
                "zaxis": {"nticks": 4},
                'camera_eye': {"x": 0, "y": -1, "z": 0.5},
                "aspectratio": {"x": 1, "y": 1, "z": 0.5}
            })
    fig.show()
    
    
# Convert matrix to 2D-net input    
    
def mattonet(nn_mat):
    nn_ml =[]
    ml = len(nn_mat)
    fl = len(nn_mat[0][0])
    for i in range(0,ml):
        for j in range(0,ml):
            for k in range(0, fl):
                a = []
                if not (nn_mat[i][j][k][0]==0 and nn_mat[i][j][k][1]==0):
                    # print(i, j, k, nn_mat[i][j][k])
                    a.append(i)
                    a.append(j)
                    a.append(nn_mat[i][j][k][0])
                    a.append(nn_mat[i][j][k][1])
                    # print(a)
                    at = tuple(a)
                    # print(at)
                    nn_ml.append(at)
    return(nn_ml)                
