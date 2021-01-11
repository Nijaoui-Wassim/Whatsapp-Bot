from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.common.keys import Keys

def getNews():
	print('getting news')
	text_box = browser.find_element_by_class_name("_2wP_Y")
	response = "Let me fetch and send top 5 latest news:\n"
	text_box.send_keys(response)
	soup = BeautifulSoup(requests.get(url).content, "html5lib")
	articles = soup.find_all('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d YKEnGe EyNMab t6ttFe Fm1jeb EjqUne")
	news = [i.find_all('a',class_="ipQwMb Q7tWef")[0].text for i in articles[:5]]
	print('got here')
	links = [root+i.find('a')['href'][1:] for i in articles[:5]]
	links = [requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode() for link in links]
	for i in range(5):
		text_box.send_keys(news[i] + "==>" + links[i] + "\n")

def main():
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com')
    browser.maximize_window()
    #sleep(20)  A 2 second pause
    paragraphs = []
    while True:
        x=input('Please sign in first and then enter "done" :  ')
        if x : break
            




    print('starting')
    bot_users = {} # A dictionary that stores all the users that sent activate bot 
    while True:
            unread = browser.find_elements_by_class_name("OUeyt") # The green dot tells us that the message is new
            name,message  = '',''
            if len(unread) > 0:
                    ele = unread[-1]
                    action = webdriver.common.action_chains.ActionChains(browser)
                    action.move_to_element_with_offset(ele, 0, -20) # move a bit to the left from the green dot
            
            # Clicking couple of times because sometimes whatsapp web responds after two clicks
                    try:
                            action.click()
                            action.perform()
                            action.click()
                            action.perform()
                    except Exception as e:
                            pass
                    try:
                            name = browser.find_element_by_class_name("_3TEwt").text  # Contact name
                            print("Contact name :  ", name)
                            message = browser.find_elements_by_class_name("_3zb-j")[-1]  # the message content
                            print("message :  ", message.text.lower())
                            if 'go' in message.text.lower():
                                    if name not in bot_users:
                                            paragraphs = words()
                                            bot_users[name] = True
                                            text_box = browser.find_element_by_class_name("_1Plpp")
                                            #response = "Hi "+name+". Wassim's Bot here :). Now I am activated for you\n"
                                            for i in paragraphs:
                                                for j in i.split():
                                                    text_box.send_keys(j)
                                                    text_box.send_keys(Keys.ENTER)
                                                    sleep(1)
                            if name in bot_users:
                                    if 'show' in message.text.lower() and 'news' in message.text.lower():
                                            getNews()
                            if 'deactivate' in message.text.lower():
                                    if name in bot_users:
                                            text_box = browser.find_element_by_class_name("_1Plpp")
                                            response = "Bye "+name+".\n"
                                            text_box.send_keys(response)
                                            del bot_users[name]
                    except Exception as e:
                            print(e)
                            pass
            sleep(2) # A 2 second pause so that the program doesn't run too fast


def words():
    temp = []
    paragraphs = []
    file1 = open("text.txt","r+", encoding="utf8")
    #print(file1)
    for parag in file1.readlines():
        #if len(parag.split("\n")) > 3:
        temp.append(parag.split("\n"))

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if len (temp[i][j]) > 3 :
                paragraphs.append(temp[i][j])
    return paragraphs





if __name__ == "__main__":
    main()
    #paragraphs()
