import numpy as np
from PIL import Image

# @WARN: don't xor black/white img as flag is too unreadable
lemur_img = Image.open('./media/lemur.png')
flag_img = Image.open('./media/flag.png')

# xor to get super imposed image as
# lemur ^ secretKey = lemur'
# flag ^ secretKey = flag'
# lemur' ^ flag' = (lemur ^ flag) ^ (secretKey ^ secretKey) = (lemur ^ flag) ^ 0 = (lemur ^ flag)
# credits: @jocheim for hints

lemur_np = np.array(lemur_img) * 255
flag_np = np.array(flag_img) * 255
result_np = np.bitwise_xor(lemur_np.astype('uint8'), flag_np.astype('uint8'))

Image.fromarray(result_np).save('./media/lemurFlag.png')