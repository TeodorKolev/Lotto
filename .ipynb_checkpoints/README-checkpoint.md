### Functionality Overview (from Lottery-checkpoint.ipynb)

This notebook automates the process of downloading, preparing, analyzing, and predicting lottery draw data:

- **Web Scraping & Data Preparation**: Downloads lottery draw data as a ZIP file, extracts it, and loads CSV files starting with "lotto_". It processes columns like 'boule_1' to 'boule_5', 'numero_chance', and the draw date.
- **Data Analysis**:
  - Generates heatmaps showing the frequency of drawn numbers over customizable ranges.
  - Categorizes numbers into color-coded ranges (e.g., 1-10: green, 11-20: yellow, etc.) and analyzes the occurrence of these patterns.
  - Counts and visualizes unique draw patterns and their frequencies.
- **Visualization**:
  - Provides color-coded pattern visualizations for recent draws.
  - Displays a legend for color categories.
- **AI/ML Prediction**:
  - Encodes draw patterns numerically and uses a Decision Tree Classifier to predict the pattern of the next draw.
  - Loads a pre-trained model (`pattern-oracle.joblib`), evaluates its accuracy, and visualizes the predicted pattern for the next draw.

---

### TODO Analysis:
* Odd / Even - (3 odd + 2 even - 814 times)
* Define patterns: (1-9 - blue, 10-19 - yellow, etc) occurencies (by year) count and PROBABILITY https://lottometrix.com/members/analysis-euromillions.php
* Top Hot - most occurencies in row range
* Top Cold - less occurencies on row range
* Overdue - Number which isn't drawn for a long time (show be beyond range)
* Pairs and frequency (2,14 - 5 times)
* Sum and frequency (sum of all numbers: 132 - 56 times)
* Low / High - split on 24(or 25) occurencies - (3 low, 2 high - 529 times)
* Consecutives (0 - 1144 times, 1 - 311 times)
* Regularity (each number is + 7) or (+7 +8 + 9 etc)
* Following numbers
* Non following numbers
* Average numbers
* Heat map chart

### TODO AI:
* Split analysis on two groups: probability and history. Set each of them value. History value should be lesser than prob one