from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_distance(self, update):
        text = update.message.text
        return text.lower() == 'selectagain'
    
    def is_going_to_price1(self, update):
        text = update.message.text
        return text.lower() == 'near'

    def is_going_to_price2(self, update):
        text = update.message.text
        return text.lower() == 'far'

    def is_going_to_category1(self, update):
        text = update.message.text
        return text.lower() == '100down'

    def is_going_to_category2(self, update):
        text = update.message.text
        return text.lower() == '100up'

    def is_going_to_category3(self, update):
        text = update.message.text
        return text.lower() == '100down'

    def is_going_to_category4(self, update):
        text = update.message.text
        return text.lower() == '100up'

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'noodles'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'rices'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'noodles'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'rices'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'noodles'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'rices'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'noodles'

    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'rices'
	
    def on_enter_distance(self, update):
        update.message.reply_text("select distance:'near' or 'far'")
        print('enter distance')

    def on_enter_price1(self, update):
        update.message.reply_text("select price:'100up' or '100down' or 'selectagain'")
        print('enter price1')

    def on_enter_price2(self, update):
        update.message.reply_text("select price:'100up' or '100down' or 'selectagain'")
        print('enter price2')

    def on_enter_category1(self, update):
        update.message.reply_text("select 'noodles' or 'rices' or 'selectagain'")
        print('enter category1')

    def on_enter_category2(self, update):
        update.message.reply_text("select 'noodles' or 'rices' or 'selectagain'")
        print('enter category2')

    def on_enter_category3(self, update):
        update.message.reply_text("select 'noodles' or 'rices' or 'selectagain'")
        print('enter category3')

    def on_enter_category4(self, update):
        update.message.reply_text("select 'noodles' or 'rices' or 'selectagain'")
        print('enter category4')

    def on_enter_state1(self, update):
        update.message.reply_text("http://boylondon.pixnet.net/blog/post/106473659-%E5%8F%B0%E5%8D%97%E2%80%A7%E6%9D%B1%E5%8D%80-%E5%A4%A7%E9%86%AC%E5%B7%9D%E9%BA%B5%E9%A4%A8 or 'selectagain'")
        print('enter state1')    

    def on_enter_state2(self, update):
        update.message.reply_text("http://blog.xuite.net/linweichean79/wretch/161956720-%E9%A3%9F%E8%A8%98+%E6%88%90%E5%A4%A7-%E6%B4%BB%E5%8A%9B%E5%B0%8F%E5%BB%9A or 'selectagain'")
        print('enter state2')

    def on_enter_state3(self, update):
        update.message.reply_text("http://pinkmayday0928.pixnet.net/blog/post/459150811-%E2%9C%BF%E5%8F%B0%E5%8D%97%E2%9C%BF-%E8%82%B2%E6%A8%82%E8%A1%97%E4%BA%BA%E6%B0%A3%E9%BA%BB%E8%BE%A3%E5%B9%B2%E9%8D%8B%EF%BC%81%E9%87%8D%E5%8F%A3%E5%91%B3%E4%BA%BA%E5%BF%85 or 'selectagain'")
        print('enter state3')

    def on_enter_state4(self, update):
        update.message.reply_text("http://imsean.pixnet.net/blog/post/43287250-%E5%8F%B0%E5%8D%97-%E6%88%90%E5%A4%A7%E5%91%A8%E9%82%8A---%E5%85%83%E5%91%B3%E5%B1%8B-%5B%E8%A8%98%E6%86%B6%E4%B9%8B%E5%91%B3%5D or 'selectagain'")
        print('enter state4')

    def on_enter_state5(self, update):
        update.message.reply_text("http://cosxsmallu.pixnet.net/blog/post/41779051-%E2%98%85%E9%A3%9F%E8%A8%98%E2%98%85-%E5%8F%B0%E5%8D%97---%E9%84%AD%E8%A8%98%E5%AE%A2%E5%AE%B6%E7%B2%84%E6%A2%9D or 'selectagain'")
        print('enter state5')

    def on_enter_state6(self, update):
        update.message.reply_text("http://smith1113422.pixnet.net/blog/post/256634735-%E5%88%86%E4%BA%AB%E9%A3%9F%E8%A8%98-%E5%8F%B0%E5%8D%97-%E6%9D%BE%E6%B1%9F%E5%A3%BD%E5%8F%B8 or 'selectagain'")
        print('enter state6')

    def on_enter_state7(self, update):
        update.message.reply_text("http://amanda390.com/2016-03-05-218/ or 'selectagain'")
        print('enter state7')

    def on_enter_state8(self, update):
        update.message.reply_text("http://heartinkstone.pixnet.net/blog/post/166348797-%5B%E9%A3%9F%E8%A8%98%5D%5B%E5%8F%B0%E5%8D%97%5D-%E6%9D%B1%E5%8D%80-%E6%88%90%E5%A4%A7%E6%A0%A1%E5%8D%80-in%27s-%E9%A3%B2%E9%A3%9F%E5%9D%8A---%E6%B5%B7%E5%8D%97 or 'selectagain'")
        print('enter state8')
