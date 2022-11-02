def colorChange(color): #subrountine
	if color=="red":
		return("\33[31m")
	elif color=="white":
		return("\033[0m")
	elif color=="yellow":
		return("\033[33m")
	elif color=="green":
		return("\033[32m")
	elif color=="purple":
		return("\033[35m")
		
title = f"{colorChange('red')} = {colorChange('white')}=
 {colorChange('blue')}={colorChange('yellow)'}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"					{title:^35}")
 
	