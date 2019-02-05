from kivy import *
from kivy.app import App
from kivy.core.window import Keyboard
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config, ConfigParser
from kivy.uix.settings import Settings
import random



class trueRoot(FloatLayout):  # The master layout

	def build(self):
		
		self.size_hint = 1, 1
		
		return self


class quickbar(BoxLayout):  # Layout to store quickbar

	def build(self):
		
		self.size_hint = .3, .1
		self.pos_hint = {"right":1, "bottom":1}
		
		return self

	
class healthLayout(FloatLayout):  # Layout to store healthbar

	def build(self):
		
		self.size_hint = 1, 1
		self.pos_hint = {"left":1, "bottom":1}
		
		return self


class healthValue(Label):
	
	def build(self, health=100):
		
		self.size_hint = .3, .05
		self.pos_hint = {'right':.325, 'top':.075}
		self.text = str(health) + '/100'
		
		return self


class widg(Widget):  # The quickbar!

	def build(self):
		
		widg1 = Button(text='test', size=(200, 50), size_hint=(None, None))
		widg2 = Button(text='test', size_hint=(1, 1))
		widg3 = Button(text='test', size_hint=(1, 1))
		widg4 = Button(text='test', size_hint=(1, 1))
		widg5 = Button(text='test', size_hint=(1, 1))
		
		return widg1, widg2, widg3, widg4, widg5


class image(Image):  # The healthbar!

	def build(self):
		
		self.allow_stretch = True
		self.keep_ratio = False
		self.size_hint = .3, .05
		self.pos_hint = {'right':.325, 'top':.075}
		self.source = ("atlas://images/healthBarAtlas/bar")
		
		return self

	
class Background(Image):  # Our world!

	def build(self):
		
		self.source = ("images/game-bg.png")
		self.allow_stretch = True
		self.keep_ratio = False
		self.size_hint = 1, 1
		self.pos_hint = {'top':1.15}
		
		return self

	
class Player(Image):  # The 'player' (currently only a black dot)
		
	def build(self):
		
		self.crouchJump = False
		self.isonground = True
		self.allow_stretch = True
		self.keep_ratio = False
		self.size_hint = .075, .1
		self.source = ("images/cube.png")
		self.pos_hint = {'top':.25}
		self.health = 100
		
		return self

	
class Enemy(Image):
	
	def build(self):
		
		self.source = ("images/enemy.png")
		self.pos_hint = {'top':.695}
		self.keep_ratio = False
		
		return self

	
class Platform(Image):

	def build(self, rand=False):
		
		self.allow_stretch = True
		self.keep_ratio = False
		self.size_hint = .3, .1
		self.source = ("images/platform.png")
		
		if rand:
			self.pos_hint = {'top':random.randint(0, 100) / 100, 'right':random.randint(0, 100) / 100}
		else:
			self.pos_hint = {'top': .4, 'right': .5}
			
		return self


class Size(Label):
	
	def build(self):
		
		self.pos_hint = {'top':1.4, 'right':.65}
		
		return self

	
class Game(Screen):  # The main game class
	
	#======Need player outside build for keyboard events======
	maxPlatforms = 10
	
	player = Player().build()
	bar = image().build()
	
	moving = False
	move = None

	def build(self):
		
		#======Necessary setup for keyboard events======
		
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
		self._keyboard.bind(on_key_up=self.setmovingfalse)
		
		#======Building the GUI======
		troot = trueRoot().build()
		
		main = Background().build()
		
		self.debug = Size().build()
		
		healthBar = healthLayout().build()
		self.healthLabel = healthValue().build(self.player.health)
		
		quick = quickbar().build()
		widgTup = widg().build()
		
		enemy = Enemy().build()
		
		for x in range(1, self.maxPlatforms):
			exec(f'self.platform{x} = Platform().build()')
		
		for x in range(1, len(widgTup)):
			quick.add_widget(widgTup[x])
			
		healthBar.add_widget(self.bar)
		healthBar.add_widget(self.healthLabel)
		
		troot.add_widget (main)
		# troot.add_widget(enemy)
		troot.add_widget(self.player)
		
		for x in range(1, self.maxPlatforms):
			exec(f'troot.add_widget(self.platform{x})')
		self.plat = self.getPlatforms()
		
		troot.add_widget(quick)
		troot.add_widget(healthBar)
		troot.add_widget(self.debug)
		
		self.add_widget(troot)
		# for x in Clock.get_events(): breaks text????
			# x.cancel()
		self.moving = False
		
		return self
	
	def getPlatforms(self):
		
		platList = []
		
		for x in range(1, self.maxPlatforms):
			try:  # dynamically get current platforms in the game (might break something)
				exec(f"platList.append(self.platform{x})")  # courtesy of: https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
			except AttributeError:
				continue
			
		return platList
	
	def health(self, *arg):
		
		app = App.get_running_app().sm.get_screen(name='GAME')  # Used to update health value on screen
		
		if self.player.health == 100:								
			self.bar.source = "atlas://images/healthBarAtlas/bar"  # Use healthbar atlas(or sprite sheet) to update image on screen
			app.healthLabel.text = str(self.player.health) + '/100'  # based on health
			
		if self.player.health < 100 and self.player.health >= 80:
			self.bar.source = "atlas://images/healthBarAtlas/bar1"
			app.healthLabel.text = str(self.player.health) + '/100'
			
		if self.player.health < 80 and self.player.health >= 60:
			self.bar.source = "atlas://images/healthBarAtlas/bar2"
			app.healthLabel.text = str(self.player.health) + '/100'
			
		if self.player.health < 60 and self.player.health >= 40:
			self.bar.source = "atlas://images/healthBarAtlas/bar3"
			app.healthLabel.text = str(self.player.health) + '/100'
			
		if self.player.health < 40 and self.player.health >= 20:
			self.bar.source = "atlas://images/healthBarAtlas/bar4"
			app.healthLabel.text = str(self.player.health) + '/100'
			
		if self.player.health < 20 and self.player.health > 0:
			self.bar.source = "atlas://images/healthBarAtlas/bar5"
			app.healthLabel.text = str(self.player.health) + '/100'
			
		if self.player.health == 0:
			self.bar.source = "atlas://images/healthBarAtlas/bar6"
			app.healthLabel.text = str(self.player.health) + '/100'
		
	def _keyboard_closed(self):
		
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		
		for x in Clock.get_events():
			x.unschedule()
			
		self.moving = False
		self._keyboard = None
	
	def setmovingfalse(self, keyboard, keycode):  # Cease movement
		
		self.moving = False
		try:
			self.move.cancel()
		except AttributeError:
			pass
		self.move = None

	def left(self, *arg):  # You're going left!
		
		if self.player.center_x >= 0:
			self.player.center_x -= (self.size[0] * .0033333)
			
			return True
		
	def right(self, *arg):  # You're going right!
		
		if self.player.center_x <= self.size[0]:
			self.player.center_x += (self.size[0] * .0033333)
			
			return True
		
	def down(self, *arg):  # ... come on get down with the sickness!
		
		self.player.center_y -= (self.size[1] * .0083333)
		
		if self.player.center_y <= (self.size[1] * .2):
			self.player.center_y = (self.size[1] * .2)
			self.player.isonground = True
			self.player.crouchJump = False
			
			return False

	def up(self, *arg):  # Get up!
		
		if not self.player.crouchJump:
			
			try:
				if not self.temp:
					self.temp = self.player.center_y
			except:
				self.temp = self.player.center_y
				
			else:
				self.player.center_y += (self.size[1] * .0083333)
				
			for platform in self.plat:
				if self.player.center_y - (self.player.size[1] * .5) >= (platform.center_y + platform.size[1] * .5) and self.player.center_x - (self.player.size[0] * .5) <= platform.center_x + (platform.size[0] * .5) and self.player.center_x + (self.player.size[0] * .5) >= platform.center_x - (platform.size[0] * .5):
					self.player.center_y = (platform.center_y + 2 * platform.size[1] * .5)
					self.player.isonground = True
					
					return False
				
			if self.player.center_y - (self.size[1] * .1666666) >= self.temp:
				Clock.schedule_interval(self.down, 1 / 60)  # follow the 2-step program
				self.player.isonground = False
				
				return False
			
		else:
			
			try:
				if not self.temp:
					self.temp = self.player.center_y
			except:
				self.temp = self.player.center_y
				
			else:
				self.player.center_y += (self.size[1] * .0166666)
				
			for platform in self.plat:
				if self.player.center_y - (self.player.size[1] * .5) >= (platform.center_y + platform.size[1] * .5) and self.player.center_x - (self.player.size[0] * .5) <= platform.center_x + (platform.size[0] * .5) and self.player.center_x + (self.player.size[0] * .5) >= platform.center_x - (platform.size[0] * .5):
					self.player.center_y = (platform.center_y + 2 * platform.size[1] * .5)
					self.player.isonground = True
					
					return False
				
			if self.player.center_y - (self.size[1] * .3333333) >= self.temp:  # and not self.player.isonground:
				Clock.schedule_interval(self.down, 1 / 60)  # follow the 2-step program
				self.player.isonground = False
				
				return False
			
	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		
		if (keycode[1] == 't'): #Debug keybind
			app = App.get_running_app().sm.get_screen(name='GAME')
			# app.debug.text = str(app.get_parent_window().size[0]) + 'x' + str(app.get_parent_window().size[1]) #showing current window size
			app.debug.text = str(self.plat[0].size_hint_x)  # testing platform list
			
		if (keycode[1] == 'h'): #Debug the health
			try:
				self.player.health -= 10
			except AttributeError:
				self.player.health = 100
			Clock.schedule_interval(self.health, 1 / 60)
			
		#====== WASD keybinds ======
		
		if (keycode[1] == 'w' or keycode[1] == 'up') and self.player.isonground:
			Clock.schedule_interval(self.up, 1 / 60)
			self.player.pos_hint = {None:None}
			
		if (keycode[1] == 's' or keycode[1] == 'down') and self.player.isonground:
			self.player.crouchJump = True
			self.player.pos_hint = {None:None}
			
		if (keycode[1] == 'a' or keycode[1] == 'left') and self.player.center_x >= 0:  # and self.player.isonground:
			
			checkList = []
			
			for x in range(0, self.maxPlatforms - 1):	#checking if player is on any platforms
				checkList.append(1)
				
			for platform in self.plat:
				try:
					if not self.move:
						self.move = Clock.schedule_interval(self.left, 1 / 60)
				except AttributeError:
					pass
				
				self.moving = True
				
				if (self.player.center_x - (self.player.size[0] * .5) >= platform.center_x + (platform.size[0] * .5) or self.player.center_x + (self.player.size[0] * .5) <= platform.center_x - (platform.size[0] * .5))and self.player.center_y - (self.player.size[1] * .5) >= (platform.center_y + platform.size[1] * .5):
					checkList[self.plat.index(platform)] = 0	#if player is on platform, mark it on the list
					
			if not checkList.count(0) > 0:						#if player is on  at least 1 platform, don't fall (in theory)
				Clock.schedule_interval(self.down, 1 / 60)
				
		if (keycode[1] == 'd' or keycode[1] == 'right') and self.player.center_x <= self.size[0]:  # and self.player.isonground:
			
			checkList = []
			
			for x in range(0, self.maxPlatforms - 1):
				checkList.append(1)
				
			for platform in self.plat:
				
				try:
					if not self.move:
						self.move = Clock.schedule_interval(self.right, 1 / 60)
				except AttributeError:
					pass
				
				self.moving = True
				
				if (self.player.center_x - (self.player.size[0] * .5) >= platform.center_x + (platform.size[0] * .5) or self.player.center_x + (self.player.size[0] * .5) <= platform.center_x - (platform.size[0] * .5))and self.player.center_y - (self.player.size[1] * .5) >= (platform.center_y + platform.size[1] * .5):
					checkList[self.plat.index(platform)] = 0
					
			if not checkList.count(0) > 0:
				Clock.schedule_interval(self.down, 1 / 60)
				
		return True

			
class BrutalReign(App):  # The application itself

	def build_config(self, config):
		
		config.setdefaults('Default', {
			'Title': 'Brutal Reign'})

	def build(self):
		
		self.title = self.config.get('Default', 'Title')
		self.sm = ScreenManager()
		self.sm.size_hint = 1, 1  # fill the window
		self.sm.add_widget(Game(name='GAME').build())  # add the Game screen
		self.sm.current = 'GAME'  # set the current screen
		
		return self.sm  # and off we go!

	
if __name__ == '__main__':
	
	BrutalReign().run()
