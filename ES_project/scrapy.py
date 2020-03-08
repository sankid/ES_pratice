'''
我们的目标是访问在线食谱并将它们存储在Elasticsearch中以用于搜索和分析。
我们将首先从Allrecipes中获取数据并将其存储在ES中。我们还将创建一个严格的模式或映射，以便我们确保数据以正确的格式和类型进行索引。最后只要列出沙拉食谱的清单。
'''


# 获取数据

import json
from time import sleep

import requests
from bs4 import BeautifulSoup

def parse(u):
    title = '-'
    submit_by = '-'
    description = '-'
    calories = 0
    ingredients = []
    rec = {}

    try:
        r = requests.get(u,headers = headers)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html,'lxml')
            #title
            title_section = soup.select('.recipe-summary_h1')
            #submitter
            submitter_section = soup.select('.submitter_name')
            #description
            description_section = soup.select('.submitter_description')
            #ingredients_section
            ingredients_section = soup.select('.recipe-ingred_txt')

            #calories
            calories_section = soup.select('.calorie-count')
            if calories_section:
                calories = calories_section[0].text.replace('cals','').strip()

            if ingredients_section:
                for ingredient in ingredients_section:
                    ingredient_text = ingredient.text.strip()
                    if 'Add all ingredients to list' not in ingredient_text and ingredient_text != '':
                        ingredients.append({'step':ingredient.text.strip()})

            if description_section:
                decription = description_section[0].text.strip().replace('"','')

            if submitter_section:
                submit_by = submitter_section[0].text.strip()

            if title_section:
                title = title_section[0].text

            rec = {'title':title,'submitter':submit_by,'description':description,'calories':calories,'ingredients':ingredients}

    except Exception as e:
        print('Exception while parsing:{}'.format(e))

    finally:
        return json.dumps(rec)


if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    url = 'https://www.allrecipes.com/recipes/96/salad/'
    r = requests.get(url,headers = headers)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html,'lxml')
        links = soup.select('.fixed-recipe-card_h3 a')
        for link in links:
            sleep(2)
            result = parse(link['href'])
            print(result)
            print('='*20)
