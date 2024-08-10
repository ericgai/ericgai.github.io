import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_slideshow_template(n_pics,i,sup_directory):
  # makes a template for a slideshow container with index i containing n_pics pictures
  print('<div class="slideshow-container"> \n')
  for j in range(n_pics):
    print(f'<div class="mySlides{i}">')
    print(f'  <div class="numbertext">{j+1} / {n_pics}</div>')
    print(f'  <img src="/{sup_directory}/IMG_0000.JPEG" style="width:100%">')
    print('  <i>CAPTION</i>')
    print('</div> \n')

  print(f'<a class="prev" onclick="plusSlides(-1,{i})">❮</a>')
  print(f'<a class="next" onclick="plusSlides(1,{i})">❯</a> \n')
  print('</div>')

if __name__=='__main__':
  make_slideshow_template(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])