import matplotlib.pyplot as plt
import pandas as pd


def read_price_history() -> pd.DataFrame:
    df = pd.read_csv('ogzd.uk.csv')

    # df = df.loc[1420:1525, ['CLOSE']]
    # df = df.loc[1420:1625, ['CLOSE']]
    df = df.loc[:, ['CLOSE']]

    df.reset_index(level=0, inplace=True)
    df.columns = ['ds', 'y']
    return df


def calculate_ema_signal(df: pd.DataFrame):
    df['ema_fast'] = df.y.ewm(span=12 + 5, adjust=False).mean()
    df['ema_slow'] = df.y.ewm(span=26 + 10, adjust=False).mean()
    df['ema_diff'] = df.ema_fast - df.ema_slow
    df['ema_signal'] = df.ema_diff.ewm(span=9, adjust=False).mean()


def trade(df: pd.DataFrame):
    fee = 0.02
    profit = 0.0
    count = 0
    last_signal = None
    init_price = None
    last_price = None  # last exchange price
    df['profit'] = 0.0
    for i, signal in enumerate(df.ema_signal):
        price = df.y[i]
        if signal != 0:
            if signal > 0 and last_signal < 0:  # buy signal
                count = count + 1
                if last_price:
                    profit += last_price - price - fee
                else:
                    init_price = price
                last_price = price
            elif signal < 0 and last_signal > 0:  # sell signal
                count = count + 1
                if last_price:
                    profit += price - last_price - fee
                else:
                    init_price = price
                last_price = price
        last_signal = signal
        df.loc[i, 'profit'] = profit

    print(f'pocket: init: {init_price} final: {profit}')
    print(f'count: {count}')


def display(df: pd.DataFrame):
    plt.plot(df.ds, df.profit, label='Profit', color='BLUE')
    plt.plot(df.ds, df.y, label='GAZ', color='PINK')
    plt.plot(df.ds, df.ema_fast, label='EXP12', color='GREEN')
    plt.plot(df.ds, df.ema_slow, label='EXP26', color='RED')
    plt.plot(df.ds, df.ema_signal, label='EXP9', color='BLACK')
    plt.legend(loc='upper left')
    plt.grid()
    plt.tight_layout()
    plt.show()


def main():
    df = read_price_history()
    calculate_ema_signal(df)
    trade(df)
    display(df)


if __name__ == '__main__':
    main()
