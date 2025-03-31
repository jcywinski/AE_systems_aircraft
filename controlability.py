import numpy as np
import matplotlib.pyplot as plt


def controlability_plot():
    S = 50
    Sh = 10
    X_cg = np.linspace(-20,20,10)
    X_ac = 0.25
    C_l_h = -0.5
    C_l_A = 0.5
    l_h = 20
    c = 4
    V_h = 100
    V = 110
    S_h_S = np.zeros(len(X_cg))
    C_m_ac = -0.5

    i = 0
    for x_cg in X_cg:
        S_h_S[i] = 1/((C_l_h/C_l_A)*(l_h/c)*(V_h/V)**2)*x_cg + (C_m_ac/C_l_A - X_ac)/((C_l_h/C_l_A)*(l_h/c)*(V_h/V)**2)
        i = i+1
    plt.plot(X_cg/c,S_h_S, label='Controlability')
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.xlabel('X_cg/MAC')
    plt.ylabel('S_h/S')
    plt.legend()
    plt.show()

controlability_plot()