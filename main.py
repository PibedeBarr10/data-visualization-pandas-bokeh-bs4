from project.web_scraping import get_data
from project.data_processing import convert_data
from project.visualization import plot

def main():
    url = 'https://understat.com/main/getPlayersStats/'

    # Data download
    json_data = get_data(url)

    # Data processing
    df = convert_data(json_data['response']['players'])

    # Data visualization
    plot(df)

main()