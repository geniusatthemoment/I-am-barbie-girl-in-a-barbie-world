from PIL import Image, ImageDraw, ImageFont

def dd(t):
    im = Image.new('RGB', (1000,1000), color=('#101B56'))
    font = ImageFont.truetype('C:/WINDOWS/Fonts/SITKA.TTC', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100, 100),
        t,
        font=font,
        fill='#FFFFFF')
    im.show()


t = ['Не учи математику','Учи математику']
dd(t[0])
dd(t[1])







