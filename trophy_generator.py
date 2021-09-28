import json

from PIL import Image, ImageDraw, ImageFont


def read_json_from_file(filename):
    f = open(filename)
    data = json.load(f)

    f.close()
    
    return data

def wrap_by_word(s, n):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

def add_text_to_trophy(year, team_name):
    my_image = Image.open("img/trophy.png")
    image_editable = ImageDraw.Draw(my_image)
    
#     image_editable.text((240, 415), year, (0, 0, 0), font=font)
    year_font = ImageFont.truetype('Roboto-Regular.ttf', 24)
    image_editable.text((232, 125), year, (0, 0, 0), font=year_font)
    
    team_name_with_new_line = wrap_by_word(team_name, 2)
    name_font = ImageFont.truetype('Roboto-Regular.ttf', 20)
#     image_editable.text((200, 435), team_name, (0, 0, 0), font=font)
    image_editable.text(
        (255, 75), 
        team_name_with_new_line, 
        (0, 0, 0), 
        font=name_font, 
        align="center", 
        anchor="ms"
    )
    file_name = f"temp/winner_trophy_{year}.png"
    my_image.save(file_name)
    return file_name

def generate_gif_from_winners(token_id, winners):
    trophy_images = [add_text_to_trophy(winner[0], winner[1]) for winner in winners]
    im = Image.open(trophy_images[0])
    im.save(f"output/winner_trophy_{token_id}.gif", save_all=True, append_images=[Image.open(img) for img in trophy_images[1:]], optimize=False, duration=1000, loop=0)
