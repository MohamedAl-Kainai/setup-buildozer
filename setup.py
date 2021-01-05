from kivy.lang import Builder
from kivymd.app import MDApp

v7x = '''
Screen: 	
	MDFloatingActionButtonSpeedDial
		data: app.row
		rotation_root_button: True	  
	MDFillRoundFlatButton
		text: 'Ghost Yuotube'
		pos_hint: {'center_x':.5,'center_y':.5}
		text_color: 2,0,4,6
		md_bg_color: 0,1,0,1
	MDIconButton:
		icon: 'discord'
		pos: 220,400
		user_font_size: "60sp"
'''
class FirstApp(MDApp):
	row = {
	  	
    	'youtube': 'Ghost YT',
    	'facebook': 'Ghost YT',
    	'telegram': 'Ghost YT',
    	'discord': 'SHEMO#6371',
    
	
	}
	def build(self):
		return Builder.load_string(v7x)
		
FirstApp().run()
