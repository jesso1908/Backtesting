import backtrader as bt 

def printTradeAnalysis(analyzer):
    '''
    Function to print the Technical Analysis results in a nice format.
    '''
    #Get the results we are interested in
    total_open = analyzer.total.open
    total_closed = analyzer.total.closed
    total_won = analyzer.won.total
    total_lost = analyzer.lost.total
    win_streak = analyzer.streak.won.longest
    lose_streak = analyzer.streak.lost.longest
    pnl_net = round(analyzer.pnl.net.total,2)
    strike_rate = (total_won / total_closed) * 100
    average_won=analyzer.won.pnl.average
    average_lost=analyzer.lost.pnl.average
    #Designate the rows
    h1 = ['Total Open', 'Total Closed', 'Total Won', 'Total Lost','average_won']
    h2 = ['Strike Rate','Win Streak', 'Losing Streak', 'PnL Net','average_lost']
    r1 = [total_open, total_closed,total_won,total_lost,average_won]
    r2 = [strike_rate, win_streak, lose_streak, pnl_net,average_lost]
    #Check which set of headers is the longest.
    if len(h1) > len(h2):
        header_length = len(h1)
    else:
        header_length = len(h2)
    #Print the rows
    print_list = [h1,r1,h2,r2]
    row_format ="{:<15}" * (header_length + 1)
    print("Trade Analysis Results:")
    for row in print_list:
        print(row_format.format('',*row))

def printSQN(analyzer):
    sqn = round(analyzer.sqn,2)
    print('SQN: {}'.format(sqn))

