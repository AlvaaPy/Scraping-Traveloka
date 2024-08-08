from playwright.sync_api import sync_playwright
import time
import mysql.connector

def scrape_kereta():
    destination = ["Jakarta"]  # ganti jika ingin mengubah asal

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

        page_url = 'https://www.traveloka.com/id-id/kereta-api'
        page.goto(page_url)

        asal = page.get_by_placeholder("Asal")
        asal.wait_for()

        for dest in destination:
            asal.click()
            asal.fill(dest)
            asalText = page.get_by_text("PSE - Pasar Senen - Jakarta", exact=True).nth(0)
            asalText.click()

            tujuan = page.get_by_placeholder("Tujuan")
            tujuan.wait_for()
            tujuan.click()
            tujuan.fill("Yogya")
            tujuanText = page.get_by_text("WT - Wates", exact=True)
            tujuanText.click()

            tanggal = page.get_by_test_id('train-desktop-search-form-departure-date-input-value')
            tanggal.click()
            calendarTest = page.get_by_test_id('date-cell-28-6-2024')  # Format Date (date-cell-dd-m-yyyy)
            calendarTest.click()

            submitButton = page.get_by_test_id("train-desktop-search-form-cta")
            submitButton.click()

            listTicketEl = page.get_by_test_id("train-desktop-search-result-list-departure")
            listTicketEl.wait_for()
            
            time.sleep(6)
            
            listTicket = page.get_by_test_id("train-desktop-search-result-list-departure-item").all()
            num_tickets = len(listTicket)
            
            for ticket in listTicket:
                trainName = ticket.locator("h3").nth(0).inner_text()
                print("Nama Kereta:", trainName)

                trainClass = ticket.locator("div.css-901oao").nth(0).inner_text()
                print("Kelas Kereta:", trainClass)

                trainType = 'Kereta Api'
                print("Jenis Kendaraan : ", trainType)

                trainOrigin = ticket.locator("div.css-901oao").nth(1).inner_text()
                print("Asal:", trainOrigin)

                traindestination = ticket.locator("div.css-901oao").nth(2).inner_text()
                print("Tujuan:", traindestination)

                trainDescription = ticket.locator("div.css-901oao").nth(3).inner_text()
                print("Keterangan:", trainDescription)

                trainDeparture = ticket.locator("h3").nth(1).inner_text()
                print("Jam Berangkat:", trainDeparture)

                trainArrival = ticket.locator("h3").nth(2).inner_text()
                print("Jam Kedatangan:", trainArrival)

                trainDuration = ticket.locator("h3").nth(3).inner_text()
                print("Durasi:", trainDuration)

                trainPrice = ticket.locator("h2").inner_text()
                harga_formatted = trainPrice.replace('Rp', '').replace('.', '').strip()
                print("Harga:", harga_formatted)

                trainDate = "28 Juni 2024"
                print("Tanggal:", trainDate)

                trainCity = "Solo"
                print("Kota tujuan:", trainCity)
                
                # Masukkan data ke database
                query = """
                INSERT INTO transportasi (nama_transportasi, jenis_transportasi, kelas, berangkat, tujuan, harga, jam_keberangkatan, jam_kedatangan, lama_perjalanan, kota, keterangan, tanggal)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (trainName, trainType, trainClass, trainOrigin, traindestination, harga_formatted, trainDeparture, trainArrival, trainDuration, trainCity, trainDescription, trainDate)
                cursor.execute(query, values)
                db.commit()
                
            print("Jumlah Tiket Kereta yang Ditemukan:", num_tickets)

        browser.close()
    cursor.close()
    db.close()
