import json
import urllib.request

def get_birds_data():
    url = 'https://aves.ninjas.cl/api/birds'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data

def generate_site():
    birds = get_birds_data()

    with open('aves_de_chile.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="es">\n')
        f.write('<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('<title>Aves de Chile</title>\n')
        f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n')
        f.write('<style>\n')
        f.write('.card-height { height: 100%; }\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<div class="container">\n')
        f.write('<h1 class="mt-4 mb-4">Aves de Chile</h1>\n')
        f.write('<div class="row">\n')
        for bird in birds:
            f.write('<div class="col-lg-4 col-md-6 col-sm-12 mb-4">\n')
            f.write('<div class="card card-height">\n')
            f.write(f'<img src="{bird["images"]["main"]}" class="card-img-top" alt="{bird["name"]["spanish"]}">\n')
            f.write('<div class="card-body">\n')
            f.write(f'<h5 class="card-title">{bird["name"]["spanish"]}</h5>\n')
            f.write(f'<p class="card-text">Nombre en inglés: {bird["name"]["english"]}</p>\n')
            f.write('</div>\n')
            f.write('</div>\n')
            f.write('</div>\n')
        f.write('</div>\n')
        f.write('</div>\n')
        f.write('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>\n')
        f.write('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>\n')
        f.write('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n')
        f.write('</body>\n')
        f.write('</html>\n')

if __name__ == "__main__":
    generate_site()
