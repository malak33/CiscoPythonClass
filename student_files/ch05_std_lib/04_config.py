import configparser

config = configparser.ConfigParser()

try:
    with open('./userprefs.ini', 'w', encoding='utf8') as f:
        try:
            config['User Data'] = {'mode': 'advanced', 'verbose': str(False)}
            config['Prefs'] = {'recent_files': str(5)}
            # config.add_section('Prefs')                   # classic approach, duplicate section will generate a configparser.Error
            config.write(f)
        except configparser.Error as e:
            print('Error {err}'.format(err=e))
except IOError as e:
    print('Error {err}'.format(err=e))


config = configparser.ConfigParser()
print(config.sections())
config.read('./userprefs.ini')
print(config.sections())
print(config['User Data']['mode'])
