from ota import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/OperationAzura/microPythonOTAExample.git')
     o.download_and_install_update_if_available('DWW 2.4', 'bazinga1')


 def start():
     print('bingo!')
     print('bingo!')
     print('bingo!')
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...


 def boot():
     download_and_install_update_if_available()
     start()


 boot()