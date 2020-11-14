def maxAge(candles_count,candles):
    max_age=candles[0]
    for i in range(candles_count):
            if (candles[i]>max_age):
                max_age=candles[i]
    return max_age
    
    
def countCandles(candles_count,candles,max_age):
    count=0
    for i in range(candles_count):
    #i is loop incrementor
        if (candles[i]==max_age):
            count=count+1
    return count



candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
max_age=maxAge(candles_count,candles)
count_candle=countCandles(candles_count,candles,max_age)
print(count_candle)
