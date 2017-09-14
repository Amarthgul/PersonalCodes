
def questionIllu(position = [12, 8]):
    import numpy as np
    import matplotlib.pylab as plt
    import mpl_toolkits.mplot3d 

    m = (position[0] - 24) / 48
    n = (position[1] - 24) / 48
    mine = [[-24, -24, 24, 24], [-24, 24, -24, 24]]
    print(m, n)
    result = [24+48*round(m), 24+48*round(n)]

    size = 25
    fontS = 50
    dotS = 200
    x = np.linspace(-size, size)
    y = np.linspace(-size, size)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x * y)

    twFour = np.array([-size, size])
    zeros = np.array([0, 0])

    fig = plt.figure(figsize = (20, 25))
    ax = plt.axes([0.025, 0.025, 0.95, 0.7], projection = '3d')
    ax.plot(twFour, zeros, zeros, linewidth = 2, c = 'k')
    ax.plot(zeros, twFour, zeros, linewidth = 2, c = 'k')
    ax.plot([24, -24], [24, 24], [0, 0], linewidth = 2, c = 'k')
    ax.plot([24, 24], [24, -24], [0, 0], linewidth = 2, c = 'k')
    ax.plot([-24, 24], [-24, -24], [0, 0], linewidth = 2, c = 'k')
    ax.plot([-24, -24], [-24, 24], [0, 0], linewidth = 2, c = 'k')
    

    ax.plot_surface(x, y, z, rstride = 1, cstride = 1,\
        linewidth = 0.75, alpha = 0.25, color = '#C49A6C')
    ax.scatter(position[0], position[1], 0, color = 'r', s = dotS)
    ax.scatter(mine[0], mine[1], 0, color = 'g', s = dotS)
    ax.scatter(result[0], result[1], 0.25, color = 'b', s = dotS)
    ax.set_zlim(-5, 5); 
    ax.set_xlim(-size, size); ax.set_ylim(-size, size)

    bx = plt.axes([0.025, 0.75, 0.95, 0.225])
    plt.xticks([]); plt.yticks([])
    bx.text(0, 0.8, 'Ori Position: ({}, {})'.format(position[0], position[1]),
            fontsize = fontS)
    bx.text(0, 0.55, r'$m=\frac{posX-24}{48}='+\
        str(m)+r'$; $n=\frac{posZ-24}{48}='+str(n)+'$',
            fontsize = fontS)
    bx.text(0, 0.3, r'$m\' :'+str(round(m))+'$   $'+\
        ' n\' :'+str(round(n))+'$', fontsize = fontS)
    bx.text(0, 0.05, 'sub: {}, {}'.format(result[0], result[1]),
            fontsize = fontS)
            
    plt.show()
