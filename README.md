# Lottery Draw Analysis and Prediction System

A sophisticated Python-based system for analyzing lottery draw patterns and predicting potential future outcomes using machine learning techniques.

## Overview

This project provides a comprehensive suite of tools for analyzing historical lottery draw data, identifying patterns, and making predictions using machine learning. It combines data processing, statistical analysis, and visualization techniques to provide insights into lottery number distributions and patterns.

## Features

### Data Collection and Processing
- Automated web scraping of lottery draw data
- ZIP file download and extraction
- CSV processing with focus on draw numbers and dates
- Efficient data preparation and cleaning

### Pattern Analysis
- **Color-Coded Range Analysis**
  - Green (1-10): Low numbers
  - Yellow (11-20): Low-mid numbers
  - Red (21-30): Mid numbers
  - Purple (31-40): Mid-high numbers
  - Blue (41-49): High numbers

### Visualization Tools
- Interactive heatmaps showing number frequency
- Pattern visualization with color-coded rectangles
- Customizable time range analysis
- Historical pattern display

### Machine Learning Predictions
- Pattern-based prediction using Decision Tree Classifier
- Model persistence with joblib
- Accuracy evaluation and reporting
- Next draw pattern prediction

## Technical Implementation

### Core Components
- **Data Processing**: Pandas for data manipulation
- **Visualization**: Matplotlib and Seaborn for data visualization
- **Machine Learning**: Scikit-learn for pattern prediction
- **Web Scraping**: Requests library for data collection

### Key Classes
- `PatternPlotter`: Handles visualization of number patterns
- `PatternAnalyzer`: Manages pattern detection and analysis

## Development Roadmap

### Statistical Analysis Implementation
- **Distribution Analysis**
  - Odd/Even number distribution (Current record: 3 odd + 2 even appears 814 times)
  - Low/High number split analysis (3 low, 2 high appears 529 times)
  - Consecutive number patterns (0 consecutive: 1144 times, 1 consecutive: 311 times)

- **Pattern Recognition**
  - Number range occurrence tracking by year
  - Probability calculation system (Reference: lottometrix.com methodology)
  - Pattern frequency analysis with historical context

- **Frequency Analysis**
  - Hot numbers (highest occurrence in selected range)
  - Cold numbers (lowest occurrence in selected range)
  - Overdue numbers (numbers not drawn for extended periods)
  - Number pair frequency tracking (e.g., "2,14" appears 5 times)

- **Advanced Metrics**
  - Sum frequency analysis (e.g., total sum 132 appears 56 times)
  - Number sequence regularity detection (fixed increments: +7, +8, etc.)
  - Following/Non-following number patterns
  - Average number distribution analysis
  - Enhanced heat map visualization

### AI/ML Enhancement Plan
- **Dual Analysis System**
  - Probability-based analysis component
  - Historical pattern analysis component
  - Weighted scoring system (history weight < probability weight)

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- requests

## Getting Started

1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Open `Lottery.ipynb` to start analysis

## Note

This project is for educational and research purposes only. It demonstrates statistical analysis and machine learning techniques but does not guarantee any lottery outcomes. Please use responsibly and be aware of your local gambling laws and regulations.

## License

MIT License - See LICENSE file for details