from urllib.request import urlretrieve
from subprocess import Popen, PIPE
from flask import Flask
import json

app = Flask(__name__)

@app.route('/number-plate/<media_url>')
def number_plate(media_url: str):
    media_url = media_url.replace('secure', 'https').replace('slash', '/').replace('dot', '.').replace('colon', ':').replace('dash', '-').replace('ampersand', '&').replace('per', '%').replace('ques', '?')
    urlretrieve(media_url, r'D:\prana\Programming\Server\assets\main.png')
    proc = Popen(r'python D:\prana\Programming\Deep-Recognition\plate_recognition.py --api-key None D:\prana\Programming\Server\assets\main.png'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, _ = proc.communicate()
    try:
        output = json.loads(output.decode())[0]['results'][0]['plate']
    except:
        return 'No Number Plate Found.'
    return output
    
@app.route('/face-mask/<media_url>')
def face_mask(media_url: str):
    media_url = media_url.replace('secure', 'https').replace('slash', '/').replace('dot', '.').replace('colon', ':').replace('dash', '-').replace('ampersand', '&').replace('per', '%').replace('ques', '?');
    urlretrieve(media_url, r'C:\Users\tejas\Desktop\Roadlance\Deep-Recognition\Mask-Recognition\Face-Mask-Detection\images\main.jpeg')
    os.chdir(r'C:\Users\tejas\Desktop\Roadlance\Deep-Recognition\Mask-Recognition\Face-Mask-Detection')
    proc = Popen(r'python C:\Users\tejas\Desktop\Roadlance\Deep-Recognition\Mask-Recognition\Face-Mask-Detection\detect_mask_image.py -i images\main.jpeg'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, _ = proc.communicate()
    output = eval(output.decode())
    return f'{output}'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
