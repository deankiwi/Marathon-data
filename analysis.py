
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils.formate_data import hours_to_hh_mm


years = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2021,
    2022,
    2023,
    2024,
]
data = []

for year in years:
    file_path = f"data/london_marathon_{year}_mens.csv"
    data.append(pd.read_csv(file_path))


for df in data:
    df["finish"] = pd.to_timedelta(df["finish"])
    df.sort_values(by="finish", inplace=True)
    df["time_seconds"] = df["finish"].dt.total_seconds()
    df["time_hours"] = df["finish"].dt.total_seconds() / 3600
    total_people = len(df)
    df["percentage_completed"] = (df.index + 1) / total_people * 100


# Assuming 'years' is a list of years corresponding to each dataframe in 'data'
percentiles = [10, 50]
colors = ["#29a3a3", "#cccc00"]
year_percentile_times = {}

for year, df in zip(years, data):
    df_sorted = df.sort_values(by="time_hours")
    percentile_times = np.percentile(df_sorted["time_hours"], percentiles)
    year_percentile_times[year] = percentile_times

# Plotting
plt.figure(figsize=(5, 5))

for year, times in year_percentile_times.items():
    for percentile, time, color in zip(percentiles, times, colors):
        plt.plot(
            year,
            time,
            marker="o",
            markersize=3,  # Adjust the marker size here
            linestyle="",
            color=color,
            label=f"{year} - {percentile}%",
        )

# Connect 50% dots with lines
for i in range(len(years) - 1):
    plt.plot(
        [years[i], years[i + 1]],
        [year_percentile_times[years[i]][1], year_percentile_times[years[i + 1]][1]],
        color=colors[1],
        linestyle="-",
        linewidth=1.5,  # Adjust the line width here
    )
# Connect 10% dots with lines
for i in range(len(years) - 1):
    plt.plot(
        [years[i], years[i + 1]],
        [year_percentile_times[years[i]][0], year_percentile_times[years[i + 1]][0]],
        color=colors[0],
        linestyle="-",
        linewidth=1.5,  # Adjust the line width here
    )


print(hours_to_hh_mm(year_percentile_times[2010][0]))
plt.annotate(
    f"{hours_to_hh_mm(year_percentile_times[2010][0])}\n",
    xy=(2010, year_percentile_times[2010][0]),
    xytext=(2010 -3, year_percentile_times[2010][0] + 0.03),
    color=colors[0],
    arrowprops=dict(arrowstyle='->', color=colors[0], lw=0.3),
    size=6,
)
plt.annotate(
    f"{hours_to_hh_mm(year_percentile_times[2010][1])}",
    xy=(2010, year_percentile_times[2010][1]),
    xytext=(2010 -3, year_percentile_times[2010][1] - 0.15),
    color=colors[1],
    arrowprops=dict(arrowstyle='->', color=colors[1], lw=0.3),
    size=6,
)
plt.annotate(
    f"Top 10% finishing time\n{hours_to_hh_mm(year_percentile_times[2024][0])}",
    xy=(2024, year_percentile_times[2024][0]),
    xytext=(2024 + 0.5, year_percentile_times[2024][0]+0.03 ),
    color=colors[0],
    arrowprops=dict(arrowstyle='->', color=colors[0], lw=0.3),
    size=6,
)
plt.annotate(
    f"Median finishing time\n{hours_to_hh_mm(year_percentile_times[2024][1])}",
    xy=(2024, year_percentile_times[2024][1]),
    xytext=(2024 + 0.5, year_percentile_times[2024][1]),
    color=colors[1],
    arrowprops=dict(arrowstyle='->', color=colors[1], lw=0.3),
    size=6,
)
plt.annotate(
    f"2018 heat wave",
    xy=(2018, year_percentile_times[2018][0]),
    xytext=(2018 + 0.5, year_percentile_times[2018][0]+0.13 ),
    color='black',
    arrowprops=dict(arrowstyle='->', color='black', lw=0.3),
    size=6,
)



plt.yticks(
    np.arange(3, 4.5, 1), [f"{int(tick)} hours" for tick in np.arange(3, 4.5, 1)],
    size=6
)
plt.xticks(np.arange(2010, 2026, 4), size=6)

# Get the current axis
ax = plt.gca()

# Set color of both major and minor ticks to grey
ax.tick_params(axis="x", colors="lightgrey")
ax.tick_params(axis="y", colors="lightgrey")

# plt.xlabel("Year")
plt.title( "London Fastest Marathon,\nMens Finishing Time",size=18, fontweight="bold", fontname="bodoni 72", loc="left")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)

plt.text(2008, 2.7, 'Data: results.tcslondonmarathon.com | Chart by Dean Welch', fontsize=4, color='gray', ha='left', va='top')
plt.xlim(2009, 2024.4)

plt.subplots_adjust(left=0.2, right=0.8, top=0.6, bottom=0.2)

plt.savefig('London_Marathon_mens.png', dpi=300, bbox_inches='tight')

plt.show()


