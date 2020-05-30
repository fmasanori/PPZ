import bottle

@bottle.route('/')
def home_page():
  mythings = ['Python', 'Ruby', 'Perl', 'C++']
  return bottle.template('hello_world2', {'username': 'Masanori',
                                          'things':mythings})
@bottle.post('/favorita')
def favorita():
  lang = bottle.request.forms.get('lang')
  if lang == None or lang == '':
    lang = 'Nenhuma escolhida'
  bottle.response.set_cookie('lang', lang)
  bottle.redirect('/show_lang')

@bottle.route('/show_lang')
def show_lang():
  lang = bottle.request.get_cookie('lang')
  return bottle.template('lang_selection', {'lang':lang})
                         
bottle.debug(True)
bottle.run(host='localhost', port = 8082)
