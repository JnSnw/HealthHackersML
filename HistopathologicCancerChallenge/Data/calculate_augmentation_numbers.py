import pandas as pd
df_targets = pd.DataFrame({'data': y, 'label':y})    

group_num = 1
df_targets["group"] = -1

for idx, item in df_targets.iterrows(): 
    
    df_targets.loc[idx, "group"] = group_num
    if (idx + 1) % 100 == 0:
        group_num = group_num + 1


df_targets_grouped = df_targets.groupby('group')

for num, df_batches in df_targets_grouped:
    
    df_labels = df_batches.groupby('label').count()
    
    num_positive = df_labels.query('label == 1').reset_index().loc[0, 'data']
    num_negative = df_labels.query('label == 0').reset_index().loc[0, 'data']

    if num_negative > num_positive:
        print('Batch {}: Create {} positive augmentations'.format(num, num_negative - num_positive))
    elif num_positive > num_negative:
        print('Batch {}: Create {} positive augmentations'.format(num, num_positive - num_negative))
    else:
        print('Batch {}: balanced!'.format(num))
        
## [2019-02-08] I'm going to complete it at the beginning of next week        
