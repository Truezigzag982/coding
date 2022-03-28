from wordcloud import WordCloud
from matplotlib import pyplot as plt
filename = "English.txt"
with open(filename, encoding="utf-8") as f:
    data = f.read()
    font = "/System/Library/Fonts/Times.ttc"
    wc = WordCloud(font_path=font,
                background_color='white',
                width=1000,
                height=800,
                ).generate(data)
    wc.to_file('词云图.png')
    plt.imshow(wc)
    plt.axis('off')
    plt.show()