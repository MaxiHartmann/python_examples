import numpy as np
import pandas as pd

def get_data(filename):
        # find number of rows to skip
        any_header_name = 'orifice'

        n=0
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if any_header_name in line:
                    # print('found at line:'+ str(num))
                    n=num-1

        df = pd.read_csv(filename, delimiter="\s+", skiprows=n)
        # print(data.mean(axis=1))

        # print columnnames
        # print(data.columns)
        # print(data.flow_rate)

        # Clean data from NaNs
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.dropna()
        df = df.reset_index(drop=True)
        print(df)

        return df

if __name__ == "__main__":
    # plotting
    import matplotlib.pyplot as plt

    filename='example_data_1.txt'
    data = get_data(filename)

    fig, ax = plt.subplots()
    ax.plot(data.flow_rate, data.dp_1, 'r.', markersize=7, label='A')
    ax.plot(data.flow_rate, data.dp_2, 'b.', markersize=7, label='B')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 220)


    # polynomal fitting 
    x= data.flow_rate
    y1= data.dp_1
    y2= data.dp_2

    polyfit_y1 = np.polyfit(x,y1,3)
    p1 = np.poly1d(polyfit_y1)
    print("coeffs for cubic regression curve for f1: ")
    print(polyfit_y1)
    polyfit_y2 = np.polyfit(x,y2,3)
    p2 = np.poly1d(polyfit_y2)
    print("coeffs for cubic regression curve for f2: ")
    print(polyfit_y2)

    # finer discretization:
    x=np.linspace(0,max(data.flow_rate)*2, 100)
    ax.plot(x, p1(x), 'r-', linewidth=1, label=p1)
    ax.plot(x, p2(x), 'b-', linewidth=1, label=p2)

    # find intersection point:
    from intersect_function import intersection
    x,y = intersection(x, p1(x), x, p2(x))
    print("Intersection point: %0.4f %0.4f" % (x, y))
    ax.plot(x,y, '*k')

    plt.legend()
    plt.show()
