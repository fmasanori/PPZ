#baixar antes https://raw.github.com/defnull/bottle/master/bottle.py
import bottle

@bottle.route('/')
def home_page():
  return 'Alô minha página Zumbi'

@bottle.route('/outra')
def test_page():
  return 'Outra página Zumbi'

bottle.debug(True)
bottle.run(host='localhost', port = 8082)

