import requests
from bs4 import BeautifulSoup

def main():
    try:
        response = requests.get('https://download.vn/danh-sach-ma-tinh-ma-huyen-ma-xa-thi-thpt-quoc-gia-32895')
        soup = BeautifulSoup(response.content, 'html.parser')

        data = soup.find_all('h3')[:63]
        data = [d.get_text(strip=True) for d in data]

        # Convert data to dictionary
        province = {}
        for item in data:
            code = item[9:11]
            name = item[14:]
            
            province[code] = name

        # Write to file
        with open('province.txt', 'w', encoding='utf-8') as file:
            file.write(str(province))

    except Exception as e:
        print('Unexpected error:', e)

if __name__ == '__main__':
    main()