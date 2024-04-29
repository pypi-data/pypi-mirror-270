# # from recipe_urls import scrape_urls
# # from recipe_urls import scrape_html
# # import random
# # import time
# # import requests
# # from requests.exceptions import HTTPError, ReadTimeout
# # from bs4 import BeautifulSoup
# # from urllib.parse import urlparse, urljoin
# # import csv
# # import httpx
# # import re

# # base_url = "https://www.bonappetit.com"

# # # ----------- get html content -----------------

# # HEADERS = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
# # }

# # try:
# #     response = requests.get(url=base_url, headers=HEADERS)
# #     if response.status_code == 403:
# #         raise HTTPError(f"Access to {base_url} is forbidden (403).")
# #     html = response.text

# # except HTTPError as e:
# #     raise HTTPError(f"HTTP error for {base_url}. {e}") from e

# # except Exception as e:
# #     raise RuntimeError(f"Unexpected error accessing {base_url}. {e}") from e

# # # ------------- get links -------------------
# # # soup = BeautifulSoup(html, "html.parser")

# # links1 = scrape_urls(base_url)
# # links2 = scrape_html(html)
# # print(set(links1) == set(links2))

# # # # # # # ----------- get host -----------------

# # # # # # # Remove "www." if it exists
# # # # # # domain = re.sub(r'^www\.', '', base_url)

# # # # # # # Extract domain name without top-level domain
# # # # # # match = re.search(r'https?://(?:www\.)?([\w-]+)\.([\w-]+)', domain)
# # # # # # if match:
# # # # # #     domain_name = match.group(1)
# # # # # #     print(domain_name)

# # # # # # # ----------- save test file -----------------

# # # # # # def save_to_csv(data, save_path):
# # # # # #     with open(save_path, 'w', newline='', encoding='utf-8') as csvfile:
# # # # # #         writer = csv.writer(csvfile)
# # # # # #         for item in data:
# # # # # #             writer.writerow([item])

# # # # # # def save_to_html(html, save_path):
# # # # # #     with open(save_path, "w") as file:
# # # # # #         file.write(html)

# # # # # # # Create folder first
# # # # # # save_to_html(html, f"tests/test_data/{domain_name}/{domain_name}.testhtml")
# # # # # # save_to_csv(links, f'tests/test_data/{domain_name}/{domain_name}.csv')

# # # # # # # ----------- run all links -----------------

# # # # # # base_urls = [
# # # # # #     "https://abuelascounter.com",
# # # # # #     "https://www.acouplecooks.com",
# # # # # #     "https://addapinch.com", 
# # # # # #     "http://www.afghankitchenrecipes.com", 
# # # # # #     "https://www.allrecipes.com", 
# # # # # #     "https://www.ambitiouskitchen.com", 
# # # # # #     "https://www.archanaskitchen.com", 
# # # # # #     "https://www.averiecooks.com", # TODO unwanted pattern 'web-stories'
# # # # # #     "https://bakingmischief.com", 
# # # # # #     "https://www.baking-sense.com", 
# # # # # #     "https://barefootcontessa.com", 
# # # # # #     "https://www.bbc.co.uk/food", 
# # # # # #     "https://www.bettycrocker.com", 
# # # # # #     "https://www.bigoven.com", 
# # # # # #     "https://bluejeanchef.com", 
# # # # # #     "https://www.bonappetit.com", 
# # # # # #     "https://www.bongeats.com", 
# # # # # #     "https://www.bowlofdelicious.com", 
# # # # # #     "https://www.budgetbytes.com",
# # # # # #     "https://carlsbadcravings.com",  
# # # # # #     "https://www.castironketo.net", 
# # # # # #     "https://www.cdkitchen.com", 
# # # # # #     "https://chefsavvy.com",
# # # # # #     "https://www.closetcooking.com/top-recipes/",  
# # # # # #     "https://cookieandkate.com/recipes/", 
# # # # # #     "https://copykat.com/100-favorite-copycat-recipes/", 
# # # # # #     "https://www.countryliving.com/food-drinks/", 
# # # # # #     "https://creativecanning.com", 
# # # # # #     "https://www.davidlebovitz.com/blog/", 
# # # # # #     "https://www.delish.com/cooking/recipe-ideas/", 
# # # # # #     "https://domesticate-me.com/category/recipes/", 
# # # # # #     "https://downshiftology.com", 
# # # # # #     "https://www.eatingbirdfood.com", 
# # # # # #     "https://www.eatingwell.com/recipes/", 
# # # # # #     "https://www.eatliverun.com/recipes/", 
# # # # # #     "https://www.eatwell101.com", 
# # # # # #     "https://eatsmarter.com", 
# # # # # #     "https://eatwhattonight.com", 
# # # # # #     "https://elavegan.com", 
# # # # # #     "https://www.epicurious.com", 
# # # # # #     "https://www.errenskitchen.com", 
# # # # # #     "https://www.ethanchlebowski.com/cooking-techniques-recipes", 
# # # # # #     "https://www.farmhouseonboone.com", 
# # # # # #     "https://www.fifteenspatulas.com", 
# # # # # #     "https://www.finedininglovers.com/recipes", 
# # # # # #     "https://fitmencook.com/recipes/", 
# # # # # #     "https://fitslowcookerqueen.com", 
# # # # # #     "https://www.food.com", 
# # # # # #     "https://food52.com", 
# # # # # #     "https://www.foodandwine.com/recipes", 
# # # # # #     "https://www.foodnetwork.com/recipes", # 403 error
# # # # # #     "https://www.foodrepublic.com/category/recipes/", 
# # # # # #     "https://www.forksoverknives.com", 
# # # # # #     "https://forktospoon.com/category/recipes/", 
# # # # # #     "https://www.gimmesomeoven.com", 
# # # # # #     "https://www.gonnawantseconds.com", 
# # # # # #     "https://goodfooddiscoveries.com",
# # # # # #     "https://www.goodhousekeeping.com/food-recipes/", 
# # # # # #     "https://www.greatbritishchefs.com", 
# # # # # #     "https://www.halfbakedharvest.com", # TODO eliminate numbers in regex
# # # # # #     "https://handletheheat.com",  
# # # # # #     "https://headbangerskitchen.com", 
# # # # # #     "https://heatherchristo.com",  
# # # # # #     "https://www.hellofresh.com/recipes", 
# # # # # #     "https://www.hersheyland.com/recipes", 
# # # # # #     "https://hostthetoast.com/recipes/", # TODO add 'how-to' to unwanted patterns
# # # # # #     "https://im-worthy.com", 
# # # # # #     "https://www.indianhealthyrecipes.com",
# # # # # #     "https://insanelygoodrecipes.com",  
# # # # # #     "https://inspiralized.com", 
# # # # # #     "https://izzycooking.com", 
# # # # # #     "https://www.jamieoliver.com", 
# # # # # #     "https://jimcooksfoodgood.com", 
# # # # # #     "https://joyfoodsunshine.com/recipe-index/", 
# # # # # #     "https://www.justataste.com", 
# # # # # #     "https://justbento.com/recipes/all", 
# # # # # #     "https://www.justonecookbook.com", 
# # # # # #     "https://www.kingarthurbaking.com", 
# # # # # #     "https://leanandgreenrecipes.net",
# # # # # #     "https://lifestyleofafoodie.com", 
# # # # # #     "https://littlespicejar.com", 
# # # # # #     "https://livelytable.com", 
# # # # # #     "https://lovingitvegan.com", 
# # # # # #     "https://ninjatestkitchen.eu", 
# # # # # #     "https://cooking.nytimes.com", 
# # # # # #     "https://ohsheglows.com", 
# # # # # #     "https://www.onceuponachef.com", 
# # # # # #     "https://www.paleorunningmomma.com", 
# # # # # #     "https://www.persnicketyplates.com", 
# # # # # #     "https://www.pickuplimes.com", 
# # # # # #     "https://www.platingpixels.com", 
# # # # # #     "https://rachlmansfield.com", 
# # # # # #     "https://rainbowplantlife.com", 
# # # # # #     "https://reciperunner.com", 
# # # # # #     "https://sallysbakingaddiction.com", 
# # # # # #     "https://simple-veganista.com", 
# # # # # #     "https://www.simplywhisked.com", 
# # # # # #     "https://www.tasteofhome.com", 
# # # # # #     "https://tasty.co", 
# # # # # #     "https://www.wellplated.com", 
# # # # # #     "https://whole30.com"
# # # # # #     ]

# # # # # # compiled_recipe_links = []

# # # # # # for base_url in base_urls:
# # # # # #     print(base_url)
# # # # # #     print('   ')
# # # # # #     random_sleeps = True
# # # # # #     lower_sleep = 1
# # # # # #     upper_sleep = 3

# # # # # #     if random_sleeps:
# # # # # #         sleep_time = random.randint(lower_sleep, upper_sleep)
# # # # # #         time.sleep(sleep_time)
# # # # # #     try:
# # # # # #         scrape = scrape_urls(base_url)
# # # # # #         print(scrape)
# # # # # #         print('----------------------------------')
# # # # # #         compiled_recipe_links.extend(scrape)
# # # # # #     except Exception as e:
# # # # # #         print(e)

# # # # # # print(len(compiled_recipe_links))


# # # # # # ###############################################################################################
# # # # # # # BASE_SCRAPER

# # # # # # HEADERS = {
# # # # # #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
# # # # # # }

# # # # # # try:
# # # # # #     response = httpx.get(url=base_url, headers=HEADERS)
# # # # # #     if response.status_code == 403:
# # # # # #         raise httpx.HTTPError(f"Access to {base_url} is forbidden (403).")
# # # # # #     html = response.content
# # # # # #     soup = BeautifulSoup(html, "html.parser")

# # # # # # except httpx.HTTPError as e:
# # # # # #     raise httpx.HTTPError(f"HTTP error for {base_url}. {e}") from e

# # # # # # except Exception as e:
# # # # # #     raise RuntimeError(f"Unexpected error accessing {base_url}. {e}") from e

# # # # # # href_links = [a["href"] for a in soup.find_all("a", href=True)]

# # # # # # recipe_pattern = re.compile(r'https://www\.cdkitchen\.com/recipes/[\w-]+/\d+/[\w-]+\.shtml')

# # # # # # # Use a set to deduplicate the links while filtering href links for recipe-specific ones
# # # # # # unique_links_set = set(link for link in href_links if recipe_pattern.search(link))
# # # # # # print(unique_links_set)

# # # # ################ TEST AND CHECK ######################################

# from recipe_urls import scrape_urls
# from recipe_urls import scrape_html
# import requests
# from requests.exceptions import HTTPError, ReadTimeout
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse
# import csv
# import re
# import os

# # def delete_csv_file(file_path):
# #     try:
# #         cont = input(f'\nConfirm delete: {file_path}')

# #         if cont.lower() != '':
# #             raise ValueError(f'Deletion not confirmed. Aborting.')

# #         os.remove(file_path)
# #         print(f"File '{file_path}' deleted successfully.")
# #     except OSError as e:
# #         print(f"Error deleting the file '{file_path}': {e}")

# def save_to_csv_exp_output(data, save_path):
#     with open(save_path, 'w') as csvfile:
#         writer = csv.writer(csvfile)
#         for item in data:
#             writer.writerow([item])

# def save_to_csv_base_url(data, save_path):
#     with open(save_path, 'w') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([data])

# def save_to_html(html, save_path):
#     with open(save_path, "w") as file:
#         file.write(html)

# base_urls = [ 
#     "https://abuelascounter.com",
#     "https://www.acouplecooks.com",
#     "https://addapinch.com", 
#     "http://www.afghankitchenrecipes.com", 
#     "https://www.allrecipes.com", 
#     "https://www.ambitiouskitchen.com", 
#     "https://www.archanaskitchen.com", 
#     "https://www.averiecooks.com",
#     "https://bakingmischief.com", 
#     "https://www.baking-sense.com", 
#     "https://barefootcontessa.com", 
#     "https://www.bbc.co.uk/food", 
#     "https://www.bettycrocker.com", 
#     "https://www.bigoven.com", 
#     "https://bluejeanchef.com", 
#     "https://www.bonappetit.com", 
#     "https://www.bongeats.com", 
#     "https://www.bowlofdelicious.com", 
#     "https://www.budgetbytes.com",
#     "https://carlsbadcravings.com",  
#     "https://www.castironketo.net", 
#     "https://www.cdkitchen.com", 
#     "https://chefsavvy.com",
#     "https://www.closetcooking.com",  
#     "https://cookieandkate.com", 
#     "https://copykat.com", 
#     "https://www.countryliving.com/food-drinks/", 
#     "https://creativecanning.com", 
#     "https://www.davidlebovitz.com/blog/", 
#     "https://www.delish.com/cooking/recipe-ideas/", 
#     "https://domesticate-me.com/category/recipes/", 
#     "https://downshiftology.com", 
#     "https://www.eatingbirdfood.com", 
#     "https://www.eatingwell.com/recipes/", 
#     "https://www.eatliverun.com/recipes/", 
#     "https://www.eatwell101.com", 
#     "https://eatsmarter.com", 
#     "https://eatwhattonight.com", 
#     "https://elavegan.com", 
#     "https://www.epicurious.com", 
#     "https://www.errenskitchen.com", 
#     "https://www.ethanchlebowski.com/cooking-techniques-recipes", 
#     "https://www.farmhouseonboone.com", 
#     "https://www.fifteenspatulas.com", 
#     # "https://www.finedininglovers.com/recipes", 
#     "https://fitmencook.com/recipes/", 
#     "https://fitslowcookerqueen.com", 
#     "https://www.food.com", 
#     "https://food52.com", 
#     "https://www.foodandwine.com/recipes", 
#     # "https://www.foodnetwork.com/recipes", # 403 error
#     "https://www.foodrepublic.com/category/recipes/", 
#     "https://www.forksoverknives.com", 
#     "https://forktospoon.com/category/recipes/", 
#     "https://www.gimmesomeoven.com", 
#     "https://www.gonnawantseconds.com", 
#     "https://goodfooddiscoveries.com",
#     "https://www.goodhousekeeping.com/food-recipes/", 
#     "https://www.greatbritishchefs.com", 
#     "https://www.halfbakedharvest.com",
#     "https://handletheheat.com",  
#     "https://headbangerskitchen.com", 
#     "https://heatherchristo.com",  
#     "https://www.hellofresh.com/recipes", 
#     "https://www.hersheyland.com/recipes", 
#     "https://hostthetoast.com/recipes/",
#     "https://im-worthy.com", 
#     "https://www.indianhealthyrecipes.com",
#     "https://insanelygoodrecipes.com",  
#     "https://inspiralized.com", 
#     "https://izzycooking.com", 
#     "https://www.jamieoliver.com", 
#     "https://jimcooksfoodgood.com", 
#     "https://joyfoodsunshine.com", 
#     "https://www.justataste.com", 
#     "https://justbento.com/recipes/all", 
#     "https://www.justonecookbook.com", 
#     "https://www.kingarthurbaking.com", 
#     "https://leanandgreenrecipes.net",
#     "https://lifestyleofafoodie.com", 
#     "https://littlespicejar.com", 
#     "https://livelytable.com", 
#     "https://lovingitvegan.com", 
#     "https://ninjatestkitchen.eu", 
#     "https://cooking.nytimes.com", 
#     "https://ohsheglows.com", 
#     "https://www.onceuponachef.com", 
#     "https://www.paleorunningmomma.com", 
#     "https://www.persnicketyplates.com", 
#     # "https://www.pickuplimes.com", 
#     "https://www.platingpixels.com", 
#     "https://rachlmansfield.com", 
#     "https://rainbowplantlife.com", 
#     "https://reciperunner.com", 
#     "https://sallysbakingaddiction.com", 
#     "https://simple-veganista.com", 
#     "https://www.simplywhisked.com", 
#     "https://www.tasteofhome.com", 
#     "https://tasty.co", 
#     "https://www.wellplated.com", 
#     "https://whole30.com"
#     ]

# # ----------- get html content -----------------
# for base_url in base_urls:
#     print(f'\nRunning {base_url}...\n')

#     HEADERS = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
#     }

#     try:
#         response = requests.get(url=base_url, headers=HEADERS)
#         if response.status_code == 403:
#             raise HTTPError(f"Access to {base_url} is forbidden (403).")
#         html = response.text

#     except HTTPError as e:
#         raise HTTPError(f"HTTP error for {base_url}. {e}") from e

#     except Exception as e:
#         raise RuntimeError(f"Unexpected error accessing {base_url}. {e}") from e

# # ------------- get links -------------------

#     links = scrape_html(html)
#     # print(links)

#     # cont = input(f'\nLinks look good?')

#     # if cont.lower() != '':
#     #     break

# # ----------- get host -----------------

#     # Remove "www." if it exists
#     domain = re.sub(r'^www\.', '', base_url)

#     # Extract domain name without top-level domain
#     match = re.search(r'https?://(?:www\.)?([\w-]+)\.([\w-]+)', domain)
#     if match:
#         domain_name = match.group(1)

#     if domain_name == 'cooking':
#         domain_name = 'nytimes'

# # # ----------- save test file -----------------

# #     # Create folder first

#     # delete_csv_file(f'tests/test_data/{domain_name}/{domain_name}.csv')
#     save_to_csv_base_url(base_url, f'tests/test_data/{domain_name}/{domain_name}_base_url.csv')
#     save_to_csv_exp_output(links, f'tests/test_data/{domain_name}/{domain_name}_exp_output.csv')
#     save_to_html(html, f"tests/test_data/{domain_name}/{domain_name}.testhtml")

