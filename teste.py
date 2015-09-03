# importa biblioteca selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
driver.get('http://bi.mte.gov.br/bgcaged/caged_perfil_municipio/index.php')

# uf
uf = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('uf'))
Select(uf).select_by_visible_text('Paraná')

# microregiao
micro = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('micro'))
Select(micro).select_by_index('Paranavaí')

# municipio
mun = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('mun'))
Select(mun).select_by_visible_text('411840:Paranavaí')

# mes inicio
mes_inicio_cons = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('mes_inicio_cons'))
Select(mun).select_by_visible_text('Jan')

# mes fim
mes_fim_cons = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('mes_fim_cons'))
Select(mun).select_by_visible_text('Jun')

# click
driver.click("xpath=//a[contains(@href,'javascript:executa_consulta()')")