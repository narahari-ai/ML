# virtual environment used for installation of scrapy project

py -m venv venv

for python2 venv should be virtualenv


second one is folder name
activate virtual environment by typing venv\Scripts\activate in commnad line or .\venv\Scripts\activate

#install required pakages.
py -m pip install -r requirements.txt


Scrapy createproject webScrapping

navigate to project newly created to user below command.

Scrapy crawl app

Write required web scrapping inside spiders folder here amazon.py


 libraries used.

 add user agent of goolge bot tried.

 scrapy_user_agents
 scrapy_proxy_pool


 scrapy setting.py file modified accodingly to use piple, user agent, user agent rotation, proxy pooling.




 Css selector and X-path selectors can be used in Scrapy.

# chrome css Selector gadget used for css selection.


# for command line shell data access used

scrapy shell "https://www.amazon.in/s?k=groceries&ref=nb_sb_noss_2"

scrapped data saved to sqllite3

to save output data in json format.
scrapy crawl app -o items.json


after installing virtual environment packages use below command to save packages to requirements.txt
py -m pip freeze > requirements.txt





