from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os 
def video(): 
    directory='C:\Users\student\Desktop\картинки питон' 
    files = os.listdir(directory) 
    images = list(filter(lambda x: x.endswith(' jpg'), files)) 
    clips = [ImageClip(m). set_ duration(2) for m in images] 7 8 

    final_clip = concatenate_videoclips(clips, method='compose') 
    final_clip.write_videofile('test.mp4' , fps=24)








def dd(t, i):
    im = Image.new('RGB', (1000,1000), color=('#101B56'))
    font = ImageFont.truetype('C:/WINDOWS/Fonts/SITKA.TTC', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100, 100),
        t,
        font=font,
        fill='#FFFFFF')
    im.show()
    im.save(str(i)+'image.png')


t = ['Не учи математику','Учи математику','Косинусом называется','абсцисса точки','лежащей на триганометрической окружности','1','2','3','4','5']
for i in range(10):
    dd(t[i], i)
