import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------

st.set_page_config(
    page_title="International Baseball Signing Explorer",
    page_icon="⚾",
    layout="wide"
)

st.title("⚾ International Baseball Signing Explorer")
st.subheader("2025 International Signing Market Analysis")

st.write(
    "Explore signing bonus trends across 108 international players "
    "by country, position, and signing bonus tier."
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("international_players_v2.csv")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚾ Filters")
st.sidebar.write("Narrow the signing market below.")

country_options = ["All Countries"] + sorted(
    df["Country"].dropna().unique().tolist()
)

selected_country = st.sidebar.selectbox(
    "Country",
    country_options
)

position_options = ["All Positions"] + sorted(
    df["Position_Group"].dropna().unique().tolist()
)

selected_position = st.sidebar.selectbox(
    "Position Group",
    position_options
)

bonus_options = [
    "All Bonus Levels",
    "Under $500K",
    "$500K-$999K",
    "$1M-$1.99M",
    "$2M+"
]

selected_bonus = st.sidebar.selectbox(
    "Signing Bonus",
    bonus_options
)

# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()

if selected_country != "All Countries":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if selected_position != "All Positions":
    filtered_df = filtered_df[
        filtered_df["Position_Group"] == selected_position
    ]

if selected_bonus != "All Bonus Levels":
    filtered_df = filtered_df[
        filtered_df["Bonus_Tier"] == selected_bonus
    ]

# --------------------------------------------------
# MARKET OVERVIEW
# --------------------------------------------------

st.divider()
st.header("Market Overview")

player_count = len(filtered_df)
total_bonus = filtered_df["Signing_Bonus"].sum()

if player_count > 0:
    average_bonus = filtered_df["Signing_Bonus"].mean()
    median_bonus = filtered_df["Signing_Bonus"].median()
else:
    average_bonus = 0
    median_bonus = 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Players",
    f"{player_count:,}"
)

col2.metric(
    "Total Bonus Money",
    f"${total_bonus:,.0f}"
)

col3.metric(
    "Average Bonus",
    f"${average_bonus:,.0f}"
)

col4.metric(
    "Median Bonus",
    f"${median_bonus:,.0f}"
)

# --------------------------------------------------
# QUICK MARKET SNAPSHOT
# --------------------------------------------------

if player_count > 0:

    st.subheader("Quick Market Snapshot")

    top_signing = filtered_df.loc[
        filtered_df["Signing_Bonus"].idxmax()
    ]

    snapshot1, snapshot2, snapshot3 = st.columns(3)

    snapshot1.metric(
        "Largest Bonus",
        f"${top_signing['Signing_Bonus']:,.0f}"
    )

    snapshot2.metric(
        "Largest Bonus Player",
        top_signing["Player"]
    )

    snapshot3.metric(
        "Countries Represented",
        filtered_df["Country"].nunique()
    )

# --------------------------------------------------
# COUNTRY ANALYSIS
# --------------------------------------------------

st.divider()
st.header("🌎 Country Analysis")

country_summary = (
    filtered_df
    .groupby("Country")
    .agg(
        Players=("Player", "count"),
        Total_Bonus=("Signing_Bonus", "sum"),
        Average_Bonus=("Signing_Bonus", "mean"),
        Median_Bonus=("Signing_Bonus", "median")
    )
    .reset_index()
)

country_summary = country_summary.sort_values(
    "Total_Bonus",
    ascending=False
)

if not country_summary.empty:

    st.subheader("Total Signing Bonus Investment by Country")

    country_chart = country_summary.set_index(
        "Country"
    )["Total_Bonus"]

    st.bar_chart(country_chart)

    display_country = country_summary.copy()

    display_country["Total_Bonus"] = (
        display_country["Total_Bonus"]
        .map("${:,.0f}".format)
    )

    display_country["Average_Bonus"] = (
        display_country["Average_Bonus"]
        .map("${:,.0f}".format)
    )

    display_country["Median_Bonus"] = (
        display_country["Median_Bonus"]
        .map("${:,.0f}".format)
    )

    display_country.columns = [
        "Country",
        "Players",
        "Total Bonus",
        "Average Bonus",
        "Median Bonus"
    ]

    st.dataframe(
        display_country,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# POSITION ANALYSIS
# --------------------------------------------------

st.divider()
st.header("⚾ Position Analysis")

position_summary = (
    filtered_df
    .groupby("Position_Group")
    .agg(
        Players=("Player", "count"),
        Total_Bonus=("Signing_Bonus", "sum"),
        Average_Bonus=("Signing_Bonus", "mean"),
        Median_Bonus=("Signing_Bonus", "median")
    )
    .reset_index()
)

position_summary = position_summary.sort_values(
    "Average_Bonus",
    ascending=False
)

if not position_summary.empty:

    st.subheader("Average Signing Bonus by Position Group")

    position_chart = position_summary.set_index(
        "Position_Group"
    )["Average_Bonus"]

    st.bar_chart(position_chart)

    display_position = position_summary.copy()

    display_position["Total_Bonus"] = (
        display_position["Total_Bonus"]
        .map("${:,.0f}".format)
    )

    display_position["Average_Bonus"] = (
        display_position["Average_Bonus"]
        .map("${:,.0f}".format)
    )

    display_position["Median_Bonus"] = (
        display_position["Median_Bonus"]
        .map("${:,.0f}".format)
    )

    display_position.columns = [
        "Position Group",
        "Players",
        "Total Bonus",
        "Average Bonus",
        "Median Bonus"
    ]

    st.dataframe(
        display_position,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# BONUS DISTRIBUTION
# --------------------------------------------------

st.divider()
st.header("💰 Signing Bonus Distribution")

tier_order = [
    "Under $500K",
    "$500K-$999K",
    "$1M-$1.99M",
    "$2M+"
]

bonus_distribution = (
    filtered_df["Bonus_Tier"]
    .value_counts()
    .reindex(tier_order, fill_value=0)
)

st.bar_chart(bonus_distribution)

# --------------------------------------------------
# KEY INSIGHTS
# --------------------------------------------------

st.divider()
st.header("💡 Key Insights")

if player_count > 0:

    country_counts = (
        filtered_df["Country"]
        .value_counts()
    )

    largest_country = country_counts.index[0]
    largest_country_count = country_counts.iloc[0]

    country_average = (
        filtered_df
        .groupby("Country")["Signing_Bonus"]
        .mean()
        .sort_values(ascending=False)
    )

    highest_average_country = country_average.index[0]
    highest_average_country_bonus = country_average.iloc[0]

    position_average = (
        filtered_df
        .groupby("Position_Group")["Signing_Bonus"]
        .mean()
        .sort_values(ascending=False)
    )

    highest_position = position_average.index[0]
    highest_position_bonus = position_average.iloc[0]

    st.markdown(
        f"""
**Largest player group:** {largest_country} with
**{largest_country_count} players** in the selected sample.

**Highest average bonus by country:** {highest_average_country}
at approximately **${highest_average_country_bonus:,.0f} per player**.

**Highest average bonus by position group:** {highest_position}
at approximately **${highest_position_bonus:,.0f} per player**.

**Largest individual signing:** {top_signing['Player']},
a **{top_signing['Position']} from {top_signing['Country']}**,
at **${top_signing['Signing_Bonus']:,.0f}**.
        """
    )

# --------------------------------------------------
# PLAYER EXPLORER
# --------------------------------------------------

st.divider()
st.header("🔎 Player Explorer")

st.write(
    f"Showing **{player_count} players** matching the selected filters."
)

player_table = filtered_df[
    [
        "Player",
        "Position",
        "Position_Group",
        "Country",
        "Signing_Bonus",
        "Bonus_Tier"
    ]
].copy()

player_table = player_table.sort_values(
    "Signing_Bonus",
    ascending=False
)

player_table["Signing_Bonus"] = (
    player_table["Signing_Bonus"]
    .map("${:,.0f}".format)
)

player_table.columns = [
    "Player",
    "Position",
    "Position Group",
    "Country",
    "Signing Bonus",
    "Bonus Tier"
]

st.dataframe(
    player_table,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

st.divider()

with st.expander("📋 Project Methodology & Limitations"):

    st.markdown(
        """
### Objective

Analyze patterns in publicly available 2025 international
amateur signing bonus information.

### Process

1. Collected publicly available international signing information.
2. Parsed unstructured player information using Python.
3. Structured player names, positions, countries, and bonuses.
4. Removed duplicate records and checked missing values.
5. Grouped positions into broader baseball position categories.
6. Created signing bonus tiers.
7. Analyzed bonus investment by country and position.
8. Built an interactive Streamlit dashboard for exploration.

### Dataset

The project contains **108 player records** with usable signing
bonus information from the public source used for the analysis.

### Important Limitation

This is a sample of publicly available signing information and is
**not a complete record of every player signed during the 2025
international signing period**.

The analysis describes patterns within this dataset. Differences
between countries or positions do not establish that those factors
caused differences in signing bonuses.
        """
    )

st.caption(
    "International Baseball Strategy & Analytics Portfolio Project | 2025"
)