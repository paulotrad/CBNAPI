import requests
from bs4 import BeautifulSoup



def news(ascending=False,counter=None,queryurl=None):

    news={}
    r=requests.get(f'https://www1.cbn.com/{queryurl}')

    if r.status_code==200:


        soup=BeautifulSoup(r.content,'html.parser')
        news['results']=soup.find('div', class_='section-header-wrapper clearfix').find('span').text.strip()

        for index,article in enumerate(soup.find_all('article')):
            endpointurl=article['about']
            if counter:
                news['count'] = counter
                if index<counter:
                        try:
                            news[index+1]={'title':article.find('span')['content'],'url':article['about'],'image':{'alt':article.find('img')['alt'],'src':article.find('img')['src'],'width':article.find('img')['width'],'height':article.find('img')['height'],'title':article.find('img')['title']}}
                        except:
                            news[index+1]={'title':article.find('span')['content'],'url':article['about'],'image':{'alt':article.find('img')['alt'],'src':article.find('img')['src'],'width':article.find('img')['width'],'height':article.find('img')['height']}}
            else:

                try:
                    news[index+1] = {'title': article.find('span')['content'], 'url': article['about'],
                                          'image': {'alt': article.find('img')['alt'],
                                                    'src': article.find('img')['src'],
                                                    'width': article.find('img')['width'],
                                                    'height': article.find('img')['height'],
                                                    'title': article.find('img')['title']}}
                except:
                    news[index+1] = {'title': article.find('span')['content'], 'url': article['about'],
                                          'image': {'alt': article.find('img')['alt'],
                                                    'src': article.find('img')['src'],
                                                    'width': article.find('img')['width'],
                                                    'height': article.find('img')['height']}}

    return news

