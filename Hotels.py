from playwright.sync_api import sync_playwright
import time
import mysql.connector

def scrape_hotels():
    kota = ["Solo"]
    
    # Koneksi ke database MySQL
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",  # ganti dengan password MySQL Anda Jika Ada
        database="tripplaner" # Ganti dengan nama DB anda
    )
    cursor = db.cursor()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page_url = 'https://www.traveloka.com/id-id/hotel'
        page.goto(page_url, timeout=300000)
        
        for k in kota:
            tujuan = page.get_by_test_id("autocomplete-field")
            tujuan.wait_for()
            tujuan.click()
            tujuan.fill(k)
            
            tujuanText = page.get_by_text("Solo", exact=True).nth(0)
            tujuanText.click()
            
            checkIn = page.get_by_test_id("check-in-date-field")
            checkIn.click()
            checkInDate = page.get_by_test_id("date-cell-28-6-2024")
            checkInDate.click()
            
            durasi = page.get_by_test_id("duration-field")
            durasi.click()
            
            durasiDay = page.get_by_text("1 malam", exact=True).nth(0)
            durasiDay.click()
            
            submitButton = page.get_by_test_id("search-submit-button")
            submitButton.click()
            
            # Menuju ke konten
            filter = page.get_by_text("Popularitas tertinggi")
            filter.click()
            
            filterFind = page.get_by_text("Harga Terendah")
            filterFind.click()
            
            listTicketEl = page.get_by_test_id("infinite-list-container")
            listTicketEl.wait_for()
            
            time.sleep(30)
            
            listHotel = page.get_by_test_id("list-card-inview-wrapper").all()
            num_tickets = len(listHotel)
            
            for hotels in listHotel:
                hotelName = hotels.get_by_test_id("tvat-hotelName").inner_text()
                print("Nama Hotel : ", hotelName)
                
                hotelPrice = hotels.get_by_test_id("tvat-hotelPrice").inner_text()
                harga_formatted = hotelPrice.replace('Rp', '').replace('.', '').strip()
                print("Harga : ", harga_formatted)
                
                hotelRating = hotels.get_by_test_id("tvat-ratingScore").inner_text()
                print("Rating : ", hotelRating)
                
                hotelKota = "Solo"
                print("Kota : ", hotelKota)
                
                # Ambil alamat dari deskripsi hotel
                hotelAlamat = hotels.get_by_test_id("tvat-hotelLocation").inner_text()
                print("Alamat : ", hotelAlamat)
                
                hotelDesk = "-"
                print("Deskripsi : ", hotelDesk)
                
                # Masukkan data ke database
                query = """
                INSERT INTO hotels (nama_hotel, harga, rating, deskripsi, kota, alamat)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (hotelName, harga_formatted, hotelRating, hotelDesk, hotelKota, hotelAlamat)
                cursor.execute(query, values)
                db.commit()
                
            print("Jumlah Hotel yang Ditemukan:", num_tickets)
        
        browser.close()
    cursor.close()
    db.close()

