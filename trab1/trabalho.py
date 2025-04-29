from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta
import time

def get_dates():
    tomorrow = datetime.now() + timedelta(days=1)
    day_after = tomorrow + timedelta(days=1)
    return tomorrow.strftime("%Y-%m-%d"), day_after.strftime("%Y-%m-%d")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        viewport={'width': 1280, 'height': 800}
    )
    page = context.new_page()
    
    # Obtém as datas para check-in e check-out
    checkin, checkout = get_dates()
    
    # Constrói a URL de busca com os parâmetros especificados
    search_url = f"https://www.booking.com/searchresults.pt-br.html?ss=Teres%C3%B3polis%2C+Rio+de+Janeiro%2C+Brasil&checkin={checkin}&checkout={checkout}&group_adults=1&no_rooms=1&group_children=0"
    
    try:
        # Navega para a página de busca
        page.goto(search_url)
        
        # Aguarda o carregamento dos resultados
        page.wait_for_selector('[data-testid="property-card"]', timeout=10000)
        
        # Adiciona um pequeno delay para garantir que a página carregou completamente
        time.sleep(2)
        
        # Obtém todos os cards de hotéis
        hotel_cards = page.query_selector_all('[data-testid="property-card"]')
        
        print("\nResultados da busca em Booking.com:")
        print("-" * 80)
        
        # Extrai e exibe as informações de cada hotel
        for card in hotel_cards:
            try:
                # Extrai o nome do hotel
                name_element = card.query_selector('[data-testid="title"]')
                name = name_element.inner_text() if name_element else "Nome não disponível"
                
                # Extrai o preço
                price_element = card.query_selector('[data-testid="price-and-discounted-price"]')
                price = price_element.inner_text() if price_element else "Preço não disponível"
                
                # Extrai a disponibilidade
                rooms_element = card.query_selector('[data-testid="availability"]')
                rooms = rooms_element.inner_text() if rooms_element else "Disponibilidade não disponível"
                
                print(f"Nome do Hotel: {name}")
                print(f"Preço: {price}")
                print(f"Disponibilidade: {rooms}")
                print("-" * 80)
                
            except Exception as e:
                print(f"Erro ao extrair dados de um hotel: {str(e)}")
                continue
                
    except Exception as e:
        print(f"Erro durante o scraping: {str(e)}")
    finally:
        browser.close()