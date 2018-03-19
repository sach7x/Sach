

```python
# 3 Observable Traits
#PyMoli is predominantly played by Male users (81%)
#Majority of in-game purchases were made by the 20-24 year old cohort
#The 2 most popular items purchased were Betrayel Whisper of Greiving Widows, and Arcane Gem
```


```python
import pandas as pd
import os
import json

```


```python
json_path = os.path.join("output/purchase_data.json")
```


```python
game_df = pd.read_json(json_path)
game_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
game_df.count()
```




    Age          780
    Gender       780
    Item ID      780
    Item Name    780
    Price        780
    SN           780
    dtype: int64




```python
#total number of players
unique_players = game_df["SN"].unique()
len(unique_players)
unique_players_df = pd.DataFrame({"Total Players":[len(unique_players)]})
unique_players_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#total unique items, average price, number of purchases, total revenue
unique_items = game_df["Item ID"].unique()
len(unique_items)


```




    183




```python
#average price
avg_price = "$" + str(game_df["Price"].mean())
avg_price
```




    '$2.931192307692303'




```python
#number of purchases
total_purchases = game_df["Item ID"].count()
total_purchases

```




    780




```python
#total revenue
revenue = game_df["Price"].sum()
revenue = "$" + str(revenue)
revenue
```




    '$2286.33'




```python
#must reorder and adjust decimal places
purchasing_analysis_df = pd.DataFrame({"Number of Unique Items" : [len(unique_items)],
                                      "Average Purchase Price" : [avg_price],
                                      "Total Number of Purchases" : [total_purchases],
                                      "Total Revenue" : [revenue]})
purchasing_analysis_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.931192307692303</td>
      <td>183</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchasing_analysis_df = purchasing_analysis_df[["Number of Unique Items", "Average Purchase Price", "Total Number of Purchases", "Total Revenue"]]
purchasing_analysis_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.931192307692303</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
male_demographics = game_df.loc[game_df['Gender'] == 'Male']
male_demographics_count = male_demographics['SN'].unique()
male_demographics_num = len(male_demographics_count)
male_demographics_num
male_percent = (len(male_demographics_count)/total_players)*100
male_percent
```




    81.15183246073299




```python
female_demographics = game_df.loc[game_df['Gender'] == 'Female']
female_demographics_count = female_demographics['SN'].unique()
female_demographics_num = len(female_demographics_count)
female_demographics_num
female_percent = (len(female_demographics_count)/total_players)*100
female_percent
```




    17.452006980802793




```python
other_demographics = game_df.loc[game_df['Gender'] == 'Other / Non-Disclosed']
other_demographics_count = other_demographics['SN'].unique()
other_demographics_num = len(other_demographics_count)
other_demographics_num
other_percent = (len(other_demographics_count)/total_players)*100
other_percent
```




    1.3961605584642234




```python
total_demographics = demographic_count.sum()
total_demographics
total_players = len(male_demographics_count) + len(female_demographics_count) + len(other_demographics_count)
total_players

```




    573




```python
#Gender Demographics DF
genderDemographics_df = pd.DataFrame({"Percentage of Players" : [male_percentage, female_percentage, other_percentage],
                                      "Total count": [male_demographics_num, female_demographics_num, other_demographics_num]
                               })
genderDemographics_df_rename = genderDemographics_df.rename(index={0: 'Male', 1:'Female', 2:'Other'})
genderDemographics_df_rename
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.153846</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.435897</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>1.410256</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing analysis
# Purchase Count
#purchase_count = game_df['Gender'].value_counts()
#purchase_count_df = pd.DataFrame(purchase_count)
#purchase_count_df
male_demographics_purchase = len(male_demographics)
male_demographics_purchase
female_demographics_purchase = len(female_demographics)
female_demographics_purchase
other_demographics_purchase = len(other_demographics)
other_demographics_purchase
# Average purchase price
avgPrice_male = male_demographics["Price"].mean()
avgPrice_male
avgPrice_female = female_demographics["Price"].mean()
avgPrice_female
avgPrice_other = other_demographics["Price"].mean()
avgPrice_other
# Total purchase value
totalValue_male = male_demographics['Price'].sum()
totalValue_male
totalValue_female = female_demographics["Price"].sum()
totalValue_female
totalValue_other = other_demographics["Price"].sum()
totalValue_other
# Normalized Totals
normTotal_male = totalValue_male/len(male_demographics_count)
normTotal_male
normTotal_female = totalValue_female/len(female_demographics_count)
normTotal_female
normTotal_other = totalValue_other/len(female_demographics_count)
normTotal_other
```




    0.35739999999999994




```python
#Purchase analysis (gender) DF
purchaseAnalysis_df = pd.DataFrame({"Normalized Totals": [normTotal_male, normTotal_female, normTotal_other],
                                   "Total Purchase Value": [totalValue_male, totalValue_female, totalValue_other],
                                   "Average Purchase Price": [avgPrice_male, avgPrice_female, avgPrice_other],
                                    "Purchase Count": [male_demographics_purchase, female_demographics_purchase, other_demographics_purchase] 
                                   })
purchaseAnalysis_df = purchaseAnalysis_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
purchaseAnalysis_df_rename = purchaseAnalysis_df.rename(index={0: 'Male', 1:'Female', 2:'Other'})
purchaseAnalysis_df_rename

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>2.950521</td>
      <td>1867.68</td>
      <td>4.016516</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>2.815515</td>
      <td>382.91</td>
      <td>3.829100</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>11</td>
      <td>3.249091</td>
      <td>35.74</td>
      <td>0.357400</td>
    </tr>
  </tbody>
</table>
</div>




```python
age_max = game_df["Age"].max()
age_max
```




    45




```python
age_min = game_df["Age"].min()
age_min
```




    7




```python
#age demographics
bins = [0,9.99,14.99,19.99,24.99,29.99,34.99,39.99,120]
group_names = ["<10", "10-14","15-19", "20-24","25-29","30-34","35-39","40+"]
ages_grouped = pd.cut(game_df["Age"], bins, labels=group_names)
game_df["Age Group"] = pd.cut(game_df["Age"], bins, labels=group_names)
game_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
age_grouped = game_df.groupby(["Age Group"])

age_group_df = pd.DataFrame({"Purchase Count":age_grouped["Age Group"].count(),
                            "Average Purchase Price":age_grouped["Price"].mean(),
                            "Total Purchase Value": age_grouped["Price"].sum() ,
                            "Normalized Totals": (age_grouped["Price"].sum()/len(unique_players))})
age_group_df = age_group_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
age_group_df



```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>0.145654</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>0.169197</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>0.674380</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>1.708150</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>0.646300</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>0.344241</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>0.208377</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>0.093805</td>
    </tr>
  </tbody>
</table>
</div>




```python
#top spenders alternate method
big_spender2 = game_df.groupby(['SN'])
big_spender2.head(10)

big_spender2_df = pd.DataFrame({"Purchase Count":big_spender2['Price'].count(),
                                "Average Purchase Price":big_spender2['Price'].mean(),
                                "Total Purchase Value":big_spender2['Price'].sum()})


big_spender2_df = big_spender2_df.sort_values("Total Purchase Value",ascending=False)
big_spender2_df = big_spender2_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
big_spender2_df.head()

                                
                                
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.412000</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.390000</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.185000</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.243333</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.860000</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#popular items alternate method
popular_items2 = game_df.groupby(['Item ID', 'Item Name'])
popular_items2.head(10)

popular_items2_df = pd.DataFrame({"Purchase Count":popular_items2['Price'].count(),
                                "Item Price":(popular_items2['Price'].sum()/popular_items2['Price'].count()),
                                "Total Purchase Value":popular_items2['Price'].sum()})

popular_items2_df = popular_items2_df.sort_values("Purchase Count", ascending=False)
popular_items2_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#top 5 profitable items

profitable_items_df = popular_items2_df.sort_values("Total Purchase Value", ascending=False)
profitable_items_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>4.14</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>4.25</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>4.95</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>4.87</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>3.61</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


