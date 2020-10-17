# vistual environment used for installation of scrapy project
Virtualenv .


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



