import pyautogui as pa
import datetime
import time
import webbrowser, os
import pyperclip

while True:
    
    dt = str(datetime.datetime.today())
    dia = dt[:10]
    string = dia
    pyperclip.copy(string)
    link = ('https://wms.mercadolivre.com.br/reports/group/orders?order_date_from={0}&order_date_to={0}&carrier.id=&status=pending,planning,to_pick,picking,sorting,to_group,grouping,grouped,to_pack,packed,to_document,documented,to_dispatch,to_out,out,returned,returned_damage_rejected,cancelled,unavailable,split&sort=date_created_desc').format(dia)
    
    pasta_download= "C:/Users/operador/Downloads"

    os.system('"start C:/Users/operador/Google/Chrome/Application/chrome.exe"')
    time.sleep(3)
    time.sleep(1)
    pa.keyDown('winleft')
    pa.press('up')
    pa.keyUp('winleft')
    time.sleep(1)
    pa.moveTo(1349,81, duration=1)
    pa.leftClick()
    pa.moveTo(1308,228, duration=1)
    pa.press('esc')
    pa.press('esc')
    time.sleep(1)
    pa.press('esc')
    pa.press('esc')
    url = link
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(link)
    time.sleep(2)
    time.sleep(1)
    pa.keyDown('winleft')
    pa.press('up')
    pa.keyUp('winleft')
    time.sleep(1)
    pa.press('esc')
    pa.moveTo(990, 180, duration=1)
    pa.leftClick(duration=1)
    pa.moveTo(685, 492, duration=1)
    pa.leftClick(duration=1)

#Gera o movimentos    
    dt = str(datetime.datetime.today())
    dia = dt[:10]
    string = dia
    pyperclip.copy(string)
    link_movs = ('https://wms.mercadolivre.com.br/reports/movements?date_from={0}&date_to={0}&process_name=picking,packing').format(dia)
    edge_path = 'C:/Users/operador/Edge/Application/msedge.exe %s'
    os.system('"start C:/Users/operador/Edge/Application/msedge.exe"')
    time.sleep(1)
    pa.moveTo(1355, 76, duration=1)
    pa.leftClick(duration=1)
    pa.moveTo(680, 491, duration=1)
    webbrowser.get(edge_path).open(link_movs)
    time.sleep(2)
    pa.keyDown('winleft')
    pa.press('up')
    pa.keyUp('winleft')
    pa.moveTo(1110, 153, duration=1)
    pa.leftClick(duration=1)
    pa.moveTo(680, 491, duration=1)
    pa.leftClick(duration=1)
    time.sleep(3)
    os.system('"taskkill /F /IM msedge.exe"')
#Fim gera movimentos
    os.system('"start C:/Users/operador/anaconda3/python.exe "g:/Meu Drive/AUTOMATION PROJECT/bar300.py"')
    time.sleep(1)
    pa.press('f11')

    time.sleep(301)
    pa.hotkey('Alt', 'f4')
  
    pa.moveTo(1135, 181, duration=0.5)
    pa.leftClick(duration=0.1)
    time.sleep(3)
    pa.moveTo(1177, 279, duration=0.5)
    pa.leftClick(duration=0.1)
#Baixa movimentos
    os.system('"start C:/Users/operador/Edge/Application/msedge.exe"')
    time.sleep(1)
    webbrowser.get(edge_path).open(link_movs)
    pa.moveTo(1355, 76, duration=1)
    pa.leftClick(duration=1)
    pa.moveTo(680, 491, duration=1)
    time.sleep(1)
    pa.keyDown('winleft')
    pa.press('up')
    pa.keyUp('winleft')
    time.sleep(1)

    pa.moveTo(1234, 158, duration=2)
    pa.leftClick()
    pa.moveTo(1136, 282, duration=2)
    pa.leftClick()
    pa.moveTo(1115, 300, duration=2)
    pa.leftClick()
#Finala baixar movimentos
    
    os.system('"start C:/Users/operador/anaconda3/python.exe "g:/Meu Drive/AUTOMATION PROJECT/bar300.py"')
    pa.press('enter')
    time.sleep(1)
    pa.press('f11')

    time.sleep(301)
    pa.hotkey('Alt','f4')
    time.sleep(1)
    os.system('"start C:/Users/operador/Downloads"')
    time.sleep(2)
    pa.press('right')
    pa.press('space')
    pa.press('f2')
    pa.hotkey('Ctrl', 'v')
    pa.press('enter')
    pa.hotkey('Ctrl', 'c')
    #pa.press('del')
    #gdrive="G:\Meu Drive\Analise Volumetria\Pedidos"
    #os.system(f'start {os.path.realpath(gdrive)}')
    #pa.hotkey('Ctrl', 'v')
    time.sleep(1)
    pa.hotkey('winleft', 'r')
    time.sleep(1)
    pa.hotkey('Ctrl','a')
    pa.write('G:\Meu Drive\Analise Volumetria\Pedidos')
    time.sleep(2)
    pa.press('enter')
    time.sleep(2)
    pa.hotkey('Ctrl', 'v')
    time.sleep(1)
    pa.press('enter')
    time.sleep(5)
    pa.press('esc')
    pa.hotkey('Alt', 'f4')
    pasta_download="C:/Users/operador/Downloads"
    os.system('"start C:/Users/operador/Downloads"')
    time.sleep(2)
    pa.press('right')
    time.sleep(2)
    pa.press('space')
    time.sleep(2)
    pa.press('del')
    time.sleep(2)
    pa.press('enter')
    time.sleep(2)
    pa.hotkey('Alt','f4')
    os.system('"taskkill /F /IM chrome.exe"')
    os.system('"start C:/Users/operador/Downloads"')
    time.sleep(2)
    pa.hotkey('Ctrl', 'a')
    pa.press('del')
    pa.press('enter')
    pa.sleep(1)
#Armazena movimentos na pasta
    pyperclip.copy(string)
    os.system('"start C:/Users/operador/DownloadMovs"')
    time.sleep(2)
    pa.press('right')
    pa.press('space')
    pa.press('f2')
    pa.hotkey('Ctrl', 'v')
    pa.press('enter')
    pa.hotkey('Ctrl', 'c')
    #pa.press('del')
    #gdrive="G:\Meu Drive\Analise Volumetria\Pedidos"
    #os.system(f'start {os.path.realpath(gdrive)}')
    #pa.hotkey('Ctrl', 'v')
    time.sleep(1)
    pa.hotkey('winleft', 'r')
    time.sleep(1)
    pa.hotkey('Ctrl','a')
    pa.write('G:\Meu Drive\Analise Volumetria\Movimentos')
    time.sleep(2)
    pa.press('enter')
    time.sleep(2)
    pa.hotkey('Ctrl', 'v')
    time.sleep(1)
    pa.press('enter')
    time.sleep(5)
    pa.press('esc')
    pa.hotkey('Alt', 'f4')
    pasta_download_movs="C:/Users/operador/DownloadMovs"
    os.system('"start C:/Users/operador/DownloadMovs"')
    time.sleep(2)
    pa.press('right')
    time.sleep(2)
    pa.press('space')
    time.sleep(2)
    pa.press('del')
    time.sleep(2)
    pa.press('enter')
    time.sleep(2)
    pa.hotkey('Alt','f4')
    os.system('"taskkill /F /IM msedge.exe"')
    os.system('"start C:/Users/operador/DownloadMovs"')
    time.sleep(2)
    pa.hotkey('Ctrl', 'a')
    pa.press('del')
    pa.press('enter')
    pa.sleep(1)
##fim armazenar na pasta

    
    os.system('"start C:/Users/operador/Google/Chrome/Application/chrome.exe"')
    time.sleep(1)
    link_update = 'https://app.powerbi.com/datahub/datasets/c1093d87-87db-4f45-a618-97505ccbb91d'
    webbrowser.get(chrome_path).open(link_update)
    time.sleep(10)
    time.sleep(1)
    pa.keyDown('winleft')
    pa.press('up')
    pa.keyUp('winleft')
    time.sleep(1)
    pa.moveTo(364, 138, duration=0.5)
    pa.leftClick(duration=0.1)
    pa.moveTo(376, 174, duration=0.5)
    pa.leftClick(duration=0.1)

    time.sleep(3)
    os.system('"taskkill /F /IM chrome.exe"')
    time.sleep(2)
    os.system('"taskkill /f /IM explorer.exe && start explorer.exe"')
    time.sleep(3)
    
