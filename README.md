# Toc Project - 晚餐吃什麼#
***

每天的早午晚餐都在想下一餐可以吃什麼 <br>
早午餐可以叫同學想 但下午下課大家就各自回家 晚餐還是要靠自己想啊


***
bot有3個需要選擇的項

* distance
	+ near
	+ far
* price
	+ 100down
	+ 100up
* category
	+ noodles
	+ rices
* 在任何狀態輸入**selectagain**都可以回到一開始的狀態重新選擇

***

bot在/start之後會在distance，此時可以輸入near或far選擇距離，near是育樂街範圍，far是離開育樂街範圍但都是騎車5分鐘以內的範圍。選擇距離後會進入price(有price1,price2)，可以輸入100down或100up選擇價位為100元以下或以上。選擇價位後會進入category(有category1~category4)，可以輸入noodles或rices選擇種類為吃面或吃飯。最後會進入state(有state1~state8)，會對應你的選擇給出對應的餐店介紹網站，可以點擊連結或輸入selectagain回到distance重新選擇。

* 進入price的2個state會跳出"select price:'100up' or '100down' or 'selectagain'"的訊息
* 進入category的4個state會跳出"select 'noodles' or 'rices' or 'selectagain'"的訊息
* 進入state的8個state會跳出"*相應的餐店的介紹網頁* or 'select again'"
* 在任何state輸入selectagain回到distance時會跳出"select distance:'near' or 'far'"

***
![GitHub](https://097f773f.ngrok.io/show-fsm)
***
<strike>如果你連選距離、價位、吃什麼種類二選一都選不到</strike> <br>
<strike>那你就都亂選一個就好了</strike> <br>
<strike>如果選來選去都不想吃那就自己想吧XD</strike>
 






