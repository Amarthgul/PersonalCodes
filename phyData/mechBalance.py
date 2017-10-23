def plotChange():
    dataSet = np.array([[0.15,  0,  8,  7,  5],
                        [ 2.0,  1,  8,  7,  5],
                        [ 2.9, 1.5, 8,  7,  5],
                        [4.05,  2,  8,  7,  5],#====1
                        [0.15,  0,  7,  7,  6],
                        [2.05,  1,  7,  7,  6],
                        [3.15, 1.5, 7,  7,  6],
                        [4.05,  2,  7,  7,  6],#====2
                        [0.15,  0,  10,  7,  4],
                        [2.75,  1,  10,  7,  4],
                        [3.80, 1.5, 10,  7,  4],
                        [4.50,  2,  10,  7,  4],#====3
                        [0.15,  0,  10,  9,  4.5],
                        [2.15,  1,  10,  9,  4.5],
                        [2.85, 1.5, 10,  9,  4.5],
                        [3.60,  2,  10,  9,  4.5],#====4
                        [0.15,  0,  12,  9,  3],
                        [2.35,  1,  12,  9,  3],
                        [2.95, 1.5, 12,  9,  3],
                        [3.75,  2,  12,  9,  3],#====5
                        [0.15,  0,  10,  7,  2],
                        [2.45,  1,  10,  7,  2],
                        [3.75, 1.5, 10,  7,  2],
                        [4.2,  2,  10,  7,  2],#====6
                        ])

    plot = False
    if plot:
        gridColor = 'r'; alp = 0.5
        fig = plt.figure(figsize = (10, 10))
        ax = plt.axes()
        for i in range(6):
            ax.plot(dataSet[i*4: (i+1)*4, 1], dataSet[i*4: (i+1)*4, 0], 'rx',
                     mew = 5, ms = 10)
        for i in range(6):
            N_0 = int(dataSet[i*4, 2]); N_1 = int(dataSet[i*4, 3])
            N_2 = int(dataSet[i*4, 4])
            strLabel = '$N_{0}$:' + str(N_0) + '\t' +\
                '$N_{1}$:' + str(N_1) + '\t' + '$N_{2}$:' + str(N_2)
            ax.plot(dataSet[i*4: (i+1)*4, 1], 
                     dataSet[i*4: (i+1)*4, 0], linewidth = 2,
                     label = strLabel)
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(1))
        ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
        ax.xaxis.set_major_locator(plt.MultipleLocator(0.25))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(0.025))
        ax.grid(which='major', axis='y', linewidth=1.5, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='minor', axis='y', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='major', axis='x', linewidth=1.5, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='minor', axis='x', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
        plt.legend(loc = 'best')
        plt.xlim(1.25, 2); plt.ylim(2, 5)
        plt.show()

    force = dataSet[:, 0];

    rest = dataSet[:, 1:] #use np.c_[a, b] to merge
    #print(force, pins, n_0, n_1, n_2)
    input = np.array([pins, n_0, n_1, n_2])
    print(input)
    reg = linear_model.LinearRegression()
    reg.fit(rest, force)
    print(reg.coef_)
    return 0
