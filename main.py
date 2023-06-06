
def pr2():
    from PIL import Image,ImageFilter
    from pathlib import Path

    current_dir =''
    filenames = Path(current_dir).glob('*') #current_dir - папка в которой код, glob - путь до папки, exist_ok - если существует папка создает ее по новой
    Path('new_dir').mkdir(parents=True,exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg','.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter(ImageFilter.EMBOSS)
                new_img.save(Path("new_dir",file))

def pr3():
    import csv
    with open('1.csv',newline='') as File:
        reader = csv.reader(File)
        k = 0
        suma = 0
        for row in reader:
            if k == 0:
                print('Нужно купить:')
            else:
                print(row[0] + ' - ' + row[1] + ' шт. за ' + row[2] + ' руб.')
                suma = suma + (int(row[1]) * int(row[2]))
            k +=1
        print('Итоговая сумма:',suma)

pr3()