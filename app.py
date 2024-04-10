import streamlit as st
import pandas as pd

# Sidebar selection
df=pd.read_csv('data/match_data.csv')

with st.sidebar:
    selected_batsman = st.selectbox("Select Batsman:", df['striker'].unique(), key="batsman")
    selected_bowler = st.selectbox("Select Bowler:", df['bowler'].unique(), key="bowler")

# Filtering data
total_innings_between=len(df[(df['bowler']==selected_bowler) & (df['striker']==selected_batsman)].match_id.unique())
filtered_data = df[(df['striker'] == selected_batsman) & (df["bowler"] == selected_bowler)]
fours_against=len(filtered_data[filtered_data['runs_off_bat']==4])
sixes_against=len(filtered_data[filtered_data['runs_off_bat']==6])
runs = filtered_data['runs_off_bat'].sum()
balls=len(filtered_data)

# Calculating outs
out_types = ['stumped', 'lbw', 'caught', 'bowled', 'caught and bowled','hit wicket','obstructing the field']
outs = filtered_data[filtered_data['wicket_type'].isin(out_types)]
out_count = len(outs)

average = runs / out_count

# Formatting average to 1 decimal place
average_formatted = "{:.1f}".format(average)

strike_rate=(runs/balls)*100
strike_rate="{:.1f}".format(strike_rate)
# Displaying the information
st.title("IPL Stats")
st.title("Players Head to Head")
custom_css = """
<style>
.title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}
.stat {
    font-size: 18px;
    margin-bottom: 8px;
}
</style>
"""

# Display the information with custom styling
st.write(f'<div class="title">{selected_batsman} vs {selected_bowler}</div>', unsafe_allow_html=True)
st.write('<hr>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Innings:</b> {total_innings_between}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Runs Scored:</b> {runs}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Balls Faced:</b> {balls}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Outs:</b> {out_count}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Batting Average:</b> {average_formatted}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Strike Rate:</b> {strike_rate}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Sixes:</b> {sixes_against}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Fours:</b> {fours_against}</div>', unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

#################################################################################################################

st.title("Batsman Overall Stats")
total_balls_batsman=len(df[(df['striker']==selected_batsman) & (df['wides']!=1) & (df['wides']!=2) & (df['wides']!=3) & (df['wides']!=4) & (df['wides']!=5)])
total_innings_batsman=len(df[(df['striker']==selected_batsman)].match_id.unique())
total_runs_batsman=df[df['striker'] == selected_batsman]['runs_off_bat'].sum()
strike_rate_batsman=(total_runs_batsman/total_balls_batsman)*100
strike_rate_batsman="{:.1f}".format(strike_rate_batsman)
df1=df[df['striker'] == selected_batsman]
sixes=len(df1[df1['runs_off_bat']==6])
fours=len(df1[df1['runs_off_bat']==4])
unique_id=df1.match_id.unique()
fifty=0
thirty=0
hundred=0
zeros=0
highest=-1
for i in unique_id:
    xx=df1[df1['match_id']==i].runs_off_bat.sum()
    highest=max(highest,xx)
    if(xx>=50):
        fifty+=1
    if(xx>=30):
        thirty+=1
    if(xx==0):
        zeros+=1
    if(xx>=100):
        hundred+=1
out_types1 = ['retired out','run out','stumped', 'lbw', 'caught', 'bowled', 'caught and bowled','hit wicket','obstructing the field']
outs_batsman= df1[df1['wicket_type'].isin(out_types1)]
out_count = len(outs_batsman)
average_batsman=total_runs_batsman/out_count
average_batsman="{:.1f}".format(average_batsman)
st.write(f'<div class="title">{selected_batsman} Stats</div>', unsafe_allow_html=True)
st.write('<hr>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Innings:</b> {total_innings_batsman}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Runs Scored:</b> {total_runs_batsman}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Balls Faced:</b> {total_balls_batsman}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Total Not Outs:</b> {total_innings_batsman-out_count}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Batting Average:</b> {average_batsman}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Strike Rate:</b> {strike_rate_batsman}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Sixes:</b> {sixes}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Fours:</b> {fours}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Highest:</b> {highest}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>100+:</b> {hundred}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>50+:</b> {fifty}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>30+:</b> {thirty}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Zeros:</b> {zeros}</div>', unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

######################################################################################################################


st.title("Bowler Overall Stats")
df2=df[(df['bowler'] == selected_bowler) & (df['noballs']!=1) & (df['noballs']!=2)& (df['noballs']!=3)& (df['noballs']!=5) & (df['wides']!=1) & (df['wides']!=2) & (df['wides']!=3) & (df['wides']!=4) & (df['wides']!=5)]
no_of_balls=len(df2)
out_types = ['stumped', 'lbw', 'caught', 'bowled', 'caught and bowled','hit wicket','obstructing the field']
wickets=len(df2[df2['wicket_type'].isin(out_types)])
total_innings_bowler=len(df[(df['bowler']==selected_bowler)].match_id.unique())
total_runs_bowler=df2['runs_off_bat'].sum()+df2[df2['legbyes']==0]['extras'].sum()
economy=total_runs_bowler/(no_of_balls/6)
economy="{:.1f}".format(economy)
bowler_average=total_runs_bowler/wickets
bowler_average="{:.1f}".format(bowler_average)
strike_bowler=no_of_balls/wickets
strike_bowler="{:.1f}".format(strike_bowler)
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
st.write(f'<div class="title">{selected_bowler} Stats</div>', unsafe_allow_html=True)
st.write('<hr>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Innings:</b> {total_innings_bowler}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Balls bowled:</b> {no_of_balls}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Wickets taken:</b> {wickets}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Economy:</b> {economy}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Average:</b> {bowler_average}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Strike Rate:</b> {strike_bowler}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>5+:</b> {fifer}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>4+:</b> {fourfer}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>3+:</b> {threefer}</div>', unsafe_allow_html=True)
st.write(f'<div class="stat"><b>Best:</b> {highest_wickets}/{best}</div>', unsafe_allow_html=True)