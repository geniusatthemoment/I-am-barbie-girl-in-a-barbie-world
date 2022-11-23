from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import 
import os 
def video: 
di='C:/Users/student/Documents/1326/Пустовалов Михаил/pictore maker' 
fis-os.listdir (di) ims-list (filter (lambda x: x.endswith (" • jpg') , fis) ) clips-[ImageClip (m) .set duration (2) for m in ims1 9 final clip-concatenate Videoclips (clips, method-'compose") 10 final clip.write _video?ile (' cool.webm', [ps-24)
3 4' from moviepy.editor import E import os directory = C:/Users/Lfybk/OneDrive/Рабочий стол/Lessons/Слайд Шоу^ 
files = os.listdir(directory) 
images = List(filter (Lambda x: x.endswith(' jpg'), files)) 
clips = [ImageClip(m). set_ duration(2) for m in imges] 7 8 
final_clip = concatenate_videoclips(cLips, method='compose') 
final_cLip.write_videofile('test.mp4;fps=24)








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


    
    