from pymt import *

c = Container()

for i in range (20):
		img_src = 'bilder/testpic'+str(i+1)+'.jpg'
		x , y =  i/5*300+150, i%5*200+100
		b = ImageButton(img_src, parent=c, scale=0.16, pos = (x,y))
		b.status = 'not zoomed'
		
		anim = b.add_animation('zoom','x', 400, 1.0/60, .2)
		anim = b.add_animation('zoom','y', 300, 1.0/60, .2)
		anim = b.add_animation('zoom','scale', 1.0, 1.0/60, .2)
		
		anim = b.add_animation('shrink','x', x, 1.0/60, .2)
		anim = b.add_animation('shrink','y', y, 1.0/60, .2)
		anim = b.add_animation('shrink','scale', 0.24, 1.0/60, .2)
		
		def click(w):
			if w.status == 'zoomed':
				w.start_animations('shrink')
				w.status = 'not_zoomed'
			else:
				w.start_animations('zoom')
				w.status = 'zoomed'		
				
		b.clickActions.append(  curry(click,b)  )
		c.add_widget(b)
		
w = UIWindow(c)
w.set_fullscreen()
runTouchApp()