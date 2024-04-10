import pandas as pd
df = pd.read_csv("data/match_data.csv")
selected_batsman="V Kohli"
selected_bowler="A Nehra"
df2=df[df['bowler'] == selected_bowler]
no_of_balls=len(df2)
out_types = ['stumped', 'lbw', 'caught', 'bowled', 'caught and bowled','hit wicket','obstructing the field']
wickets=len(df2[df2['wicket_type'].isin(out_types)])
df3=df2[df2['wicket_type'].isin(out_types)]
unibowler=df3.match_id.unique()
fifer=0
fourfer=0
threefer=0
highest_wickets=-1
best=0
for i in unibowler:
    yy=len(df3[df3['match_id']==i])
    zz=df2[df2['match_id']==i]['runs_off_bat'].sum()+df2[(df2['legbyes']==0) & (df2['match_id']==i)]['extras'].sum()
    if(highest_wickets<=yy):
        highest_wickets=max(highest_wickets,yy)
        best=zz
    if(yy>=5):
        fifer+=1
    if(yy>=3):
        threefer+=1
    if(yy>=4):
        fourfer+=1
print(fifer,fourfer,threefer,highest_wickets,best)

total_innings_bowler=len(df[(df['striker']==selected_bowler)].match_id.unique())
total_runs_bowler=df2['runs_off_bat'].sum()+df2[(df2['legbyes']==0)]['extras'].sum()
total_innings_between=len(df[(df['bowler']==selected_bowler) & (df['striker']==selected_batsman)].match_id.unique())
print(total_innings_between)
