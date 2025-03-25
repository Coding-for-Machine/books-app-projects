from .models import Manzil, BizHaqimizda

def site_settings(request):
    manzil = Manzil.objects.last()
    biz = BizHaqimizda.objects.last()
    return {"manzil": manzil,"biz": biz}