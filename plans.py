from playwright.sync_api import sync_playwright
import time

def scrape_plans():
    
    plans = [
        "Jakarta" # ganti jika ingin mengubah asal
    ]
    
    
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page_url = 'https://www.traveloka.com/id-id/tiket-pesawat'
        page.goto(page_url)
        
        
        for plan in plans:
            asal = page.get_by_test_id("airport-input-departure")
            asal.wait_for()
            asal.click
            asal.fill(plan)
            cekAsal = page.get_by_text("Soekarno Hatta International Airport", exact=True) # Ganti sesuai Value
            cekAsal.click()
            
            
            tujuan = page.get_by_test_id("airport-input-destination")
            tujuan.wait_for()
            tujuan.click
            tujuan.fill("Solo")
            cekTujuan = page.get_by_text("Adi Soemarmo", exact=True) # Ganti sesuai Value
            cekTujuan.click()
  
            
            tanggal = page.get_by_test_id('departure-date-input')
            tanggal.click()
            calendarTest = page.get_by_test_id('date-cell-27-6-2024').nth(0) # Format Date (date-cell-dd-m-yyyy)
            calendarTest.click()
            
            submitButton = page.get_by_test_id('desktop-default-search-button')
            submitButton.click()
            
            # page.wait_for_selector("flight-inventory-card-container")
             
            listTicketPlans = page.locator('//*[@id="FLIGHT_SEARCH_RESULT_CONTENT"]/div[6]/div[3]/div/div')
            # print("Pemilihan elemen listTicketPlans:", listTicketPlans)  # Cetak informasi pemilihan elemen
            listTicketPlans.wait_for()
            
            time.sleep(10)
            
            listTicket = page.locator('//*[@id="FLIGHT_SEARCH_RESULT_CONTENT"]/div[6]/div[3]/div/div/div[*]').all()
            
            
            for ticket in listTicket:
                 plansName = ticket.locator('//*[@id="FLIGHT_SEARCH_RESULT_CONTENT"]/div[6]/div[3]/div/div/div[*]/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div').inner_text()
                 print("Nama Pesawat : ", plansName)
                
            #     plansClass = ticket.locator().inner_text()
            #     print("Kelas : ", plansClass)
            
            #     plansType = "Pesawat"
            #     print("Jenis Kendaraan : ", plansType)
                
            #     plansOrigin = ticket.locator().inner_text()
            #     print("Asal : ", plansOrigin)
                
            #     plansDestination = ticket.locator().inner_text()
            #     print("Tujuan : ", plansDestination)
                
            #     plansDescription = ticket.locator().inner_text()
            #     print("Keterangan : ", plansDescription)
                
            #     plansDeparature = ticket.locator().inner_text()
            #     print("Jam Berangkat : ", plansDeparature)
                
            #     plansArrival = ticket.locator().inner_text()
            #     print("Jam Kedatangan : ", plansArrival)
                
            #     plansDuration = ticket.locator().inner_text()
            #     print("Durasi : ", plansDuration)
                
            #     plansPrice = ticket.locator().inner_text()
            #     print("Harga : ", plansPrice)
                
            #     plansDate = "28 Juni 2024"
            #     print("Tanggal : ", plansDate)
                
            #     plansCity = "-"
            #     print("Kota tujuan : ", plansCity)
                
        browser.close()
                
               
                
        