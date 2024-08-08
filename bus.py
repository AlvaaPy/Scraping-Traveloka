from playwright.sync_api import sync_playwright
import time

def bus_scrape():
    destination = ["Pulo Gebang"] # ganti jika ingin mengubah asal

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page_url = 'https://www.traveloka.com/id-id/bus-and-shuttle'
        page.goto(page_url)


        for dest in destination:
            asal = page.get_by_placeholder("Ketik nama kota, terminal, atau titik lainnya").nth(0)
            asal.wait_for()
            asal.click()
            asal.fill(dest)
            asalText = page.get_by_text("Terminal Pulo Gebang", exact=True).nth(0)
            asalText.click()

            tujuan = page.get_by_placeholder("Ketik nama kota, terminal, atau titik lainnya").nth(1)
            tujuan.wait_for()
            tujuan.click()
            tujuan.fill("Solo")
            tujuanText = page.get_by_text("Terminal Tirtonadi", exact=True)
            tujuanText.click()

            tanggal = page.locator("//input").nth(2)
            tanggal.click()
            # calendar = page.get_by_test_id('train-desktop-search-form-departure-date-input-calendar')
            calendarTest = page.get_by_test_id('date-cell-28-6-2024').nth(0)  # Format Date (date-cell-dd-m-yyyy)
            calendarTest.click()
            
            submitButton = page.locator("div.css-18t94o4").nth(1)
            submitButton.click()
            
            listTicketEl = page.locator("div.r-lgvlli").nth(0)
            listTicketEl.wait_for()
            
            time.sleep(7)
            
            ticketBus = page.locator("div.r-lrvibr").nth(277).all()
            
            for ticket in ticketBus:
                busName = ticket.locator("h3").inner_text()
                print("Nama Bus:", busName)

            #     busClass = ticket.locator("div.css-901oao").nth(0).inner_text()
            #     print("Kelas Bus:", busClass)

            #     busType = 'Bus'
            #     print("Jenis Kendaraan:", busType)

            #     busOrigin = ticket.locator("div.css-901oao").nth(1).inner_text()
            #     print("Asal:", busOrigin)

            #     busDestination = ticket.locator("div.css-901oao").nth(2).inner_text()
            #     print("Tujuan:", busDestination)

            #     busDescription = ticket.locator("div.css-901oao").nth(3).inner_text()
            #     print("Keterangan:", busDescription)

            #     busDeparture = ticket.locator("h3").nth(1).inner_text()
            #     print("Jam Berangkat:", busDeparture)

            #     busArrival = ticket.locator("h3").nth(2).inner_text()
            #     print("Jam Kedatangan:", busArrival)

            #     busDuration = ticket.locator("h3").nth(3).inner_text()
            #     print("Durasi:", busDuration)

            #     busPrice = ticket.locator("h2").inner_text()
            #     print("Harga:", busPrice)

            #     busDate = "28 Juni 2024"
            #     print("Tanggal:", busDate)

            #     busCity = "Solo"
            #     print("Kota tujuan:", busCity)
                
            # print("Jumlah Tiket Bus yang Ditemukan:", num_tickets)

        browser.close()
