import pandas as pd

def convert_data(data):
    df = pd.DataFrame(data)    # create DataFrame

    # Conversion data types
    df['id'] = df['id'].astype(int)   # convert 'id' values to integers
    df['xG'] = df['xG'].astype(float) # convert 'xG' values to floats
    df['goals'] = df['goals'].astype(int)
    df['shots'] = df['shots'].astype(int)

    # Data reduction
    mini_df = df[['id', 'player_name', 'games', 'goals', 'xG']]
    final_df = mini_df.loc[(mini_df['xG'] >= 2) | (mini_df['goals'] >= 2)]

    # Calclulating difference between xG and goals
    final_df['xG_diff'] = final_df['xG'] - final_df['goals']
    
    # Sort values by xG difference
    final_df = final_df.sort_values('xG_diff', ascending = False)

    return final_df