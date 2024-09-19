# DeltaViz

**DeltaViz** is a Python-based data visualization tool designed to analyze and visualize changes between software releases. The project provides visual insights into changes in record counts and percentage differences across various data tables between two releases.

## Features

- **Bar Plot of Changes in Number of Records**: Visualizes the absolute change in record counts for each data table.
- **Bar Plot of Percentage Change**: Displays the percentage change in record counts for each data table.
- **Scatter Plot of Old vs New Record Counts**: Compares old and new record counts to identify trends and discrepancies.

## Technologies Used

- **Python**: Programming language for data processing and visualization.
- **Pandas**: Library for data manipulation and analysis.
- **Matplotlib**: Library for creating static, interactive, and animated visualizations.
- **Seaborn**: High-level interface for attractive statistical graphics.

## Installation

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/deltaviz.git
   cd deltaviz
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   ```

   - **On Windows:**

     ```bash
     .\env\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Data:**

   Ensure your data is in a format similar to the example provided in the script. Modify the `data` dictionary in `main.py` as needed.

2. **Run the Script:**

   Execute the script to generate plots:

   ```bash
   python main.py
   ```

   The generated plots will be saved as PNG files in the plots directory (`bar-plot1.png`, `bar-plot2.png`, `scatter-plot.png`).

3. **View Results:**

   Check the saved PNG files to view the visualizations.

## Contributing

If you have suggestions or improvements, please contribute by creating a pull request or opening an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Seaborn** for its high-level interface for drawing attractive statistical graphics.
- **Matplotlib** for its versatility in creating various types of plots.

