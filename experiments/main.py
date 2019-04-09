import matplotlib
import pandas as pd
import sys


def main(df):
    print(df)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:")
        print("  %s file" % sys.argv[0])
        sys.exit(1)

    source = sys.argv[1]
    df = pd.read_csv(source, sep='\s+', header=None)

    main(df)
