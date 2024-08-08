from Hotels import scrape_hotels
from trains import scrape_kereta
from plans import scrape_plans
from plansB import scrape_plansb
from bus import bus_scrape
from busT import Bus

def main():
    # print("\nScraping data Hotel dari Traveloka....")
    # scrape_hotels()
    
    print("\nScraping data Kereta dari Traveloka....")
    scrape_kereta()
    
    # print("\nScraping data Pesawat dari Traveloka....")
    # scrape_plansb()
    
    # print("\nScraping data Kereta dari Traveloka....")
    # Bus()
    
    
if __name__ == '__main__':
    main()