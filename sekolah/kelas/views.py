from django.shortcuts import render


def kelas(request):
    judul= [ "kelas 1", "kelas 2", " kelas 3" ]
    pemilik= "SDN waru barat 7"
    
    konteks={
        'title':judul,
        'pemilik': pemilik,
        
    }
    return render(request,'kelas.html',konteks)
