# THPT Exam Score Scraper

## Project Overview
This project is a multithreaded Python application designed to collect and save the scores of the THPT (National High School Exam) from the VnExpress website. The program is optimized to fetch data concurrently, significantly reducing the time needed for data collection.

## Features
- Collects exam scores for all subjects across all provinces and cities in Vietnam.
- Utilizes multithreading for efficient data scraping.
- Saves data to Excel files (`.xlsx`) for easy data manipulation and analysis.

## Technologies Used
- **Python**: Core language for development.
- **OpenPyXL**: For creating and writing to Excel files.
- **BeautifulSoup**: For parsing HTML data.
- **Requests**: To make HTTP requests to the VnExpress website.
- **Threading**: For concurrent data scraping.

## Project Structure
```
📁 data/                  # Directory to store collected Excel files
📄 main.py                # Main script for execution
📄 province.txt           # List of provinces and their codes
📄 README.md              # Project documentation
```

## How It Works
1. Loads province codes from `province.txt`.
2. Distributes the data scraping tasks across multiple threads:
   - Two dedicated threads for Hanoi and Ho Chi Minh City due to their larger datasets.
   - Remaining provinces are evenly split among the rest of the threads.
3. Fetches and parses exam scores from the VnExpress website.
4. Writes the collected data to Excel files categorized by province.

## Setup Instructions
1. Ensure Python is installed (version 3.6+).
2. Install the required packages:
```bash
pip install requests beautifulsoup4 openpyxl
```
3. Place the `province.txt` file in the same directory as the script.
4. Run the script:
```bash
python main.py
```

## Notes
- Ensure the website URL format is consistent with the one used in the code.
- If the `data/` directory does not exist, it will be created automatically.

## Future Improvements
- Implement error handling for network issues.
- Add functionality to resume failed data scraping sessions.

## License
This project is for educational and non-commercial use only.

