# International Baseball Signing Explorer #

An interactive analysis of the 2025 international amateur signing market, built to explore how publicly reported signing bonuses vary across countries and position groups.

## Live Dashboard

https://international-baseball-signing-explorer-gls4bn9rmmthpd6j53gojv.streamlit.app/

## Project Objective

The goal of this project was to take publicly available international signing information, convert it into a structured dataset, validate and clean the data, and build an interactive tool that makes signing-market trends easier to explore.

The dashboard allows users to filter players by country, position group, and signing bonus tier while automatically updating market summaries and player-level results.

## Dataset

The final dataset contains 108 international players with usable publicly reported signing bonus information from the 2025 signing period.

The analysis includes:

- Player name
- Country
- Position
- Position group
- Signing bonus
- Signing bonus tier

## Workflow

1. Collected publicly available 2025 international signing information.
2. Parsed unstructured player information into structured records using Python.
3. Cleaned and validated player names, countries, positions, and signing bonuses.
4. Checked for missing values and duplicate records.
5. Grouped individual positions into broader baseball position categories.
6. Created signing bonus tiers for market segmentation.
7. Analyzed bonus investment by country and position.
8. Built an interactive Streamlit dashboard for self-service exploration.

## Key Findings

- The sample contains 108 players and approximately $62.3 million in reported signing bonuses.
- The Dominican Republic represents the largest player group in the dataset with 60 players.
- Cuba has the highest average signing bonus in the sample at approximately $1.10 million per player, although the Cuban sample contains only eight players.
- Outfielders have the highest average bonus among the broad position groups at approximately $622,000.
- The largest individual bonus in the dataset is Diego Tornes, an outfielder from Cuba, at $2,497,500.

## Tools

- Python
- pandas
- Streamlit
- GitHub

## Limitations

This dataset is a sample of publicly available signing information and is not a complete record of every player signed during the 2025 international signing period.

Results describe patterns within this dataset and should not be interpreted as evidence that a player's country or position caused differences in signing bonus amounts.
