import datetime

def praejo_laiko(metai):
    data = datetime.datetime.strptime(metai, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    skirtumas = now - data

    print("Praejo metu:", skirtumas.days // 365)  # dvigubas // palieka sveika skaiciu
    print("Praejo menesiu:", round(skirtumas.days / 365) * 12)
    print("Praejo dienu:", skirtumas.days)
    print("Praejo valandu:", round(skirtumas.total_seconds() / 3600))
    print("Praejo minuciu:", round(skirtumas.total_seconds() / 60))
    print("Praejo sekundziu:", round(skirtumas.total_seconds()))

praejo_laiko(input("Iveskite data YYYY-MM-DD HH:MM:SS "))