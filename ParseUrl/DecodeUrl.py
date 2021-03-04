from urllib.parse import unquote
text='https%3A%2F%2Ff.video.weibocdn.com%2FmY3RBynvlx07KmKlBoYE01041200DhFl0E010.mp4%3Flabel%3Dmp4_hd%26template%3D480x852.25.0%26trans_finger%3Dd8257cc71422c9ad30fe69ce9523c87b%26ori%3D0%26ps%3D1BVp4ysnknHVZu%26Expires%3D1613314170%26ssig%3Din3rxvxoFX%26KID%3Dunistore%2Cvideo'
text = unquote(text, 'utf-8')

print(text)
