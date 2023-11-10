import moviepy.editor as mpy
"""
libx264 yüklemek için https://www.imagemagick.org/script/download.php
adresinden imagemagick programını indirip kurun. Kurulum esnasında lisanslı
libx264 de kurulacaktır.
Başka çözüm yöntemleride internette bulunabilir. Ancak en kestirmesi bu!
"""

vcodec =   "libx264"
videoquality = "24"
"""
Sıkıştırma işlemi belirtiliyor: Aşağıda seçenekler var
slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
ben "slow" seçtim.
"""
compression = "slow"

"""
Kesip yapıştıracağım ana .mp4, .m4v uzantılı video adını aşağıya yazın
kesilecek dosya ile bu program aynı klasörde olmalı
"""
title = "1080P - Kopya.mp4"
loadtitle = title
"""
kesip yapıştırıldıktan sonraki son halinin adını belirleyin
"""

savetitle = 'Kes_Ekle_' + title 

"""
nereden kesilecek ve birleştirilecekleri listele, 10-15 sn ve 20-25 sn arasını kes
ve birleştir
"""
cuts = [('00:00:10.000', '00:00:15.000'),('00:00:20.000', '00:00:25.000')]



# mpy modülü ana video dosyasını yükler
video = mpy.VideoFileClip(loadtitle)

# dosyayı keselim. cuts listesinde kaç parça var ise sırası ile işlenecek
clips = []
for cut in cuts:
             clip = video.subclip(cut[0], cut[1])
             clips.append(clip)

final_clip = mpy.concatenate_videoclips(clips)


final_clip = mpy.CompositeVideoClip([final_clip])

# dosyayı kaydet
final_clip.write_videofile(savetitle, threads=4, fps=24,
                          codec=vcodec,
                          preset=compression,
                          ffmpeg_params=["-crf",videoquality])

video.close()



