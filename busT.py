from playwright.sync_api import sync_playwright
import time
import mysql.connector
import re

def Bus():
    # # Koneksi ke database MySQL
    # try:
    #     conn = mysql.connector.connect(
    #         host="127.0.0.1",
    #         user="root",
    #         password="",  # ganti dengan password MySQL Anda
    #         database="tripplaner"
    #     )
    #     cursor = conn.cursor()
    # except Exception as e:
    #     print(f"Error connecting to MySQL: {e}")
    #     return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page_url = 'https://www.tiket.com/bus-travel/search?origin=63d0b5bd2cbd5656536ba09f&destination=63d0b5be2cbd5656536ba175&tripType=oneway&journeyType=depart&departureDate=2024-06-28&returnDate=2024-06-14&adult=1'
        page.goto(page_url, timeout=60000)  # Set timeout lebih lama
        
        # filter = page.get_by_test_id("search_tabs_FASTEST")
        # filter.click()

        time.sleep(10)

        try:
            tickets = page.locator("ScheduleList_card__qTGWF").all()
        except Exception as e:
            print(f"Error finding tickets: {e}")
            browser.close()
            return

        for ticket in tickets:
            try:
                ticketName = ticket.locator("ScheduleCard_bus_operator__kdN_K").inner_text(timeout=5000)
                print("Nama Bus : ", ticketName)
            except Exception as e:
                print(f"Error finding ticket name: {e}")
                ticketName = "-"
            
            # ticketClass = "-"
            # ticketType = "Pesawat"
            
            # try:
            #     ticketOrigin = ticket.get_by_test_id("flight_card_segment_departure_airport_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket origin: {e}")
            #     ticketOrigin = "-"
            
            # try:
            #     ticketDestination = ticket.get_by_test_id("flight_card_segment_destination_airport_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket destination: {e}")
            #     ticketDestination = "-"
            
            # try:
            #     ticketDescription = ticket.get_by_test_id("flight_card_segment_stops_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket description: {e}")
            #     ticketDescription = "-"
            
            # try:
            #     ticketDeparture = ticket.get_by_test_id("flight_card_segment_departure_time_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket departure: {e}")
            #     ticketDeparture = "-"
            
            # try:
            #     ticketArrival = ticket.get_by_test_id("flight_card_segment_destination_time_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket arrival: {e}")
            #     ticketArrival = "-"
            
            # try:
            #     ticketDuration = ticket.get_by_test_id("flight_card_segment_duration_0").inner_text(timeout=5000)
            # except Exception as e:
            #     print(f"Error finding ticket duration: {e}")
            #     ticketDuration = "-"
            
            # try:
            #     ticketPrice = ticket.locator('//div[@class="FlightCardPrice-module__priceContainer___nXXv2"]').inner_text(timeout=5000)
            #     ticketPrice = ticketPrice.replace('IDR', '')
            #     ticketPrice = ticketPrice.replace('.', '')
            #     ticketPrice = ticketPrice.replace(',', '.')
            #     harga = float(re.sub(r'[^\d.]', '', ticketPrice))
            #     # Bulatkan harga ke angka terdekat
            #     harga = round(harga)
            # except Exception as e:
            #     print(f"Error finding ticket price: {e}")
            #     harga = None
            
            # ticketDate = "2024-06-28"
            # ticketCity = "Solo"

            # # Simpan data ke dalam tabel transportasi
            # sql = """INSERT INTO transportasi 
            #          (nama_transportasi, jenis_transportasi, kelas, berangkat, tujuan, harga, jam_keberangkatan, jam_kedatangan, lama_perjalanan, kota, keterangan, tanggal)
            #          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # val = (ticketName, ticketType, ticketClass, ticketOrigin, ticketDestination, harga, ticketDeparture, ticketArrival, ticketDuration, ticketCity, ticketDescription, ticketDate)
            
            # try:
            #     cursor.execute(sql, val)
            #     conn.commit()
            #     print(f"Data berhasil disimpan: {val}")
            # except Exception as e:
            #     conn.rollback()
            #     print(f"Error saat menyimpan data: {e}")

        browser.close()
        # cursor.close()
        # conn.close()

