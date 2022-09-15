import qrcode 

data = 'www.discord.com/channels/992088686319644763/992101361531506839'

img = qrcode.make(data)

img.save('C:/Users/PRINCE/Desktop/data analysis/myqrcode.png')
